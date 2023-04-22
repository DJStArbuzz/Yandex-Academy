import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
import random
import datetime
import os
import wikipedia

with open('info.txt') as f:
    information = f.readlines()
    information = [i.replace('\n', '') for i in information]
TOKEN, LOGIN, PASSWORD = information[0], information[1], information[2]

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_message(chat, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'chat_id': chat,
                                'message': text,
                                'random_id': random_id})


oper = ['СМи87ЕШНСЕП?',
        'Мои записи на стене',
        'Мои друзья',
        'Загрузи фотографии',
        'Привет, Дидж СвятоБуз',
        'Хочу знать',
        'Укажи день недели']
time = ['Время', 'Число', 'Дата', 'День']
weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


# Первая (нулевая точнее) операция ничего толкового не выполянет, но нужна на будущее


# 1 задание - Вывод последних 5 постов
def my_posts():
    count = 1
    response = vk_1.wall.get(count=5, offset=1)
    result = ''
    if response['items']:
        for i in response['items']:
            text = i['text']
            date_time = str(datetime.datetime.fromtimestamp(i['date'])).split()
            res = f'{count}) {text} \n' \
                  f'date: {date_time[0]}, time: {date_time[1]}'
            result += res + '\n'
            count += 1
    send_message(chat_id, result)


# 2 задание - Вывод списка друзей в алфавитном порядке
def my_friends():
    count = 1
    response = vk_1.friends.get(fields="bdate, city")
    result = ''
    sp = []
    if response['items']:
        for i in response['items']:
            try:
                b_date = str(i['bdate'])
            except KeyError:
                b_date = 'Нет данных'
            res = f"{i['last_name']} {i['first_name']}. Родился(ась) {b_date}"
            sp.append([i['last_name'], res])
    sp = sorted(sp)
    for i in sp:
        result += str(count) + ')' + i[1] + '\n'
        count += 1
    send_message(chat_id, result)


# 3 задание - Загрузка в альбом группы фотографий
def upload_photo():
    upload = vk_api.VkUpload(vk_session)
    name_list = os.listdir('static/img')
    for i in name_list:
        upload.photo(
            i,
            album_id=291952495,
            group_id=219504995
        )


# 4 задание - Приветствие
def hello_buzz():
    response = vk_1.account.getProfileInfo()
    print(response)
    try:
        name = response['first_name']
    except KeyError:
        name = 'Пользователь'
    if response['home_town'] != '':
        town = response['home_town']
    else:
        town = '... а не знаю где ты живешь.'
    res1 = f'Привет, {name}, как жизнь?'
    res2 = f'Ты вроде живешь в городе с названием {town}? Ну как вы там?'

    send_message(chat_id, res1)
    send_message(chat_id, res2)


# 5 задание - Вывод времени
def time_q():
    result = str(datetime.datetime.now()).split()
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    result2 = f'День: {result[0]}, время: {result[1]}, день недели: {weekdays[weekday]}'
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    if msg2 == 'Да':
                        send_message(chat_id2, result2)
                    elif msg2 == 'Нет':
                        send_message(chat_id2, 'Я вас не понял, прошу прощения')
                    break


# 6 задание - Информация из википедии
def wiki_time():
    send_message(chat_id, 'И что вы хотите узнать?')
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    if msg2 == 'Ни о чем':
                        send_message(chat_id2, 'Впустую не надо вызывать команду')
                        break
                    else:
                        sp = wikipedia.summary(msg2, sentences=2)
                        send_message(chat_id2, sp)
                        send_message(chat_id2, 'Что-нибудь еще хотите узнать?')
                        wiki_time()
                    break


# 7 задание - Выбор фото из альбома
def load_photo():
    pass


# 8 задание - Выбор фото на запрос
def choice_photo_albom():
    pass


# 9 задание - Статистика
def statistika():
    pass


# 10 задание - Что за день?
def choice_day():
    send_message(chat_id, 'Укажите число в формате YYYY-MM-DD')
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    if msg2 == 'Отбой':
                        send_message(chat_id2, 'Впустую не надо вызывать команду')
                        break
                    else:
                        sp = msg2.split('.')
                        msg2 = msg2.replace('.', '-')
                        if len(sp[0]) == 4 and len(sp[1]) == len(sp[2]) == 2 and 1 <= int(sp[1]) <= 12:
                            weekday = datetime.datetime.weekday(datetime.datetime.strptime(msg2, '%Y-%m-%d'))
                            send_message(chat_id2, weekdays[weekday].title())
                        else:
                            send_message(chat_id2, 'Неправильно указана дата')
                        choice_day()


# 11 задание - Геокодер
def geocoder():
    pass


login, password = LOGIN, PASSWORD
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
vk_1 = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text
                chat_id = event.chat_id
                if msg == oper[0]:
                    send_message(chat_id, 'Да')
                elif msg == oper[1]:
                    my_posts()
                elif msg == oper[2]:
                    my_friends()
                elif msg == oper[3]:
                    upload_photo()
                elif msg == oper[4]:
                    hello_buzz()
                elif msg == oper[5]:
                    wiki_time()
                elif msg == oper[6]:
                    choice_day()
                for i in time:
                    if i.lower() in msg or i in msg:
                        send_message(chat_id, f'{i}? Вы хотите узнать время?')
                        time_q()
                    break
