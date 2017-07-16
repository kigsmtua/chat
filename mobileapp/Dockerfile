FROM node:6.10

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

npm install -g ionic cordova

CMD ionic serve
