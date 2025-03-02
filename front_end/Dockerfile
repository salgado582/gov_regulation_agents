# Stage 1: Build the Vue app
FROM node:16-alpine as build-stage
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code and build the application
COPY . .
RUN npm run build

# Stage 2: Serve the built application using Nginx
FROM nginx:stable-alpine as production-stage
# Remove default Nginx website content
RUN rm -rf /usr/share/nginx/html/*
# Copy built files from previous stage to Nginx's directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 80 to the Docker host
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
