import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

from utils import connectToDB, getLocationData

st.set_page_config(page_title="show map with date from couchDB", page_icon="📈")
st.write("page 2")
db = connectToDB()

i_lat = -30
i_long = 120.7
i_lat2 = -32
i_long2 = 122.7
data1 = np.random.randn(1000, 2) / [50, 50] + [i_lat, i_long]
data2 = np.random.randn(1000, 2) / [50, 50] + [i_lat-2, i_long+2]
data3 = np.random.randn(1000, 2) / [50, 50] + [i_lat+5, i_long]
data = data1 + data2 + data3

chart_data = pd.DataFrame(
   getLocationData(db),
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=-32.27,
        longitude=133.77,
        zoom=3.5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))