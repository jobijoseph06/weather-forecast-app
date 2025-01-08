import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,max_value=5,help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    global dates, temperature
    dates = ["2025-22-05", "2025-23-05", "2025-24-05"]
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature


d, t = get_data(days)

figure = px.line(x=d ,y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)