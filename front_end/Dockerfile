FROM node:18-alpine
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Expose the port that the dev server runs on (default Vite port is 5173)
EXPOSE 3000

# Run the development server
CMD ["npm", "run", "dev"]
