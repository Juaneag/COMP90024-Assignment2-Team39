import copy
import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import DATA, get_url, state_name, aggregate_volunteer_work_data

VOLUNTEER = "Volunteer"
NONVOLUNTEER = "Non-Volunteer"
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
    url = get_url(DATA.VOLUNTARY_WORK)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    default_state_value = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    formatted_data = aggregate_volunteer_work_data(data)
    volunteer_data = copy.deepcopy(default_state_value)
    non_volunteer_data = copy.deepcopy(default_state_value)

    for item in formatted_data:
        volunteer_data[item["key"]] += item["value"]["P_Tot_Volunteer"]
        non_volunteer_data[item["key"]] += item["value"]["P_Tot_N_a_volunteer"]

    stacked_state_data = [
        get_series_data(VOLUNTEER, volunteer_data),
        get_series_data(NONVOLUNTEER, non_volunteer_data)
    ]

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": [VOLUNTEER, NONVOLUNTEER]
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