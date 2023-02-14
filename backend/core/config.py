import os

class Settings:
    API_V1_PATH = '/api/v1'

    PROJECT_NAME: str = "Weatherapp"
    PROJECT_AUTHOR: str = "Adam Karpovich"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USER: str = os.getenv("MYSQL_DATABASE")
    DATABASE_PASSWORD: str = os.getenv("MYSQL_ROOT_PASSWORD")
    DATABASE_HOST: str = os.getenv("MYSQL_ROOT_HOST")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")

    API_WEATHER_KEY: str = os.getenv("MY_WEATHER_API_KEY")
    WEATHER_API_URL: str = os.getenv("WEATHER_API_URL")

    CITIES: list = os.getenv("CITIES_LIST").split(',')

settings = Settings()