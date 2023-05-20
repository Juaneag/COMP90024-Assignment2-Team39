import requests
import streamlit as st
from utils import DATA, get_url, aggregate_home_and_community_data
st.set_page_config(page_title="Page2", page_icon="📈")
st.write("page 1")

if __name__ == '__main__':
    url = get_url(DATA.TWITTER_RELATED)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the response data as needed
        st.write(data)
        # st.write(aggregate_home_and_community_data(data))
    else:
        print("Error:", response.status_code)



