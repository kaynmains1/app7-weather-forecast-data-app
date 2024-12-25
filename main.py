import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:", placeholder="Enter a city", key="place")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="Select the number of forecast days", key="days")
box = st.selectbox(label="Select data to view", options=("Temperature", "Sky"), key="box")
st.subheader(f"{box} for the next {days} days in {place.capitalize()}")

def get_data(days):
    temperature = 3
    return days, temperature

d, t = get_data(days)

figure = px.line(d, t, labels={"x": "Date", "y": "Temperature (C)"})
chart = st.plotly_chart(figure)