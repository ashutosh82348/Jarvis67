elif 'how is the weather' and 'weather' in query:
    url = 'https://api.openweathermap.org/b5fa1df8dd4a28b83eb0d1f7fc54ed30'
    res = requests.get(url)
    data = res.json()
    weather = data['weather'] [0] ['main']
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    lattitude = data['coord']['lat']
    longitude = data['coord']['lon']
    
    description = data[weather][0]['description']
    speak('Temprature : {} degree celcius'.format(temp))
    print('Wind speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(lattitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))
    print('weather is : {} '.format(weather))
    speak('Wind speed : {} '.format(weather))