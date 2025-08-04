# Random Number API

A simple FastAPI application that generates random numbers between 0 and 1000.

## Endpoints

- `GET /` - Welcome message
- `GET /random` - Returns a random number between 0 and 1000
- `GET /health` - Health check endpoint

## Deployment

This application is configured for deployment on Railway.app:

1. Create a new project on Railway
2. Connect your GitHub repository
3. Railway will automatically detect it's a Python app and deploy using the railway.json configuration

## Local Development

1. Install dependencies: