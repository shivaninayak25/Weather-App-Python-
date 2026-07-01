import requests
api_key = "YOUR_API_KEY"
city = input("Enter city name:")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()
if data ["cod"]== 200:
    print("city:",data["name"])
    print("Temperature:",data["main"]["temp"],"c")
    print("Minimum_Temperature:",data["main"]["temp_min"],"c")
    print("maximum_Temperature:",data["main"]["temp_max"],"c")
    print("Humidity:",data["main"]["humidity"],"%")
    print("weather:",data["weather"][0]["description"])
    print("Wind Speed:",data["wind"]["speed"],"m/s")
    print("feels_like",round(data["main"]["feels_like"]))
    
    print("Visibility",data["visibility"]/1000,"km")
    print("Country",data["sys"]["country"])
else:
    print("city not found!")