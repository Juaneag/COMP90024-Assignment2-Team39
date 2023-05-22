import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import get_url, DATA, get_chart_option, aggregate_home_and_community_data, get_default_state_value, get_series_data

st.set_page_config(page_title="Sudo Home And Community Care", page_icon="📈")
st.markdown('''
#### Sudo Home And Community Care
Show total assistance count for each state

_from SD Home and Community Care Program 2012-2013_
''')

TOTAL = "Total Instances of Assistance"

if __name__ == '__main__':
    data = []
    url = get_url(DATA.HOME_AND_COMMNUNITY_CARE)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    formatted_data = aggregate_home_and_community_data(data)
    total_data = get_default_state_value()

    for item in formatted_data:
        total_data[item["key"]] += round(item["value"]["hcc_toti_1_no_7_12_6_13"], 2)

    stacked_state_data = [
        get_series_data(TOTAL, total_data),
    ]

    options = get_chart_option(stacked_state_data, [TOTAL])
    st_echarts(options=options, height="500px")