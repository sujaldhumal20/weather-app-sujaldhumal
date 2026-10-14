import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('WEATHER_API_KEY')

st.set_page_config(page_title='Weather App', page_icon='🌤️')

st.markdown(
    """
    <style>
    .stApp {
        background-color: #b9def2;
        background-image:
            radial-gradient(circle at 82% 13%, rgba(255, 239, 177, .9) 0 4rem, rgba(255, 239, 177, .24) 4.1rem, transparent 12rem),
            radial-gradient(ellipse at 16% 30%, rgba(255, 255, 255, .66) 0 5rem, transparent 15rem),
            radial-gradient(ellipse at 90% 53%, rgba(255, 255, 255, .48) 0 6rem, transparent 17rem),
            linear-gradient(155deg, #75c3ec 0%, #a4d7ef 42%, #d8e8f3 100%);
        background-attachment: fixed;
    }
    [data-testid="stTextInput"] input {
        background-color: rgba(242, 250, 255, 0.92) !important;
        border: 1px solid #75c3ec !important;
        border-radius: 10px !important;
        color: #183b53 !important;
    }
    [data-testid="stTextInput"] input:focus {
        border-color: #399dd2 !important;
        box-shadow: 0 0 0 2px rgba(57, 157, 210, 0.2) !important;
    }
    [data-testid="stButton"] {
        width: fit-content !important;
    }
    [data-testid="stButton"] button {
        width: fit-content !important;
        min-width: 0 !important;
        padding: 0.45rem 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title('WeatherBolt 🌤️')

st.write('Enter the city name and click the button to fetch the weather data')
city = st.text_input('Enter the City Name')
if st.button('Get Weather 🌦️'):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    data = response.json()
    if response.status_code == 200:
        st.success(f"Weather data for {city.capitalize()} fetched successfully!")
        data = response.json()
        print(data)
        name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        st.subheader(f"Weather in {city.capitalize()}, {country}")
        #Create 4 columns for the metrics
        col1, col2= st.columns(2)
        col3, col4= st.columns(2)

        col1.metric('Temperature ', f"🌡️ {temperature}°C")
        col2.metric('Humidity ', f"🌧️ {humidity}%")
        col3.metric('Wind Speed ', f"🌬️ {wind_speed} m/s")
        col4.metric('Weather ', f"🌤️ {weather_description.capitalize()}")
    else:
        st.error(f"City '{city}' not found. Please check the spelling and try again.")