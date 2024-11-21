from fastapi import FastAPI
from .models import HealthResponse

app = FastAPI(title="Vercel DB Demo API")

@app.get("/api/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        version="0.1.0"
    )
