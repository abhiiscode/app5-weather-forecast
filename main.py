import streamlit as st
import plotly.express as px
# .express is the module present in plotly


st.title("Weather forcast for the Next Days")
place = st. text_input("Place: ")
days = st.slider("forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select date to view",
                     ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-07-01", "2024-07-02", "2024-07-03",]
    temperatures = [10, 11, 15]
    # list comprehestion
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

date, temp = get_data(days)

figure = px.line(x=date, y=temp,
                 labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(figure)
