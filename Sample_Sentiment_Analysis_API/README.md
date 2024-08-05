
# Sentiment Analysis API

This project demonstrates how to create a sentiment analysis API using FLASK and deploy it on RunPod.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   pip install flask transformers
   pip install --ignore-installed flask
   ```

2. Run the FLASK app:
   ```bash
   python app.py
   ```

3. Send a POST request to test the API:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text":"I love this!"}' http://IP:PORT/analyze
   ```

## Deployment on RunPod

Follow the steps in the video to deploy this project on RunPod.
