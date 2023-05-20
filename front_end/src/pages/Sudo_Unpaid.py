import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import get_url, DATA, state_name, aggregate_unpaid_assistance_data, default_state_value

st.set_page_config(page_title="Sudo Unpaid", page_icon="📈")
st.markdown('''
#### Sudo Unpaid
Show total females unpaid assistance for each state 

_from LGA-I09 Unpaid Assistance to a Person with a Disability by Age by Sex for Aboriginal & Torres Strait Islander Persons-Census 2016_
''')

TOTAL = "Females total number unpaid assistance"

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
    url = get_url(DATA.UNPAID_ASSISTANCE)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    formatted_data = aggregate_unpaid_assistance_data(data)
    total_data = default_state_value

    for item in formatted_data:
        total_data[item["key"]] += round(item["value"]["f_tot_no_upaid_assist_pvded"], 2)

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