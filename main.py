# import streamlit as st
# import plotly.express as px
# from backend import get_data
# # .express is the module present in plotly
#
# # Add title, text input, slider, selextbox, subheader
# st.title("Weather forcast for the Next 5 Days")
# place = st. text_input("Place: ")
# days = st.slider("forecast Days", min_value=1, max_value=5,
#                  help="Select the number of forecasted days")
# option = st.selectbox("Select date to view",
#                      ("Temperature", "Sky"))
# st.subheader(f"{option} for the next {days} days in {place}")
#
# if place:
#     try:
#     # Get the temperature/Sky date
#         filtered_data = get_data(place, days)
#
#         if option == "Temperature":
#             # Create a temperature plot
#             temperatures = [dict["main"]['temp'] / 10    for dict in filtered_data]
#             dates = [dict["dt_txt"] for dict in filtered_data]
#             figure = px.line(x=dates, y=temperatures,
#                              labels={"x": "Date", "y": "Temperature (c)"})
#             st.plotly_chart(figure)
#
#         if option == "Sky":
#             # Create a temperature plot
#             sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
#             images = {"Clear": "images/clear.png", "Clouds": "images/clouds.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
#             # Transleting the data
#             print(sky_condition)
#             image_path = [images[condition] for condition in sky_condition]
#             st.image(image_path, width=115)
#     except KeyError:
#         st.info("You Entered Wrong City Name,"
#                 " Name start's with capital later")
#
#
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
                             labels={"x": "Date", "y": "Temperature (°C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [d["weather"][0]["main"] for d in filtered_data]
            images = {"Clear": "☀️", "Clouds": "☁️", "Rain": "🌧️", "Snow": "❄️"}
            image_path = [images[condition] for condition in sky_condition]
            st.write(" ".join(image_path))

    except KeyError:
        st.info("You entered a wrong city name. Name starts with a capital letter.")