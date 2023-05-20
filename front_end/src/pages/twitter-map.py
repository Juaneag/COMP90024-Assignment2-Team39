import streamlit as st
import pydeck as pdk
import requests
import streamlit as st
from utils import DATA, get_url, aggregate_home_and_community_data
from db_data import twitter_related

state_location = {
    "1": { "latitude": -32.0, "longitude": 147.0, "state_name": "New South Wales" },
    "2": { "latitude": -36.75, "longitude": 144.75, "state_name": "Victoria" },
    "3": { "latitude": -20.0, "longitude": 143.0, "state_name": "Queensland" },
    "4": { "latitude": -26.0, "longitude": 121.0, "state_name": "Western Australia" },
    "5": { "latitude": -30.0, "longitude": 135.0, "state_name": "South Australia" },
    "6": { "latitude": -42.0, "longitude": 146.0, "state_name": "Tasmania" },
    "7": { "latitude": -19.0, "longitude": 133.0, "state_name": "Northern Territory" },
    "8": { "latitude": -35.5, "longitude": 149.0, "state_name": "Australian Capital Territory" },
    "9": { "latitude": 0.0, "longitude": 0.0, "state_name": "Other"},
}

if __name__ == '__main__':
    data = []
    chart_data = []
    url = get_url(DATA.TWITTER_RELATED)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    for item in data:
        key = item["key"]
        location_data = state_location[key]
        state_location[key].update(item)

        chart_data.append(state_location[key])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-32.27,
            longitude=133.77,
            zoom=3.5,
            pitch=50,
        ),
        tooltip={"html": "<b>State:</b> {state_name}<br><b>Count:</b> {value}", "style": { "color": "white" }},
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position=["longitude", "latitude"],
                get_fill_color="[255 * (10 - value / 100), 255 * (value / 100), 0, 255]",
                get_radius="value*100",
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ],
    ))