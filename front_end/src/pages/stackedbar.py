import streamlit as st
from streamlit_echarts import st_echarts

st.set_page_config(page_title="show map with date from couchDB", page_icon="📈")
st.write("page 2")

options = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["20-24", "25-29", "30-34", "35-39", "40-44"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["New South Wales", "Victoria", "Queensland", "South Australia", "Western Australia", "Tasmania", "Australian Capital Territory", "Northern Territory"],
    },
    "series": [
        {
            "name": "20-24",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [320, 302, 301, 334, 390, 330, 320],
        },
        {
            "name": "25-29",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "30-34",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "35-39",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [150, 212, 201, 154, 190, 330, 410],
        },
        {
            "name": "40-44",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [820, 832, 901, 934, 1290, 1330, 1320],
        },
    ],
}
st_echarts(options=options, height="500px")