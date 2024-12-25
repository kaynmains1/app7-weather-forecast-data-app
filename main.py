import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:", placeholder="Enter a city", key="place")
days = st.slider(label="Forecast days", min_value=1, max_value=5, help="Select the number of forecast days", key="days")
box = st.selectbox(label="Select data to view", options=("Temperature", "Sky"), key="box")
st.subheader(f"{box} for the next {days} days in {place.capitalize()}")
try:
    if place:
        filtered_data = get_data(place, days)

        if box == "Temperature":
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperature = [float(temp) / 10 for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            chart = st.plotly_chart(figure)

        if box == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow":"images/snow,png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image = [images[condition] for condition in sky_condition]
            st.image(image, width= 115)
except KeyError:
    st.title("Please enter the correct name of a city")