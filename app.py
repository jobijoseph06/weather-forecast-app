from os import write

import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,max_value=5,help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))



if place:
    st.subheader(f"{option} for the next {days} days")
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [i["main"]["temp"]/10 for i in filtered_data ]

            dates =[i['dt_txt'] for i in filtered_data]
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Extract the weather condition and corresponding dates
            sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
            dates = [i["dt_txt"] for i in filtered_data]

            # Map weather conditions to images
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]

            # Display images and dates in a grid with 6 images per row
            for i in range(0, len(image_paths), 6):
                cols = st.columns(6)  # Create 6 columns
                for col, image_path, date in zip(cols, image_paths[i:i + 6], dates[i:i + 6]):
                    with col:
                        st.image(image_path, width=100)
                        st.write(date)






    except KeyError:
        st.write("That place was not exist")






