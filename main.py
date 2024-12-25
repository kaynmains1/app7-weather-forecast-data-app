import streamlit as st
import numpy as np
import pandas as pd


st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:", placeholder="Enter a city", key="place")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="Select the number of forecast days", key="days")
box = st.selectbox(label="Select data to view", options=("Temperature", "Sky"), key="box")
st.subheader(f"{box} for the next {days} days in {place.capitalize()}")
chart = st.line_chart("")