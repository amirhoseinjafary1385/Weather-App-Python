from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '6a3603e80f1fd9ce46576af6efff1ef7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == '404':
        return render_template('weather.html', error='City not found')
    else:
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
        return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
