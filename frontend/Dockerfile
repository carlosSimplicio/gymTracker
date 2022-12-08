FROM node:16.17.1-alpine3.15

WORKDIR /app

COPY package.json .

COPY package-lock.json .

RUN npm ci

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
