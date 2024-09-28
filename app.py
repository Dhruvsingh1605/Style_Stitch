# import streamlit as st
# import pickle
# import requests
# import pandas as pd

# # Load your trained model
# model = pickle.load(open('clothing_recommendation_model.pkl', 'rb'))

# # Load your fashion dataset
# fashion_df = pd.read_csv('fashion_data.csv')

# # Function to fetch weather data using OpenWeather API
# def fetch_weather_data(city_name):
#     api_key = "a95ea5e3647542abd4530782e99d43d1"
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
#     response = requests.get(base_url)
#     return response.json()

# # Function to determine season based on temperature
# def determine_season(temp):
#     if temp >= 30:
#         return 'Summer'
#     elif temp <= 15:
#         return 'Winter'
#     else:
#         return 'Spring/Autumn'

# # Clothing recommendation function
# def recommend_clothing(temp, season, weather_type):
#     if temp >= 30:
#         # Recommend cotton clothing
#         cotton_clothes = fashion_df[fashion_df['name'].str.contains("Cotton")]
#         return cotton_clothes.sample(n=5).to_dict(orient='records')
#     elif temp <= 15:
#         # Recommend woolen clothing
#         woolen_clothes = fashion_df[fashion_df['name'].str.contains("Woolen")]
#         return woolen_clothes.sample(n=5).to_dict(orient='records')
#     elif "rain" in weather_type.lower():
#         # Recommend clothes for rainy weather
#         rainy_clothes = fashion_df[fashion_df['name'].str.contains("Raincoat")]
#         return rainy_clothes.sample(n=5).to_dict(orient='records')
#     else:
#         # Default to regular clothes
#         regular_clothes = fashion_df.sample(n=5).to_dict(orient='records')
#         return regular_clothes

# # Streamlit App
# st.title("Style Stitch - Clothing Recommendation System")

# city = st.text_input("Enter city name:")

# if city:
#     weather_data = fetch_weather_data(city)
#     if weather_data.get("main"):
#         temp = weather_data['main']['temp']
#         weather_type = weather_data['weather'][0]['description']
#         season = determine_season(temp)
        
#         st.write(f"Current temperature: {temp}°C")
#         st.write(f"Weather Type: {weather_type}")
#         st.write(f"Season: {season}")

#         # Get clothing recommendations
#         recommendations = recommend_clothing(temp, season, weather_type)

#         st.subheader("Recommended Clothing:")
#         for recommendation in recommendations:
#             st.write(f"Clothing: {recommendation['name']}")
#             st.image(recommendation['img'], width=150)
#             st.write(f"[Product Link]({recommendation['purl']})")
#     else:
#         st.write("City not found or API limit exceeded.")


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
        cotton_clothes = fashion_df[fashion_df['name'].str.contains("Cotton", case=False, na=False)]
        return cotton_clothes.sample(n=5).to_dict(orient='records')
    elif temp <= 15:
        # Recommend woolen clothing
        woolen_clothes = fashion_df[fashion_df['name'].str.contains("Woolen", case=False, na=False)]
        return woolen_clothes.sample(n=5).to_dict(orient='records')
    elif "rain" in weather_type.lower():
        # Recommend clothes for rainy weather
        rainy_clothes = fashion_df[fashion_df['name'].str.contains("Raincoat", case=False, na=False)]
        return rainy_clothes.sample(n=5).to_dict(orient='records')
    else:
        # Default to regular clothes
        regular_clothes = fashion_df.sample(n=5).to_dict(orient='records')
        return regular_clothes

# Function to check if a URL is valid
def is_valid_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False

# Streamlit App
st.set_page_config(page_title="Style Stitch", page_icon="👗", layout="wide")

# Custom CSS for styling the app
st.markdown("""
    <style>
        body {
            background-color: #e9f7ef; /* Light Green */
        }
        .main-title {
            font-size: 4em;
            color: #F57C00; /* Orange */
            text-align: center;
            font-family: 'Trebuchet MS', sans-serif;
            margin: 20px 0;
        }
        .input-container {
            text-align: center;
            margin: 20px 0;
        }
        .recommendation-card {
            background-color: #FAFAFA;
            padding: 15px;
            border-radius: 15px;
            margin: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .recommendation-title {
            font-size: 1.25em;
            color: #00796B; /* Teal */
            margin: 10px 0;
        }
        .buy-button {
            background-color: #3498db; /* Blue */
            color: white;  /* Button text in white */
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: background-color 0.3s;
            font-size: 1em;  /* Adjusted font size for better visibility */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3); /* Added shadow for better contrast */
        }
        .buy-button:hover {
            background-color: #d4ebf2; /* Darker Blue */
        }
        .image-container img {
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>Style Stitch</h1>", unsafe_allow_html=True)
st.subheader("Find your perfect outfit based on the weather in your city!")

# Input field for city name
with st.container():
    city = st.text_input("Enter city name:", placeholder="e.g., New York, Paris", key="city_input")

if city:
    weather_data = fetch_weather_data(city)
    if weather_data.get("main"):
        temp = weather_data['main']['temp']
        weather_type = weather_data['weather'][0]['description']
        season = determine_season(temp)

        st.write(f"### Current Temperature: {temp}°C")
        st.write(f"#### Weather Type: {weather_type}")
        st.write(f"#### Season: {season}")

        # Get clothing recommendations
        recommendations = recommend_clothing(temp, season, weather_type)

        st.subheader("Recommended Clothing:")
        cols = st.columns(5)  # Display in 5 columns
        for idx, recommendation in enumerate(recommendations):
            with cols[idx]:
                st.markdown("<div class='recommendation-card'>", unsafe_allow_html=True)
                st.markdown(f"<h4 class='recommendation-title'>{recommendation['name']}</h4>", unsafe_allow_html=True)

                # Check if the image URL is valid
                if is_valid_url(recommendation['img']):
                    st.image(recommendation['img'], width=150, use_column_width=True)
                else:
                    # Show a placeholder image if the URL is not valid
                    st.image('https://via.placeholder.com/150', width=150, use_column_width=True, caption="Image Not Available")

                st.markdown(f"<a href='{recommendation['purl']}' class='buy-button'>Buy Now</a>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("City not found or API limit exceeded.")


