## Style Stitch
The Fashion Recommender System provides personalized clothing recommendations based on real-time weather data fetched from the OpenWeather API. By inputting a city, the user receives appropriate outfit suggestions based on factors such as temperature, season, and weather type. The model ensures practical and diverse fashion recommendations.

Key Features:
Weather-Based Recommendations: The system uses live weather data from the OpenWeather API to recommend clothing items suitable for the current conditions (e.g., cotton for warm weather, woolen for cold weather).
Randomized Item Selection: Five clothing items are randomly selected from a pool of appropriate items, ensuring diverse suggestions.
Streamlit Frontend: A user-friendly web interface built with Streamlit allows users to input their city and receive recommendations instantly.
Machine Learning Model: The backend uses a trained machine learning model that leverages weather, season, and clothing data to provide accurate recommendations.
Real-Time Weather Fetching: The model dynamically fetches weather details from OpenWeather API using city input.
Software and Tools Requirements:
Python 3.7 (Conda)
Streamlit
OpenWeather API
Pandas
Scikit-learn
Pickle
VSCode IDE
Heroku (for deployment)
Git CLI
Github Account
Project Workflow
1. Data Collection and Preprocessing:
A fashion dataset was used, containing information such as clothing name, fabric type, and season suitability.
The data was cleaned and pre-filtered into categories for different weather conditions and seasons.
2. Model Training:
A machine learning model (Random Forest or other suitable algorithm) was trained using the weather, season, and clothing data.
The model was saved using pickle for real-time use during predictions.
3. API Integration:
The OpenWeather API was integrated to fetch real-time weather data (temperature, weather type, etc.) based on the city provided by the user.
The weather data was fed into the machine learning model to produce clothing recommendations.
4. Frontend Development:
The user interface was built using Streamlit, allowing users to input their city.
The frontend sends the city data to the backend, fetches weather data, and provides appropriate clothing recommendations.
5. Model Deployment:
The application can be deployed to Heroku or other cloud platforms, making it accessible online.
