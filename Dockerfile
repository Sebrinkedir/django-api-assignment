# Use official Python image with a clear version tag
FROM python:3.11-slim-bullseye

# Don't buffer logs, no .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and tools
RUN pip install --upgrade pip setuptools wheel

# Copy and install requirements
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Expose port for web
EXPOSE 8000
