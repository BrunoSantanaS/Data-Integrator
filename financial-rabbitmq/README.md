- [1. Financial RabbitMQ Application](#1-financial-rabbitmq-application)
  - [1.1. What is RabbitMQ?](#11-what-is-rabbitmq)
  - [1.2. Project Purpose](#12-project-purpose)
- [2. Project Structure](#2-project-structure)
- [3. Instalation](#3-instalation)
  - [3.1. Prerequisites](#31-prerequisites)
  - [3.2. Getting Started](#32-getting-started)
  - [3.3. Stopping the Server](#33-stopping-the-server)
  - [3.4. License](#34-license)


# 1. Financial RabbitMQ Application

This project sets up a RabbitMQ container that acts as the message broker to manage and route requests for running automated scripts. RabbitMQ is responsible for receiving requests, routing them to different queues, and ensuring that each consumer processes only the intended data.

## 1.1. What is RabbitMQ?

RabbitMQ is an open-source message broker that implements the Advanced Message Queuing Protocol (AMQP). It enables communication between different components of a system by passing messages between producers and consumers in a reliable and scalable way.

## 1.2. Project Purpose

In this project, RabbitMQ functions as the intermediary between the system's Producer and Consumer components:
- **Producer:** Sends messages to an Exchange.
- **Exchange:** Routes each message to a specific queue based on criteria (JSON, XML, or CSV).
- **Queue:** Holds requests, with each queue corresponding to a different file format.
- **Consumer:** Processes the requests from their designated queue.

This architecture allows automated scripts to be executed according to the type of request received, enabling a clean separation of concerns and scalable task processing.

# 2. Project Structure

When a message is created by the producer the topic is identified and sent to the correct Queue that will be processed for the specific Consumer.

![RabbitMQ Infrastructure](docs\images\rabbitmq_infra.png)

# 3. Instalation

This section provides information on how to run the service using Docker

## 3.1. Prerequisites

- Docker installed on your machine
- Docker Compose installed

## 3.2. Getting Started

To start the RabbitMQ server using Docker, follow these steps:

1. **Clone the repository:**

   ```bash
   cd financial-rabbitmq
   ```

2. **Start the RabbitMQ Server:**

   Run the following command to bring up the RabbitMQ container:

    ```bash
    ./scripts/start.sh
    ```

3. **Access the RabbitMQ Management Interface:**

   Once the container is running, you can access the RabbitMQ Management Interface by navigating to [http://localhost:15672](http://localhost:15672) in your web browser. The default credentials are set in the docker-compose file (`RABBITMQ_DEFAULT_USER` and `RABBITMQ_DEFAULT_PASS`).


## 3.3. Stopping the Server

To stop the FTP server, you can run:

```bash
docker-compose down
```

## 3.4. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.