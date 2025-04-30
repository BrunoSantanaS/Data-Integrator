- [1. Django Integration Application](#1-django-integration-application)
  - [1.1. Setup](#11-setup)
  - [1.2. Applications Overview](#12-applications-overview)
    - [1.2.1. ftp\_consumer App](#121-ftp_consumer-app)
    - [1.2.2. client\_consumer App](#122-client_consumer-app)
  - [1.3. API Endpoints and Documentation](#13-api-endpoints-and-documentation)
  - [1.4. Running Unit Tests](#14-running-unit-tests)
  - [1.5. Future Features](#15-future-features)
  - [1.6. License](#16-license)


# 1. Django Integration Application

This Django application is part of an integration project designed to consume data from an FTP server emulated via Docker. The app leverages Django REST Framework to expose APIs for managing FTP connections and client transactions.

## 1.1. Setup

1. **Clone the Repository**
   Clone the project to your local machine:
   ```bash
   cd Data-Integrator/app
   ```

2. **Create and Activate a Virtual Environment**
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **Linux:**
     ```bash
     python3 -m venv .venv
     .venv\bin\activate
     ```

3. **Install Dependencies**
   Install the packages listed in [requirements.txt](../app/requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   Apply the Django migrations:
   ```bash
   python manage.py migrate
   ```

5. **Run the Application**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   The service will be available at [http://localhost:8000](http://localhost:8000).

## 1.2. Applications Overview

### 1.2.1. ftp_consumer App

The [ftp_consumer](../app/ftp_consumer/) app manages FTP connections and provides a RESTful API for operations such as creating, listing, updating, deleting, and retrieving FTP connection records.

### 1.2.2. client_consumer App

The [client_consumer](../app/client_consumer/) app manages client transactions and provides a RESTful API for operations such as creating and listing client transaction records.

## 1.3. API Endpoints and Documentation

API documentation is automatically generated using [drf-spectacular](https://drf-spectacular.readthedocs.io/). You can access interactive API documentation through Swagger:

- **Swagger UI:**
  - FTP & Client Consumer: [http://localhost:8000/api/docs/](http://localhost:8000/ftp/api/docs/)

- **Schema:**
  - FTP & Client Consumer: [http://localhost:8000/api/schema/](http://localhost:8000/ftp/api/schema/)

Using Swagger, you can try out the endpoints directly from your browser.

![Swagger Documentation](/app/docs/images/swagger_interface.png)

## 1.4. Running Unit Tests

Unit tests are provided to ensure the integrity of all API operations. To execute the tests, run:

```bash
python manage.py test
```

Tests cover key functionalities for both apps:
- **ftp_consumer:** Creating, listing, updating, deleting, and retrieving FTP connection records.
  Detailed tests can be found in [ftp_consumer/tests/](../app/ftp_consumer/tests/).

- **client_consumer:** Creating and listing client transaction records.
  Detailed tests can be found in [client_consumer/tests/](../app/client_consumer/tests/).

## 1.5. Future Features

- **User Authentication:**
  Implement login functionality to secure API endpoints.

- **API Permissions:**
  Enforce permissions for accessing individual API endpoints.

- **Advanced FTP Operations:**
  Extend FTP functionalities with additional operations and error handling.

- **Transaction Filtering:**
  Add support for filtering client transactions by client name, transaction type, or date range.

- **Pagination:**
  Implement pagination for endpoints to handle large datasets efficiently.

- **Deployment Considerations:**
  Provide guidelines for deploying the WSGI server to scale the application. This may include configuring multiple worker processes (using Gunicorn or uWSGI), setting up a reverse proxy (such as Nginx), and implementing load balancing.

## 1.6. License

This project is licensed under the MIT License.