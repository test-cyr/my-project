# Stage 1: Build
FROM node:18-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine

COPY build /usr/share/nginx/html
COPY nginx default.conf /etc/nginx/conf.d/default.conf
COPY ssl/ /etc/nginx/ssl/
