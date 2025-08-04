from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Random Number API"}

@app.get("/random")
async def get_random_number():
    """Returns a random number between 0 and 1000"""
    random_number = random.randint(0, 1000)
    return {"random_number": random_number}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)