import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import get_url, DATA, get_chart_option, aggregate_unpaid_assistance_data, get_default_state_value, get_series_data

st.set_page_config(page_title="Sudo Unpaid", page_icon="📈")
st.markdown('''
#### Sudo Unpaid
Show total females unpaid assistance for each state 

_from LGA-I09 Unpaid Assistance to a Person with a Disability by Age by Sex for Aboriginal & Torres Strait Islander Persons-Census 2016_
''')

TOTAL = "Females total number unpaid assistance"

if __name__ == '__main__':
    data = []
    url = get_url(DATA.UNPAID_ASSISTANCE)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)

    formatted_data = aggregate_unpaid_assistance_data(data)
    total_data = get_default_state_value()

    for item in formatted_data:
        total_data[item["key"]] += round(item["value"]["f_tot_no_upaid_assist_pvded"], 2)

    stacked_state_data = [
        get_series_data(TOTAL, total_data),
    ]

    options = get_chart_option(stacked_state_data, [TOTAL])
    st_echarts(options=options, height="500px")