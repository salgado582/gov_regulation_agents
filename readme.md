# Hackathon Project

This repository contains a multi-service application developed for a hackathon. The project is composed of separate services for the frontend, backend, and an instructlab component, as well as a MongoDB database. All services are containerized using Docker and orchestrated via Docker Compose.

## Repository Structure

/project-root /front_end Dockerfile ...other frontend files... /backend Dockerfile ...other backend files... /instructlab Dockerfile ...other instructlab files... docker-compose.yaml README.md

cpp
Copy

- **front_end/**: Contains the code and Dockerfile for the frontend application.
- **backend/**: Contains the code and Dockerfile for the backend service.
- **instructlab/**: Contains the code and Dockerfile for the instructlab service.
- **docker-compose.yaml**: Orchestrates all containers including the MongoDB database.

## Prerequisites

- [Docker](https://www.docker.com/get-started)  
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup and Running the Project

1. **Clone the Repository:**

bash

Run the following command to build the Docker images and start all services:

bash
Copy
docker-compose up --build
This command will:

Build images for front_end, backend, and instructlab based on their respective Dockerfiles.
Pull and run the official MongoDB image.
Start all services as defined in the docker-compose.yaml file.
Access the Services:

Frontend: http://localhost:3000
Backend: http://localhost:5000
InstructLab: http://localhost:8080
MongoDB: Accessible on port 27017 (if you need to connect directly)
Configuration
Environment Variables:
The docker-compose.yaml file sets environment variables (e.g., NODE_ENV and MONGO_URL) for the backend. You can modify these values as needed.

Networking:
All services are connected through a common Docker network, which allows them to communicate using service names.

Development and Debugging
Rebuilding Containers:
If you make changes to a service, you can rebuild and restart the container using:

bash
Copy
docker-compose up --build
Viewing Logs:
To view the logs for a specific service, use:

bash
Copy
docker-compose logs -f [service_name]
Troubleshooting:

Ensure Docker and Docker Compose are installed and running.
Check container logs for any errors.
Verify that environment variables are correctly configured.

For Front-end:

- Open front_end directry.
- Write the following commands:
- npm install
- npm run dev


