from typing import Union
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
import bcrypt
import os
import yaml
import jwt

app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# db connection
username = 'username'
password = 'password'


IMAGE = 'packet-tracer:local'
DB_URI = 'mongodb://%s:%s@127.0.0.1' % (username, password)
TOKEN_KEY = 'projet2cssiq'

client = MongoClient(DB_URI)


class Login(BaseModel):
    email: str
    password: str


class Register(BaseModel):
    email: str
    username: str
    role: str
    password: str


class Deployment:
    def __init__(self, name, label, ip, image=IMAGE):
        self.name = name
        self.label = label
        self.image = image
        self.ip = ip

    def getFileName(self):
        return "tmp/deployment-" + self.name + ".yaml"

    def getName(self):
        return self.name

    def __getDeploymentTemplate():
        with open("templates/deployment.yaml") as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def __generateDeployment(self):
        template = Deployment.__getDeploymentTemplate()
        template["metadata"]["name"] = self.name
        template['metadata']['labels']['app'] = self.label
        template['spec']['selector']['matchLabels']['app'] = self.label
        template['spec']['template']['metadata']['labels']['app'] = self.label
        template["spec"]["template"]["spec"]["containers"][0]["image"] = self.image
        template['spec']['template']['spec']['containers'][0]['name'] = self.name + '-container'
        template['spec']['template']['spec']['containers'][0]['env'].append({
            "name": "DISPLAY",
            "value": self.ip + ":0.0"
        })
        return template

    def export(self):
        with open(self.getFileName(), "w") as f:
            yaml.dump(self.__generateDeployment(), f)


class DeploymentModel(BaseModel):
    name: str
    label: str
    ip: str


@app.post("/login", status_code=status.HTTP_200_OK)
def login(login: Login, response: Response):
    collection = client['packet-tracer'].users
    user = collection.find_one(login.__dict__)
    if user:
        return {
            'username': user['username'],
            'email': user['email'],
            'role': user['role'],
            'token': jwt.encode(
                {
                    "username": user['username'],
                    "role": user['role']
                }, TOKEN_KEY, algorithm="HS256")
        }
    response.status_code = status.HTTP_401_UNAUTHORIZED


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(register: Register):
    collection = client['packet-tracer'].users
    user = collection.insert_one(register.__dict__)
    if not user:
        response.status_code = status.HTTP_400_BAD_REQUEST


@app.get('/databases')
def get_databases():
    return client.list_database_names()


@app.post('/run-deployment')
def run_packet_tracer(deploymentModel: DeploymentModel):
    deployment = Deployment(deploymentModel.name,
                            deploymentModel.label, deploymentModel.ip)
    deployment.export()

    os.system("kubectl delete deployment " + deployment.getName())
    os.system("kubectl apply -f " + deployment.getFileName())
