# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system packages including Git
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Copy project files into the container
COPY repo_file_changes.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script
CMD ["python", "repo_file_changes.py"]
