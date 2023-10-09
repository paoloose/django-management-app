FROM python:3.11-alpine

WORKDIR /app

RUN set -xe;

COPY . /app

RUN python3 -m pip install -r ./requirements.txt; \
    cd ./backend; \
    python3 ./manage.py makemigrations; \
    python3 ./manage.py migrate; \
    addgroup -g 1000 appuser; \
    adduser -u 1000 -G appuser -D -h /home/appuser -s /bin/sh appuser; \
    chown -R appuser:appuser /app;

# Install tini
RUN apk add --no-cache tini

# Install the tree utility
RUN apk add --no-cache tree

RUN tree -L 5

USER appuser
EXPOSE 8000/tcp
ENTRYPOINT [ "tini", "--" ]
CMD [ "python3", "./backend/manage.py", "runserver", "0.0.0.0:8000" ]
