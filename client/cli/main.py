import typer
import socket
import requests
import json


API_URL = "http://192.168.36.60:8000" #l'address de serveur 

app = typer.Typer()


def getIpAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


IP = getIpAddress()


class Deployment:
    def __init__(self, name, label, ip):
        self.name = name
        self.label = label
        self.ip = ip


@app.command()
def login():

    email = typer.prompt("E-mail")
    password = typer.prompt("Password", hide_input=True)

    credentials = {
        "email": email,
        "password": password
    }

    response = requests.post(API_URL + '/login', data=json.dumps(credentials))

    if response.status_code != 200:
        typer.secho("Invalid credentials", fg="red")
        return

    user = response.json()

    typer.secho("Login successfull", fg="green")
    typer.secho("Starting Packet tracer please wait ... ", fg="green")

    deployment = Deployment(
        user['username'], user['username'], IP).__dict__
    requests.post(API_URL + '/run-deployment', data=json.dumps(deployment))


@app.command()
def registre():

    email = typer.prompt("E-mail")
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)

    credentials = {
        "email": email,
        "username": username,
        "password": password,
        "role": "client"

    }

    response = requests.post(API_URL + '/register',
                             data=json.dumps(credentials))

    if response.status_code != 201:
        typer.secho("Invalid credentials", fg="red")
        return

    typer.secho("Register successfull", fg="green")


if __name__ == "__main__":
    app()
