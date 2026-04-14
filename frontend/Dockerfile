FROM node:20-alpine
WORKDIR /app
COPY package.json server.js index.html ./
RUN npm install
CMD ["npm","start"]
