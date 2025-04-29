# Financial FTP Application

This project provides a simple way to set up an FTP server using Docker. It utilizes the `bogem/ftp` image to create a configurable FTP server for financial services.

## Project Structure

```
financial-ftp-app
├── docker-compose.yml
├── configs
│   └── ftp
│       └── config.txt
├── scripts
│   └── start.sh
└── README.md
```

## Prerequisites

- Docker installed on your machine
- Docker Compose installed

## Getting Started

To get started with the Financial FTP Application, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/financial-ftp-app.git
   cd financial-ftp-app
   ```

2. **Configure the FTP server:**

   Edit the `configs/ftp/config.txt` file to set up your FTP server settings, including user credentials and directory permissions.

3. **Start the FTP server:**

   Run the following command to start the Docker containers:

   ```bash
   ./scripts/start.sh
   ```

4. **Access the FTP server:**

   Once the server is running, you can connect to it using an FTP client with the credentials specified in the `config.txt` file.

## Stopping the Server

To stop the FTP server, you can run:

```bash
docker-compose down
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.