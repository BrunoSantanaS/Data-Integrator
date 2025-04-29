# Django FTP Consumer Application

This Django application is part of an integration project designed to consume data from an FTP server emulated via Docker. The app leverages Django REST Framework to expose APIs for managing FTP connections.

## Setup

1. **Clone the Repository**
   Clone the project to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd Data-Integrator/app
   ```

2. **Create and Activate a Virtual Environment**

   Windows:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   Linux:
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

## The ftp_consumer App

The [ftp_consumer](../app/ftp_consumer/) app is responsible for managing FTP connections. It defines a RESTful API with endpoints to create, list, update, delete, and retrieve FTP connection records.

### API Endpoints and Swagger Documentation

API docs are automatically generated using [drf-spectacular](https://drf-spectacular.readthedocs.io/). You can access interactive API documentation through Swagger:

- **Swagger UI:** [http://localhost:8000/ftp/api/docs/](http://localhost:8000/ftp/api/docs/)
- **Schema:** [http://localhost:8000/ftp/api/schema/](http://localhost:8000/ftp/api/schema/)

Using Swagger, you can try out the endpoints directly from your browser.

## Running Unit Tests

Unit tests are provided to ensure the integrity of FTP connection operations. To execute the tests, run:

```bash
python manage.py test ftp_consumer
```

Tests cover key functionalities such as creating, listing, updating, deleting, and retrieving FTP connection records. Detailed tests can be found in [ftp_consumer/tests/](../app/ftp_consumer/tests/).

## Future Features

- **User Authentication:**
  Implement login functionality to secure API endpoints.

- **API Permissions:**
  Enforce permissions for accessing individual API endpoints.

- **Advanced FTP Operations:**
  Extend FTP functionalities with additional operations and error handling.

- **Deployment Considerations:**
  Provide guidelines for deploying the WSGI server to scale the application. This may include configuring multiple worker processes (using Gunicorn or uWSGI), setting up a reverse proxy (such as Nginx), and implementing load balancing.

## License

This project is licensed under the MIT License.