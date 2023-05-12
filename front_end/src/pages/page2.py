
import streamlit as st

st.set_page_config(page_title="Page2", page_icon="📈")
st.write("page 2")
st.sidebar.header("page 2")
st.markdown(
    """
    This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
)