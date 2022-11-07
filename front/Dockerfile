FROM node:18.12

WORKDIR /app/front

COPY . /app

ENV PATH /app/node_modeles/.bin:$PATH

COPY package.json /app/package.json

RUN npm config set strict-ssl false
RUN npm install


CMD npm run serve