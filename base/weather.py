import pyowm

# 你的 OpenWeatherMap API Key
owm = pyowm.OWM('your_api_key')

# 指定城市的名称或编码
city_name = "Shanghai"

# 查询当前天气
observation = owm.weather_at_place(city_name)
w = observation.get_weather()

# 获取天气信息
temperature = w.get_temperature('celsius')["temp"]
wind = w.get_wind()["speed"]
humidity = w.get_humidity()

print(f"Temperature: {temperature}°C")
print(f"Wind: {wind} m/s")
print(f"Humidity: {humidity}%")
