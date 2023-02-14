from fastapi import FastAPI
from routers.api.v1 import weather
from core.config import settings

app = FastAPI()

origins = [
    "http://localhost:8501",
    "http://localhost:8000",
]

app.include_router(
	weather.router, 
	prefix= settings.API_V1_PATH + "/weather", 
	tags=["Weather"]
)

@app.get("/")
async def root():
    return {"message": "Hello Weatherapp Backend Application!"}