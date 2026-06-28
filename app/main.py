from fastapi import FastAPI

app = FastAPI(
    title="RideFlow API",
    version="1.0.0",
    description="Backend for RideFlow - Intelligent Ride Dispatch Platform"
)

@app.get("/")
def root():
    return {"message": "RideFlow API is running 🚖"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }