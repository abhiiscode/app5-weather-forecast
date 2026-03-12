import streamlit as st
import plotly.express as px
from backend import get_data

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

st.title("Weather Forecast for the Next 5 Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days, api_key=API_KEY)

        if option == "Temperature":
            temperatures = [d["main"]['temp'] / 10 for d in filtered_data]
            dates = [d["dt_txt"] for d in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [d["weather"][0]["main"] for d in filtered_data]
            icons = {"Clear": "Sunny", "Clouds": "Cloudy", "Rain": "Rainy", "Snow": "Snowy"}
            result = [icons.get(condition, condition) for condition in sky_condition]
            st.write(" | ".join(result))

    except KeyError:
        st.info("Wrong city name. Please start with capital letter.")