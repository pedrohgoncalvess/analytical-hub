FROM node:latest

WORKDIR /usr/src/app

COPY . .

RUN npm install

RUN npm run build

CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5000" ]