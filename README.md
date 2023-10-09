# Django management app

A management app made with the Django REST Framework.

- [X] Basic CRUD operations over the Article resource.
- [X] Authentication with JWT.
- [ ] Unit testing.
- [ ] Query optimization with the Django ORM.

## Development

Setup a Python virtual environment and install the dependencies.

```bash
python -m venv .venv

# unix
source .venv/bin/activate
# windows
.venv\Scripts\activate.bat
```

Apply the migrations and create a superuser. A SQLite3 database will be created in the project
directory.

```bash
python manage.py migrate
python manage.py createsuperuser
```

Start the development server and visit <http://localhost:8000/api/>.

```bash
python manage.py runserver
```

## Code style

- For Django settings and properties, prefer the [use of lists over tuples](https://docs.djangoproject.com/en/dev/releases/1.9/#default-settings-that-were-tuples-are-now-lists).
- Use type annotations for function arguments and return values when possible. `self` doesn't need
  to be annotated.
- Prefer single quotes over double quotes.
