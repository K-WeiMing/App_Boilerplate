# Step 1: Build the application
FROM node:16 AS builder
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ .
RUN npm run build

# Step 2: Set up nginx webserver
FROM nginx:stable-alpine
COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]