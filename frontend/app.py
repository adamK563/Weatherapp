import folium
import streamlit as st
from streamlit_folium import st_folium
import requests
import sys
sys.path.append('../')
from backend.core.config import settings
from backend.main import origins

base_url = origins[0]

st.set_page_config(
    page_title="world weather",
    page_icon=":world_map:️",
    layout="wide",
)
st.title("🌎 Welcome To The WeatherApp")
get_started = st.button(label="Start the map")

if "cities" not in st.session_state:
    st.session_state.cities = []

if "cities" not in st.session_state:
    st.session_state.cities = []

if "temprtures" not in st.session_state:
    st.session_state.temprtures = []

if get_started:
    url = base_url + settings.API_V1_PATH + "/weather"            
    response_get_map = requests.get(url)
    data = response_get_map.json()

    if response_get_map.status_code == 200:
        st.success(response_get_map)
    else:
        st.error(response_get_map)

data

# map = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=2)

# # add markers for each city on the map
# for city, location, temp in zip(st.session_state.cities, st.session_state.cities, st.session_state.temprtures):
#     folium.Marker(location, popup=city, tooltip=str(temp)).add_to(map)


# st_folium(map, width=725)

