# Use a lightweight Python 3.11 image as our base
FROM python:3.11-slim

# Update & install only what's necessary
RUN apt-get update && \
    apt-get install -y git build-essential sudo curl cmake && \
    git --version && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspaces/instructlab

# Copy your entire local project into the container
# COPY . /workspaces/instructlab/

# Install Python dependencies (InstructLab)
RUN pip install instructlab

# Default command

