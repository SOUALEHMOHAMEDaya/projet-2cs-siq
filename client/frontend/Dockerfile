FROM node:12-alpine    

RUN mkdir -p /var/www/html/client

WORKDIR /var/www/html/client

COPY package.json .
RUN npm install

COPY . .


EXPOSE 3000

CMD [ "npm","run","dev" ]