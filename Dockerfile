FROM python:3.11-slim

LABEL Description="This Dockerfile runs a Python script that prints 'Hello world!!' and keeps the container alive for 5 hours."

# Create the Python script
RUN echo 'import time\nprint("Dockerfile: Hello world !!")\nend_time = time.time() + 5 * 60 * 60\nwhile time.time() < end_time:\n    time.sleep(60)' > /app/hello.py

# Set the working directory
WORKDIR /app

# Run the script
CMD ["python", "hello.py"]
