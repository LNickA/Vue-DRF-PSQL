FROM node:18.12

WORKDIR /app/front

ENV PATH /app/node_modeles/.bin:$PATH

COPY package.json /app/package.json

RUN npm config set strict-ssl false
RUN npm install

COPY . /app
CMD npm run serve