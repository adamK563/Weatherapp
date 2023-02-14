from fastapi import APIRouter
from api_client_weather.api.v1.api_calls import get_location_and_weather, get_map_size
router = APIRouter()

@router.get('/')
async def get_weather():
    try:
        city_locations, temprtures = get_location_and_weather()
    except city_locations.error as error:
        raise ConnectionError("Failed to connect to server: {0}".format(error))
    
    map_size = get_map_size(city_locations)
    return city_locations, temprtures, map_size
    