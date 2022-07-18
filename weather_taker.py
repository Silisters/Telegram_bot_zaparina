import requests


def getting_weather_info():
    """
    Функция делает запрос по API на получение погоды на неделю
    :return: Возвращает словарь с информацией о погоде на неделю main_weather_information
    """
    response_API = requests.get('https://api.openweathermap.org/data/2.5/onecall?'
                            'lat=48.4811723'
                            '&lon=135.0560726'
                            '&exclude=current,minutely,alerts,hourly'
                            '&lang=ru'
                            '&units=metric'
                            '&appid=1917720edcc250944510df63ea8875ba')
    main_weather_information = response_API.text
    main_weather_information = eval(main_weather_information)
    return main_weather_information


main_weather_info = getting_weather_info()

needed_info_from_weather = []
first_week_weather = []
needed_info_from_weather_2 = []
value_list = 0
for daily_unpucking_info in main_weather_info['daily']:
    """
    Цикл распаковывает информацию о погоде на 8 словарей которые принтуются
    """
    first_week_weather.append(daily_unpucking_info)
for tmp_info_weather in first_week_weather:
    needed_info_from_weather.append(tmp_info_weather.get('temp'))
    needed_info_from_weather.append(tmp_info_weather.get('feels_like'))
    needed_info_from_weather.append(tmp_info_weather.get('weather'))
    needed_info_from_weather.append(tmp_info_weather.get('rain'))
    needed_info_from_weather_2.append(needed_info_from_weather)
    needed_info_from_weather = []
    print(needed_info_from_weather_2[value_list])
    value_list = value_list+1
    '''
    Цикл достает нужные данные по погоде и сохраняет их в список словарей needed_info_from_weather_2
    '''