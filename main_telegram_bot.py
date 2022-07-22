import telebot
import weather_taker as wt
import time

'''
В данном блоке кода я отправляю запрос на бота телеграмм,
'''
bot = telebot.TeleBot('5514648164:AAFNc2wSSR6ctCCdLrNUoESnAjycKPgdzfU')


@bot.message_handler(content_types='text')
def waiting_input_weather(message):
    if message.text == 'Погода':
        send = bot.send_message(message.from_user.id, "На какое число?")
        bot.register_next_step_handler(send, start_giving_weather)


'''
В функции waiting_input_weather бот получает сообщения от пользователя и проверяет не спросил ли он Погода
После чего вызывает функцию получения даты на которую нужна погода
'''


def start_giving_weather(message):
    try:
        int(message.text)
    except ValueError or AttributeError:
        waiting_value = bot.send_message(message.from_user.id, 'Пожалуйста введите число!')
        bot.register_next_step_handler(waiting_value, start_giving_weather)
    else:
        proc_user_and_return_result(message)


'''
Рекурсивная функция start_giving_weather пытается перевести сообщение в тип данных int
Если это не получается вызывает себя. Если получается то вызывает функцию по обработке числа на которое нужна погода
'''


def proc_user_and_return_result(message):  # Processing the user's request and returning the result
    time_info = time.localtime()
    time_info_structure = time.strftime('%d', time_info)
    value_difference = int(message.text) - int(time_info_structure)
    if int(message.text) == int(time_info_structure):
        returning_the_result(message, 0)
    elif value_difference == 1:
        returning_the_result(message, 1)
    elif value_difference == 2:
        returning_the_result(message, 2)
    elif value_difference == 3:
        returning_the_result(message, 3)
    elif value_difference == 4:
        returning_the_result(message, 4)
    elif value_difference == 5:
        returning_the_result(message, 5)
    elif value_difference == 6:
        returning_the_result(message, 6)
    elif value_difference == 7:
        returning_the_result(message, 7)


'''
Функция proc_user_and_return_result обрабатывает то на какое число нужна погода, 
и передает эти данные в следующую функцию
'''


def returning_the_result(message, day_number):
    weather_info_day = unpucking_info_for_toyday(day_number)
    bot.send_message(message.from_user.id,
                     'Температура днем/ночью, min/max ' + str(weather_info_day[0]) +
                     '/' + str(weather_info_day[1]) +
                     ' ' + str(weather_info_day[2]) +
                     '/' + str(weather_info_day[3]))
    bot.send_message(message.from_user.id,
                     'Ощущается как днем/ночью ' +
                     str(weather_info_day[4]) +
                     '/' + str(weather_info_day[5]))
    bot.send_message(message.from_user.id,
                     'Погода ' + str(weather_info_day[6]) +
                     ' ' + 'Количество осадков в мм ' +
                     str(weather_info_day[7]))


'''
Функция returning_the_result вызывает unpucking_info_for_today и получает из нее массив данных
После этого отправляет в определенном формате информацию по погоде пользователю
'''


def unpucking_info_for_toyday(day_info):
    weather_info = wt.getting_weather_info()  # Вызов функции из файла weather_taker для получения данных
    weather_info_for_user = wt.unpucking_weather_info(weather_info)
    today_info = weather_info_for_user[day_info]
    needed_info_1 = today_info[0]
    needed_info_2 = today_info[1]
    needed_info_3 = today_info[2]
    needed_info_3_1 = needed_info_3[0]
    needed_info = []
    for complecting_information in (needed_info_1['day'],
                                    needed_info_1['night'],
                                    needed_info_1['min'],
                                    needed_info_1['max'],
                                    needed_info_2['day'],
                                    needed_info_2['night'],
                                    needed_info_3_1['description'],
                                    today_info[3]):
        needed_info.append(complecting_information)
    return needed_info


'''
Функция unpucking_info_for_today обращается к скрипту по получению погоды, расспаковывает и вытаскивает необходимые
данные упаковывая их в массив.
'''

bot.polling(none_stop=True, interval=0)
