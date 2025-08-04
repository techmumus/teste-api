from fastapi import FastAPI
import random
from datetime import datetime

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

@app.get("/time")
async def get_current_time():
    """Returns the current time in ISO format"""
    current_time = datetime.now()
    return {
        "current_time": current_time.isoformat(),
        "formatted_time": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)