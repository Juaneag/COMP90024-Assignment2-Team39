import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import DATA, get_url, state_name, aggregate_volunteer_work_data, get_default_state_value, get_series_data

st.set_page_config(page_title="Sudo Volunteer Work", page_icon="📈")
st.markdown('''
#### Sudo Volunteer Work
Compare Volunteer work vs not a volunteer for each state

_from SA2-based B19 Voluntary Work for an Organisation or Group by Age by Sex as at 2011-08-11_
''')

VOLUNTEER = "Volunteer"
NONVOLUNTEER = "Non-Volunteer"

if __name__ == '__main__':
    data = []
    url = get_url(DATA.VOLUNTARY_WORK)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    formatted_data = aggregate_volunteer_work_data(data)
    volunteer_data = get_default_state_value()
    non_volunteer_data = get_default_state_value()

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