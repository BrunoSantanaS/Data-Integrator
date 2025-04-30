- [1. Financial FTP Application](#1-financial-ftp-application)
  - [1.1. What is an FTP Server?](#11-what-is-an-ftp-server)
- [2. Project Structure](#2-project-structure)
- [3. Instalation](#3-instalation)
  - [3.1. Prerequisites](#31-prerequisites)
  - [3.2. Getting Started](#32-getting-started)
  - [3.3. Stopping the Server](#33-stopping-the-server)
  - [3.4. License](#34-license)


# 1. Financial FTP Application

This project provides a simple way to set up an FTP server using Docker. It utilizes the `bogem/ftp` image to create a configurable FTP server for simulating financial services from external partners.

In this demo every Client Folder will hold a different file format to be consumed by automated task files that will be consumed are: `CSV`, `XML` and `JSON`

## 1.1. What is an FTP Server?

An FTP (File Transfer Protocol) server is a service that enables the transfer of files between computers over a network. It allows users to upload, download, and manage files remotely, making it ideal for sharing data securely and efficiently.

# 2. Project Structure

```
financial-ftp-app
├── docker-compose.yml
├── configs
│   └── ftp
│       └── config.txt
│       └── client1    <- Simulates an FTP server
│       └── client2    <- Simulates an FTP server
│       └── client3    <- Simulates an FTP server
|
├── scripts
│   └── start.sh
└── README.md
```

*Note: The client directories (client1, client2, client3) are abstracted for demo purposes to simulate different FTP servers from various sources.*

# 3. Instalation

This section provides information on how to run the service using Docker

## 3.1. Prerequisites

- Docker installed on your machine
- Docker Compose installed

## 3.2. Getting Started

To get started with the Financial FTP Server Application, follow these steps:

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

## 3.3. Stopping the Server

To stop the FTP server, you can run:

```bash
docker-compose down
```

## 3.4. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.