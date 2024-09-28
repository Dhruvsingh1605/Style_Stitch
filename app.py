import streamlit as st
import pickle
import requests
import pandas as pd

# Load your trained model
model = pickle.load(open('clothing_recommendation_model.pkl', 'rb'))

# Load your fashion dataset
fashion_df = pd.read_csv('fashion_data.csv')

# Function to fetch weather data using OpenWeather API
def fetch_weather_data(city_name):
    api_key = "a95ea5e3647542abd4530782e99d43d1"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    return response.json()

# Function to determine season based on temperature
def determine_season(temp):
    if temp >= 30:
        return 'Summer'
    elif temp <= 15:
        return 'Winter'
    else:
        return 'Spring/Autumn'

# Clothing recommendation function
def recommend_clothing(temp, season, weather_type):
    if temp >= 30:
        # Recommend cotton clothing
        cotton_clothes = fashion_df[fashion_df['name'].str.contains("Cotton")]
        return cotton_clothes.sample(n=5).to_dict(orient='records')
    elif temp <= 15:
        # Recommend woolen clothing
        woolen_clothes = fashion_df[fashion_df['name'].str.contains("Woolen")]
        return woolen_clothes.sample(n=5).to_dict(orient='records')
    elif "rain" in weather_type.lower():
        # Recommend clothes for rainy weather
        rainy_clothes = fashion_df[fashion_df['name'].str.contains("Raincoat")]
        return rainy_clothes.sample(n=5).to_dict(orient='records')
    else:
        # Default to regular clothes
        regular_clothes = fashion_df.sample(n=5).to_dict(orient='records')
        return regular_clothes

# Streamlit App
st.title("Clothing Recommendation System")

city = st.text_input("Enter city name:")

if city:
    weather_data = fetch_weather_data(city)
    if weather_data.get("main"):
        temp = weather_data['main']['temp']
        weather_type = weather_data['weather'][0]['description']
        season = determine_season(temp)
        
        st.write(f"Current temperature: {temp}°C")
        st.write(f"Weather Type: {weather_type}")
        st.write(f"Season: {season}")

        # Get clothing recommendations
        recommendations = recommend_clothing(temp, season, weather_type)

        st.subheader("Recommended Clothing:")
        for recommendation in recommendations:
            st.write(f"Clothing: {recommendation['name']}")
            st.image(recommendation['img'], width=150)
            st.write(f"[Product Link]({recommendation['purl']})")
    else:
        st.write("City not found or API limit exceeded.")
