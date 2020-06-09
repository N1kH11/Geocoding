def geocode():
    import googlemaps as gm
    gmaps_key = gm.Client(key='your Geocoder API Key')
    geocoder_res = gmaps_key.geocode(city)
    try:
        return geocoder_res[0]['geometry']['location']['lat'], geocoder_res[0]['geometry']['location']['lng']
    except:
        print('Exception Occurred : {}'.format())
        return None, None


def fetch_data():
    from urllib.request import urlopen
    import json

    weather_api = 'your OpenWeatherMapApi Key'
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat, lng, weather_api)
    with urlopen(url) as response:
        pure_response = response.read()
    data = json.loads(pure_response)
    return data


def fetch_future():
    from urllib.request import urlopen
    import json

    weather_api = 'ebfcac32bda131ed5a160f2757938396'
    url = 'https://api.openweathermap.org/data/2.5/forecast/daily?lat={}&lon={}&appid={}&cnt={}' \
        .format(lat, lng, weather_api, days)
    with urlopen(url) as response:
        pure_response = response.read()
    data = json.loads(pure_response)
    return data


def showFuture():
    latitude = future_data['city']['coord']['lat']
    longitude = future_data['city']['coord']['lon']
    city = future_data['city']['name']
    days_data = future_data['cnt']
    day_wise_data = future_data['list']
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('CITY : {}'.format(city))
    print('Displaying data for {} day/s'.format(days_data))
    for temp in day_wise_data:
        dt = int(temp['dt'])
        sunrise = int(temp['sunrise'])
        sunset = int(temp['sunset'])
        temp_morning = temp['temp']['morn']
        temp_day = temp['temp']['day']
        temp_eve = temp['temp']['eve']
        temp_night = temp['temp']['night']
        temp_min = temp['temp']['min']
        temp_max = temp['temp']['max']
        pressure = temp['pressure']
        humidity = temp['humidity']
        # description = temp['weather']['description']
        wind_speed = temp['speed']
        wind_degree = temp['deg']
        import time
        print('=============Date : {}============='.format(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(dt))))
        print('Min. Temp : {} Fahrenheit'.format(temp_min))
        print('Max. Temp : {} Fahrenheit'.format(temp_max))
        print('Morning Temp : {} Fahrenheit'.format(temp_morning))
        print('Day Temp : {} Fahrenheit'.format(temp_day))
        print('Evening Temp : {} Fahrenheit'.format(temp_eve))
        print('Night Temp : {} Fahrenheit'.format(temp_night))
        # print('Weather Description : {}'.format(description))
        print('Windspeed : {} mps'.format(wind_speed))
        print('Wind Degree : {} mps'.format(wind_degree))
        print('Humidity : {}%'.format(humidity))
        print('Pressure : {} hPa'.format(pressure))
        print('SUNRISE : {}'.format(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(sunrise))))
        print('SUNSET : {}'.format(time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(sunset))))
        print('*Time displayed for Sunrise and Sunset is based on your PC\'s local timezone')



def displayData(data):
    temp_max = data['main']['temp_max']
    temp_min = data['main']['temp_min']
    windspeed = data['wind']['speed']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    sunrise = int(data['sys']['sunrise'])
    sunset = int(data['sys']['sunset'])
    import time
    sunset = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(sunset))
    sunrise = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(sunrise))
    print('==================================================')
    print('======CURRENT WEATHER REPORT for {}======'.format(data['name'].upper()))
    print('Min. Temp : {} Fahrenheit'.format(temp_min))
    print('Max. Temp : {} Fahrenheit'.format(temp_max))
    print('Windspeed : {} mps'.format(windspeed))
    print('Humidity : {}%'.format(humidity))
    print('Pressure : {} hPa'.format(pressure))
    print('SUNRISE : {}'.format(sunrise))
    print('SUNSET : {}'.format(sunset))
    print('Latitude : {}'.format(data['coord']['lat']))
    print('Longitude : {}'.format(data['coord']['lon']))
    print('*Time displayed for Sunrise and Sunset is based on your PC\'s local timezone')


# Main
print('======Hello , Welcome to WeatherForecast======')
print('1.Using Latitute,Longitude')
print('2.Using City Name')
choice = input('CHOICE-->')
lat = -1
lng = -1
if choice == '1':
    lat = float(input('Enter Latitude : '))
    lng = float(input('Enter Longitude : '))
elif choice == '2':
    city = input('Enter City name : ')
    lat, lng = geocode()

showData = fetch_data()
displayData(showData)

days = int(input('How many days forecast you want to see(Max : 16 Days) : '))
if days > 16:
    days = 16
future_data = fetch_future()
showFuture()