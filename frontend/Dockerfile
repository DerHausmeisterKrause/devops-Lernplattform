FROM node:20-alpine
WORKDIR /app
COPY package.json server.js index.html ./
RUN npm config set strict-ssl false && npm install --no-audit --no-fund
CMD ["npm","start"]
