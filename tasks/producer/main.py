import asyncio
import os

import aiohttp
import pika
from dotenv import load_dotenv

load_dotenv()

DJANGO_HOST = os.getenv('DJANGO_HOST')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT'))
RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

async def fetch_ftp_connections():
    """
    Fetches a list of FTP connections from the Django API.

    This function sends an asynchronous GET request to the Django API endpoint
    to retrieve a list of FTP connections. It handles potential errors such as
    timeouts and client connection issues.

    Returns:
        list: A list of FTP connections if the request is successful.
              Returns an empty list if an error occurs or if the response status
              code is not 200.

    Raises:
        asyncio.TimeoutError: If the request times out.
        aiohttp.ClientError: If there is an issue with the client connection.

    Notes:
        - The `DJANGO_HOST` variable must be defined and accessible in the scope
          where this function is called.
        - The function uses a timeout of 10 seconds for the request.
    """
    endpoint = "/ftp/api/list/"
    url = f"{DJANGO_HOST}{endpoint}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error: Received status code {response.status} from {url}")
                    return []
    except asyncio.TimeoutError:
        print("Error: Timeout while connecting to the Django API.")
        return []
    except aiohttp.ClientError as e:
        print(f"Error: Failed to connect to the Django API. Details: {e}")
        return []

def send_to_rabbitmq(ftp_connection):
    """
    Sends a message to a RabbitMQ exchange for the given FTP connection.
    This function establishes a connection to a RabbitMQ server, declares an
    exchange and a queue, binds the queue to the exchange with a routing key,
    and publishes a message containing details about the FTP connection.
    Args:
        ftp_connection (dict): A dictionary containing FTP connection details.
            Expected keys are:
                - 'host' (str): The FTP server hostname or IP address.
                - 'port' (int): The port number of the FTP server.
                - 'content_type' (str): The type of content being processed.
    Raises:
        pika.exceptions.AMQPError: If there is an error in connecting to RabbitMQ
            or performing any RabbitMQ operations.
    Example:
        ftp_connection = {
            'host': 'ftp.example.com',
            'port': 21,
            'content_type': 'text'
        }
        send_to_rabbitmq(ftp_connection)
    """
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials)
    )
    channel = connection.channel()

    # Declare the exchange and queue
    exchange_name = 'ftp_exchange'
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic', durable=True)


    queue_name = f"ftp.{ftp_connection['content_type']}"
    channel.queue_declare(queue=queue_name, durable=True)

    routing_key = f"ftp.{ftp_connection['content_type']}"
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
    message = f"FTP Connection: {ftp_connection['host']}:{ftp_connection['port']}"

    # Publish the message
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,
        )
    )
    print(f" [x] Sent {routing_key}:{message}")

    connection.close()

async def main():
    ftp_connections = await fetch_ftp_connections()
    if not ftp_connections:
        print("No FTP connections retrieved. Exiting.")
        return

    for ftp_connection in ftp_connections:
        try:
            send_to_rabbitmq(ftp_connection)
        except Exception as e:
            print(f"Error: Failed to send message to RabbitMQ. Details: {e}")

if __name__ == "__main__":
    asyncio.run(main())