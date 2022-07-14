FROM python:3.9-alpine
MAINTAINER Prabhjeet

EXPOSE 8080

# Keeps python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN apt-get update
COPY requirements.txt .
RUN python -m pip install --trusted-host pypi.python.org -r requirements.txt

COPY ./app /app
WORKDIR /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disable-password --gecos "" appuser && chown -R appuser /app
USER appuser

COPY start_django.sh /app/
CMD ./start_django.sh
