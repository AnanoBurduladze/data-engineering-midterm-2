#!/bin/bash

# Docker Image-ის აგება
echo "Building Docker image..."
docker build -t fastapi-sqlite-app .

# Docker კონტეინერის გაშვება
echo "Running Docker container..."
docker run --rm -p 8000:8000 fastapi-sqlite-app

echo "Application is running on http://127.0.0.1:8000"
