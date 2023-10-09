# Django management app

A management app made with the Django REST Framework.

- [X] Basic CRUD operations over the Article resource.
- [X] Authentication with JWT.
- [X] Unit testing.
- [X] Swagger UI endpoint.
- [X] Containerization with Docker.

## Development

Requirements:

- Python 3.11.x
- Docker (optional)

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

Create a `.env` file based on the `.env.example` file and set the environment variables.

```bash
cp .env.example .env
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

You can also use the `docker-compose.yml` file to run the container. By default, it will bind
the **port 80** to the host machine and create a superuser with the credentials specified in the
`.env` file.

```bash
docker-compose up
```

You can also build and run the image yourself.

```bash
docker build -t django-management-app .

docker run -it -p 8000:8000 \
  --env-file .env \
  django-management-app
```

## Coding style

- For Django settings and properties, prefer the [use of lists over tuples](https://docs.djangoproject.com/en/dev/releases/1.9/#default-settings-that-were-tuples-are-now-lists).
- Use type annotations for function arguments and return values when possible. `self` doesn't need
  to be annotated.
- Prefer single quotes over double quotes.
