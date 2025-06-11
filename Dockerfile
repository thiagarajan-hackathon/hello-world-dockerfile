
FROM python:3.11-slim

LABEL Description="This Dockerfile runs a Python script that prints 'Hello world!!' and keeps the container alive for 5 hours."

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY hello.py .

# Run the script
CMD ["python", "hello.py"]
