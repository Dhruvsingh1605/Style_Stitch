from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    city = request.form['city']
    weather_data = fetch_weather_data(city)
    temp = weather_data['main']['temp']
    weather_type = weather_data['weather'][0]['description']
    season = determine_season(temp)
    
    recommendations = recommend_clothing(temp, season, weather_type)
    return render_template('results.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
