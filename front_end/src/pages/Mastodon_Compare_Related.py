import copy
import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import DATA, get_url

st.set_page_config(page_title="Mastodon Compare Related", page_icon="📈")
st.markdown('''
#### Mastodon Compare Related
Compare related vs unrelated toots
''')

RELATED = "Related"
UNRELATED = "Unrelated"

def get_series_data(name, data):
    return {
        "name": name,
        "type": "bar",
        "stack": "total",
        "label": {"show": True},
        "emphasis": {"focus": "series"},
        "data": data,
    }

if __name__ == '__main__':
    data = []
    url = get_url(DATA.MASTODON_TOOTS)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    formatted_data = {d["key"]: d["value"] for d in data}

    stacked_state_data = [
        get_series_data(RELATED, [formatted_data[1]]),
        get_series_data(UNRELATED, [formatted_data[0]])
    ]

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": [RELATED, UNRELATED]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "inverse": True,
            "data": ["Mastodon"],
        },
        "series": stacked_state_data,
    }
    st_echarts(options=options, height="500px")