import requests
import streamlit as st
from streamlit_echarts import st_echarts
from utils import DATA, get_url, get_chart_option, get_series_data, get_default_state_value

st.set_page_config(page_title="Twitter Compare Related", page_icon="📈")
st.markdown('''
#### Twitter Compare Related
Compare Twitter data of related vs unrelated tweets with charity in each state
''')

RELATED = "Related"
UNRELATED = "Unrelated"

if __name__ == '__main__':
    data_related = []
    data_unrelated = []
    url_related = get_url(DATA.TWITTER_RELATED)
    url_unrelated = get_url(DATA.TWITTER_UNRELATED)
    response_related = requests.get(url_related)
    response_unrelated = requests.get(url_unrelated)
    if response_related.status_code == 200 and response_unrelated.status_code == 200:
        data_related = response_related.json()
        data_unrelated = response_unrelated.json()
    else:
        print("Error:", response_related.status_code)
        print("Error:", response_unrelated.status_code)

    volunteer_data = get_default_state_value()
    non_volunteer_data = get_default_state_value()

    for item in data_related:
        volunteer_data[item["key"]] += item["value"]
    for item in data_unrelated:
        non_volunteer_data[item["key"]] += item["value"]

    stacked_state_data = [
        get_series_data(RELATED, volunteer_data),
        get_series_data(UNRELATED, non_volunteer_data)
    ]

    options = get_chart_option(stacked_state_data, [RELATED, UNRELATED])
    st_echarts(options=options, height="500px")