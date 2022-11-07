FROM node:18.12

WORKDIR /app/front

COPY . /app

ENV PATH /app/node_modeles/.bin:$PATH

COPY package.json /app/package.json

RUN npm config set strict-ssl false
RUN npm install
RUN npm install @vue/cli

CMD npm run serve
