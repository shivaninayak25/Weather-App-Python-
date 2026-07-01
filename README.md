# 🌤️ Weather App (Python)

A simple command-line Weather App built using Python. It fetches real-time weather information for any city using the OpenWeather API.

## Features

- 🌍 Search weather by city name
- 🌡️ Current temperature
- 🔥 Feels like temperature
- 📉 Minimum temperature
- 📈 Maximum temperature
- 💧 Humidity
- 🌬️ Wind speed
- 👀 Visibility (in km)
- ☁️ Weather description
- 🌎 Country code
- ❌ Displays an error message if the city is not found

## Technologies Used

- Python 3
- Requests library
- OpenWeather API

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shivaninayak25/Weather-App-Python.git
   ```

2. Open the project folder:
   ```bash
   cd Weather-App-Python
   ```

3. Install the required library:
   ```bash
   pip install requests
   ```

4. Get a free API key from OpenWeather:
   https://openweathermap.org/api

5. Replace:
   ```python
   api_key = "YOUR_API_KEY"
   ```
   with your own API key.

6. Run the program:
   ```bash
   python weather.py
   ```

## Example Output

```
Enter city name: Bangalore

City: Bangalore
Temperature: 27.4 °C
Minimum Temperature: 26.1 °C
Maximum Temperature: 29.3 °C
Humidity: 72 %
Weather: scattered clouds
Wind Speed: 3.8 m/s
Feels Like: 29.0 °C
Visibility: 10.0 km
Country: IN
```


