import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import DATA, get_url, get_default_state_value, state_name, aggregate_unpaid_assistance_data, aggregate_home_and_community_data, aggregate_volunteer_work_data, get_series_data

st.set_page_config(page_title="Combine Related", page_icon="📈")
st.markdown('''
#### Combine Related
Compare all SUDO data and total tweets related to charity in each state 
''')

RELATED = "Twitter"
SUDO_HOME_AND_COMMU = "Total Instances of Assistance"
SUDO_UNPAID = "Females Total Number Unpaid Assistance"
SUDO_VOLUNTEER = "Total Volunteer"
DATA_SERIES_TYPE = "line"

if __name__ == '__main__':
    data_twitter = []
    data_sudo_volunteer_work = []
    data_sudo_home_and_commu = []
    data_sudo_unpaid = []
    response_twitter = requests.get(get_url(DATA.TWITTER_RELATED))
    response_sudo_volunteer_work = requests.get(get_url(DATA.VOLUNTARY_WORK))
    response_sudo_home_and_commu = requests.get(get_url(DATA.HOME_AND_COMMNUNITY_CARE))
    response_sudo_unpaid = requests.get(get_url(DATA.UNPAID_ASSISTANCE))

    if response_twitter.status_code == 200 and response_sudo_volunteer_work.status_code == 200 and response_sudo_home_and_commu.status_code == 200 and response_sudo_unpaid.status_code == 200:
        data_twitter = response_twitter.json()
        data_sudo_volunteer_work = response_sudo_volunteer_work.json()
        data_sudo_home_and_commu = response_sudo_home_and_commu.json()
        data_sudo_unpaid = response_sudo_unpaid.json()
    else:
        print("Error: Failed to load data")

    related_twitter_data = get_default_state_value()
    sudo_volunteer_work = get_default_state_value()
    sudo_unpaid = get_default_state_value()
    sudo_home_and_commnunity = get_default_state_value()

    formatted_sudo_volunteer_work = aggregate_volunteer_work_data(data_sudo_volunteer_work)
    formatted_sudo_unpaid = aggregate_unpaid_assistance_data(data_sudo_unpaid)
    formatted_sudo_home_and_commnunity = aggregate_home_and_community_data(data_sudo_home_and_commu)

    for item in data_twitter:
        related_twitter_data[item["key"]] += item["value"]

    for item in formatted_sudo_volunteer_work:
        sudo_volunteer_work[item["key"]] += item["value"]["P_Tot_Volunteer"]

    for item in formatted_sudo_unpaid:
        sudo_unpaid[item["key"]] += round(item["value"]["f_tot_no_upaid_assist_pvded"], 2)

    for item in formatted_sudo_home_and_commnunity:
        sudo_home_and_commnunity[item["key"]] += round(item["value"]["hcc_toti_1_no_7_12_6_13"], 2)

    stacked_state_data = [
        get_series_data(RELATED, related_twitter_data, DATA_SERIES_TYPE),
        get_series_data(SUDO_VOLUNTEER, sudo_volunteer_work, DATA_SERIES_TYPE),
        get_series_data(SUDO_UNPAID, sudo_unpaid, DATA_SERIES_TYPE),
        get_series_data(SUDO_HOME_AND_COMMU, sudo_home_and_commnunity, DATA_SERIES_TYPE)
    ]

    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": [RELATED, SUDO_VOLUNTEER, SUDO_UNPAID, SUDO_HOME_AND_COMMU]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "yAxis": {"type": "value"},
        "xAxis": {
            "type": "category",
            "inverse": True,
            "data": list(state_name.values()),
            "axisLabel": {
                "interval": 0,
                "rotate": 30
            }
        },
        "series": stacked_state_data,
    }
    st_echarts(options=options, height="500px")