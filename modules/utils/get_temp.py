from .api import get_data 

def get_temp(city_name="Дніпро"):
    data = get_data(city_name)
    if not data:
        return 0, [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
    
    list_weather = data.get("list")
    if not list_weather:
        return 0, [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
    
    min_temp = 100
    list_temp = []
    for weather in list_weather:
        temp = int(weather.get("main").get("temp"))
        list_temp.append(temp)
        if temp < min_temp:
            min_temp = temp
    
    min_visible_temp = (round(min_temp/5)*5) - 10
    list_height = []
    for temp in list_temp:
        height = round((temp - min_visible_temp) * 2.874)
        list_height.append(height) 

    return min_visible_temp, list_height