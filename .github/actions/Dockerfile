# Use official Python base image
FROM python:3.11-slim

# Install system packages including Git
# RUN apt-get update && \
#     apt-get install -y git && \
#     rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY *files.txt /app/
COPY repo_file_changes.py /app/

# Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the Python script
CMD ["python", "/app/repo_file_changes.py"]
