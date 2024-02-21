import json, requests

def weather_data(city):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=66a76eaa062f5621800a76c754440792"

    http_str = requests.get(url).text
    json_data = json.loads(http_str)
    final_data = {}
    final_data["temp"] = json_data["main"]["temp"]
    final_data["temp_mn"] = json_data["main"]["temp_min"]
    final_data["temp_mx"] = json_data["main"]["temp_max"]
    final_data["pres"] = json_data["main"]["pressure"]
    final_data["hum"] = json_data["main"]["humidity"]
    final_data["city_name"] = json_data["name"]
    final_data["des"] = json_data["weather"][0]["main"]
    return final_data