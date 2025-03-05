#!/bin/bash

# Docker Image-ის აგება
echo "Building Docker image..."
docker build -t csv-processor .

# Docker კონტეინერის გაშვება
echo "Running Docker container..."
docker run --rm -v $(pwd):/app csv-processor

echo "Process completed!"
