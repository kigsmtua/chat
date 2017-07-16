FROM node:6.10

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm install -g ionic cordova

RUN npm install

CMD ionic serve
