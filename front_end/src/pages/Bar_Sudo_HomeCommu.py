import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import get_url, DATA, state_name, aggregate_home_and_community_data

TOTAL = "Total Instances of Assistance"
st.set_page_config(page_title="show map with date from couchDB", page_icon="📈")
st.write("page 2")

def get_series_data(name, data):
    data_list = list(data.values())
    return {
        "name": name,
        "type": "bar",
        "stack": "total",
        "label": {"show": True},
        "emphasis": {"focus": "series"},
        "data": data_list,
    }

if __name__ == '__main__':
    data = []
    url = get_url(DATA.HOME_AND_COMMNUNITY_CARE)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    default_state_value = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    formatted_data = aggregate_home_and_community_data(data)
    total_data = default_state_value

    for item in formatted_data:
        total_data[item["key"]] += round(item["value"]["hcc_toti_1_no_7_12_6_13"], 2)

    stacked_state_data = [
        get_series_data(TOTAL, total_data),
    ]

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": [TOTAL]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "inverse": True,
            "data": list(state_name.values()),
        },
        "series": stacked_state_data,
    }
    st_echarts(options=options, height="500px")