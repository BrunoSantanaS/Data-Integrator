# Navigate to the project directory
cd "$(dirname "$0")/.."

# Start the Docker containers
docker-compose up -d

# Display the status of the containers
docker-compose ps

if docker-compose ps | grep -q 'rabbitmq'; then
    echo "RabbitMQ server is up and running."
else
    echo "RabbitMQ server is not running."
fi