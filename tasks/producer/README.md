# 1. Producer Task Documentation

This documentation provides instructions on how to install, configure, and run the Producer Task. The Producer Task is responsible for consuming data from the Django FTP Consumer Application and sending it to RabbitMQ for further processing.

---

## 1.1. Setup

### 1.1.1. Prerequisites

Before starting, ensure you have the following installed on your system:

- Python 3.8 or higher
- Virtual environment tools (e.g., `venv`)
- RabbitMQ server running (refer to the [RabbitMQ Server README](../../financial-rabbitmq/README.md))
- Django FTP Consumer Application running (refer to the [Django App README](../../app/README.md))

---

### 1.1.2. Installation

1. **Clone the Repository**

   Clone the project to your local machine:
   ```bash
   cd tasks/producer

2. **Create and Activate a Virtual Environment**

   Clone the project to your local machine:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

    Linux/Mac
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install Dependencies**

   Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

   Copy the [.env.example](\.env.example) file to [.env](\.env) and update the values as needed

   Ensure the following variables are correctly set:

   - RABBITMQ_USERNAME: RabbitMQ username
   - RABBITMQ_PASSWORD: RabbitMQ password
   - RABBITMQ_HOST: RabbitMQ host (e.g., localhost)
   - RABBITMQ_PORT: RabbitMQ port (default: 5672)
   - DJANGO_HOST: URL of the Django application (e.g., http://localhost:8000)


## How It Works

### 1. Data Consumption from Django App
The Producer Task fetches a list of FTP connections from the Django FTP Consumer Application. It sends a GET request to the following endpoint:

The response contains a list of FTP connection details, including:
- `host`: FTP server hostname
- `port`: FTP server port
- `content_type`: Type of content being processed (e.g., JSON, CSV, XML)

    ![Swagger Documentation](/tasks/producer/docs/fetch_data_django.png)

### 2. Data Publishing to RabbitMQ

For each FTP connection retrieved, the Producer Task sends a message to RabbitMQ. The message is routed to a specific queue based on the `content_type` of the FTP connection. The process involves:

  1. Declaring an exchange (`ftp_exchange`) of type `topic`.
  2. Declaring a queue named `ftp.<content_type>` (e.g., `ftp.json`, `ftp.csv`).
  3. Binding the queue to the exchange with a routing key matching the `content_type`.
  4. Publishing a message containing the FTP connection details to the appropriate queue.

  ![RabbitMQ Queue](/tasks/producer/docs/rabbitmq_queues.png)