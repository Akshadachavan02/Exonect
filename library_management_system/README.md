# Library Management System

This is a Django-based Library Management System designed to manage books, authors, and borrowers efficiently. The project includes features for CRUD operations, JWT authentication, and background task processing with Celery.

## Project Structure

```
library_management_system/
├── library_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── library/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── manage.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd library_management_system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL:**
   Update the `DATABASES` setting in `library_management_system/settings.py` with your PostgreSQL database credentials.

5. **Run migrations:**
   ```
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```
   python manage.py runserver
   ```

## API Documentation

The API endpoints are defined in `library/urls.py`. Use Postman or similar tools to interact with the API.

## Background Tasks with Celery

To run background tasks, ensure Redis is installed and running. Update the Celery configuration in `library_management_system/settings.py` and start the Celery worker:

```
celery -A library_management_system worker --loglevel=info
```

## File Uploads

For file uploads, configure the necessary settings in `settings.py` and ensure that your views handle file storage appropriately.

## Query Optimization

Utilize `select_related` and `prefetch_related` in `library/views.py` to optimize database queries for better performance.

## License

This project is licensed under the MIT License.