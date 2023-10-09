FROM python:3.11-alpine

RUN set -xe
RUN python -m pip install --upgrade pip

COPY ./requirements.txt .
RUN python -m pip install -r ./requirements.txt

COPY ./backend /app
COPY .env .
WORKDIR /app

RUN python3 ./manage.py makemigrations
RUN python3 ./manage.py migrate
RUN python3 ./manage.py createsuperuser --noinput
RUN addgroup -g 1000 appuser
RUN adduser -u 1000 -G appuser -D -h /home/appuser -s /bin/sh appuser
RUN chown -R appuser:appuser /app

# Install tini
RUN apk add --no-cache tini

USER appuser
EXPOSE 8000/tcp
ENTRYPOINT [ "tini", "--" ]
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:8000" ]
