#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Start the Docker containers
docker-compose up -d

# Display the status of the containers
docker-compose ps

echo "FTP server is up and running."