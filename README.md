# Django management app

A management app made with the Django REST Framework.

- [X] Basic CRUD operations over the Article resource.
- [X] Authentication with JWT.
- [X] Unit testing.

## Development

Requirements:

- Python 3.11.x

Setup a Python virtual environment and install the dependencies.

```bash
python -m venv .venv

# unix
source .venv/bin/activate
# windows
.venv\Scripts\activate.bat
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Subsequent commands are made in the `./backend` directory:

Apply the migrations and create a superuser. A SQLite3 database will be created in the project
directory.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Start the development server and visit <http://localhost:8000/>.

```bash
python manage.py runserver
```

You'll see a Swagger UI endpoint. Use your newly created credentials to authorize the requests.

## Running with Docker

Build the image.

```bash
docker build -t django-management-app .
# Verify it with `$ docker images`
```

Run the container exposing the port 8000 and create a superuser.

```bash
docker run -it -p 8000:8000 \
  -e DJANGO_SUPERUSER_USERNAME=admin \
  -e DJANGO_SUPERUSER_PASSWORD=password \
  -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
  django-management-app
```

## Code style

- For Django settings and properties, prefer the [use of lists over tuples](https://docs.djangoproject.com/en/dev/releases/1.9/#default-settings-that-were-tuples-are-now-lists).
- Use type annotations for function arguments and return values when possible. `self` doesn't need
  to be annotated.
- Prefer single quotes over double quotes.
