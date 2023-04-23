import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll

import random
import pymorphy2
import datetime
import sqlite3
import wikipedia

with open('info.txt') as f:
    information = f.readlines()
    information = [i.replace('\n', '') for i in information]

TOKEN, LOGIN, PASSWORD = information[0], information[1], information[2]
ALBUM_ID, GROUP_ID = 291952495, 219504995
FLAG = True

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_message(chat, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'chat_id': chat,
                                'message': text,
                                'random_id': random_id})


operation = ['Время',
             'Мой аккаунт',
             'Расписание',
             'ДЗ',
             'Мои проекты',
             'Мои оценки',
             'Работы',
             'Новости',
             'Определение',
             'Формы',
             'Отметиться']

time_choice = ['Время',
               'Число',
               'Дата',
               'День']
weekdays = ['понедельник',
            'вторник',
            'среда',
            'четверг',
            'пятница',
            'суббота',
            'воскресенье']
# При вызове любого из этих слов выводится время и число
# weekdays для определения дней недели
my_akk = ['ФИО',
          'Телефон',
          'ДР',
          'Рейтинг',
          'Баллы',
          'Все']

objects = ['Математика',
           'Русский язык',
           'Химия',
           'Физкультура',
           'Информатика']

# Выводится конкретная информация о пользователе
exams = ['КР',
         'ПР',
         'ЕГЭ',
         'ОГЭ',
         'ВПР',
         'ПА',
         'Олимпиада',
         'Соревнования']

errors = ['Впустую не надо вызывать команду',
          'Я вас не понял, прошу прощения']
# При вызове "Расписание" пользователю дают выбор из будущих работ

vk_session = vk_api.VkApi(LOGIN, PASSWORD)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)


# Удалить функции потом


def akk_info():
    with open('akk_info.txt') as file_akk_info:
        sp = file_akk_info.readlines()
        sp = [i[:-1] for i in sp]
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    result = [f'Ваше ФИО: {sp[0]}',
                              f'Ваш телефон: {sp[1]}',
                              f'Ваше день рождения: {sp[2]}',
                              f'Ваше рейтинг: {sp[3]}',
                              f'Ваше кол-во баллов: {sp[4]}']
                    if msg2 == 'ФИО':
                        send_message(chat_id2, result[0])
                    elif msg2 == 'Телефон':
                        send_message(chat_id2, result[1])
                    elif msg2 == 'ДР':
                        send_message(chat_id2, result[2])
                    elif msg2 == 'Мой рейтинг':
                        send_message(chat_id2, result[3])
                    elif msg2 == 'Мои баллы':
                        send_message(chat_id2, result[4])
                    elif msg2 == 'Вся информация':
                        result_full = ''
                        for i in result:
                            result_full += i + '\n'
                        send_message(chat_id2, result_full[:-1])
                    elif msg2 == 'Ни о чем':
                        send_message(chat_id2, errors[0])
                    else:
                        send_message(chat_id2, errors[1])
                    break


def choice_time():
    result = str(datetime.datetime.now()).split()
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    result2 = f'День: {result[0]}, время: {result[1][:result[1].find(".")]}, день недели: {weekdays[weekday]}'
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    if msg2 == 'Да':
                        send_message(chat_id2, result2)
                    elif msg2 == 'Нет':
                        send_message(chat_id2, errors[0])
                    else:
                        send_message(chat_id2, errors[1])
                    break


def my_schedule():
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    name = f'schedule/{weekday}.txt'
    try:
        with open(name, encoding='utf8') as weekday_file:
            sp = weekday_file.readlines()
            sp = [i[:-1] for i in sp]
        result = ''
        for i in range(len(sp)):
            result += f'{i + 1}) {sp[i]}\n'
        result_2 = 'Не забудь сдать домашнее задание.'
        send_message(chat_id, result)
        send_message(chat_id, result_2)
    except FileNotFoundError:
        result = 'Стоп. Сегодня же воскресенье, какие могут быть уроки. Иди отдыхать, воин!'
        result_2 = 'Подготовься к завтрашнему дню!'
        send_message(chat_id, result)
        send_message(chat_id, result_2)


def my_homework():
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    name = f'schedule/homework_{weekday}.txt'
    try:
        with open(name, encoding='utf8') as weekday_file:
            sp = weekday_file.readlines()
            sp = [i[:-1] for i in sp]
        result = ''
        for i in range(len(sp)):
            result += f'{i + 1}) {sp[i]}\n'
        result_2 = 'Не забудь сдать завтра свое домашнее задание.'
        send_message(chat_id, result)
        send_message(chat_id, result_2)
    except FileNotFoundError:
        result = 'Подготовься к завтрашнему дню!'
        send_message(chat_id, result)


def my_projects():
    name = f'schedule/projects.txt'
    try:
        with open(name, encoding='utf8') as weekday_file:
            sp = weekday_file.readlines()
            sp = [i[:-1] for i in sp]
        result = ''
        for i in range(len(sp)):
            result += f'{sp[i]}\n'
        result_2 = 'Не забудь закончить свои проекты.'
        send_message(chat_id, result)
        send_message(chat_id, result_2)
    except FileNotFoundError:
        result = 'Все проекты выполнены!'
        send_message(chat_id, result)


def my_marks():
    con = sqlite3.connect("db/mark.db")
    cur = con.cursor()
    res = cur.execute("SELECT math, russian, chemistry, pe, it FROM example").fetchall()
    sum_1, sum_2, sum_3, sum_4, sum_5 = 0, 0, 0, 0, 0
    n = len(res)
    for i in res:
        sum_1 += int(i[0]) if i[0] != '-' else 1
        sum_2 += int(i[1]) if i[1] != '-' else 1
        sum_3 += int(i[2]) if i[2] != '-' else 1
        sum_4 += int(i[3]) if i[3] != '-' else 1
        sum_5 += int(i[4]) if i[4] != '-' else 1
    sp_ob = [sum_1, sum_2, sum_3, sum_4, sum_5]
    for i in range(len(objects)):
        send_message(chat_id, f'{objects[i]} - {sp_ob[i] / n}')


def wiki_time():
    global FLAG
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    if msg2 == 'Нет' and FLAG:
                        send_message(chat_id2, 'Впустую не надо вызывать команду')
                        break
                    elif msg2 == 'Нет' and not FLAG:
                        send_message(chat_id2, 'Отбой операции.')
                        FLAG = True
                        break
                    else:
                        sp = wikipedia.summary(msg2, sentences=2)
                        send_message(chat_id2, sp)
                        send_message(chat_id2, 'Что-нибудь еще хотите узнать?')
                        FLAG = False
                        wiki_time()
                    break


def morphy_time():
    for event2 in longpoll.listen():
        if event2.type == VkEventType.MESSAGE_NEW:
            if event2.to_me:
                if event2.from_chat:
                    msg2 = event2.text
                    chat_id2 = event2.chat_id
                    result = morphy_time_work(msg2)
                    for i in result:
                        send_message(chat_id2, i)
                    break


def morphy_time_work(text):
    morph = pymorphy2.MorphAnalyzer()
    slovo = morph.parse(text)[0]
    result = []
    if 'INFN' in slovo.tag.POS or 'VERB' in slovo.tag.POS:
        result.append('Прошедшее время:')
        result.append(slovo.inflect({'past', 'masc'}).word)
        result.append(slovo.inflect({'past', 'femn'}).word)
        result.append(slovo.inflect({'past', 'neut'}).word)
        result.append(slovo.inflect({'past', 'plur'}).word)
        result.append('Настоящее время:')
        result.append(slovo.inflect({'pres', '1per', 'sing'}).word)
        result.append(slovo.inflect({'pres', '1per', 'plur'}).word)
        result.append(slovo.inflect({'pres', '2per', 'sing'}).word)
        result.append(slovo.inflect({'pres', '2per', 'plur'}).word)
        result.append(slovo.inflect({'pres', '3per', 'sing'}).word)
        result.append(slovo.inflect({'pres', '3per', 'plur'}).word)
    else:
        result.append('Не глагол')
    return result


def my_work():
    with open('schedule/exams.txt', encoding='utf8') as f:
        sp = f.readlines()
    for i in range(len(exams)):
        send_message(chat_id, f'{exams[i]} - {sp[i]}')


def news():
    try:
        with open('schedule/news.txt', encoding='utf8') as file:
            sp = file.readlines()
            sp = [i[:-1] for i in sp]
        result = ''
        for i in range(len(sp)):
            result += f'{sp[i]}\n'
        send_message(chat_id, result)
    except FileNotFoundError:
        result = 'Новостей нет!'
        send_message(chat_id, result)


vk_1 = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text
                chat_id = event.chat_id
                if msg == operation[0]:
                    send_message(chat_id, f'{msg}? Вы хотите узнать время?')
                    choice_time()
                    """Время"""
                elif msg == operation[1]:
                    send_message(chat_id, 'Вы хотите что-то уточнить?')
                    akk_info()
                    """Мой аккаунт"""
                elif msg == operation[2]:
                    send_message(chat_id, 'Ваше расписание на сегодня.')
                    my_schedule()
                    """Расписание"""
                elif msg == operation[3]:
                    send_message(chat_id, 'Ваше Домашнее задание. Не забудьте его сдать.')
                    my_homework()
                    """ДЗ"""
                elif msg == operation[4]:
                    send_message(chat_id, 'Ваши проекты. Не забудьте их выполнить и сдать на проверку своему учителю.')
                    my_projects()
                    """Мои проекты"""
                elif msg == operation[5]:
                    send_message(chat_id, 'Ваши оценки в текущей четверти')
                    my_marks()
                    """Мои оценки"""
                elif msg == operation[6]:
                    send_message(chat_id, 'Ближайшие работы')
                    my_work()
                    """Работы"""
                elif msg == operation[7]:
                    send_message(chat_id, 'Новости и события на этой недле')
                    news()
                    """Новости"""
                elif msg == operation[8]:
                    send_message(chat_id, 'И что вы хотите узнать?')
                    wiki_time()
                    """Определение"""
                elif msg == operation[9]:
                    send_message(chat_id, 'Укажите слово, которое надо изменить.')
                    morphy_time()
                    """Формы"""
                elif msg == operation[10]:
                    send_message(chat_id, 'Учитель запишет вас. Молодцы, что пришли.')
                    with open('akk_info.txt', 'r') as f:
                        name = f.readline().replace('\n', '')
                    with open('schedule/flag.txt', 'w') as f:
                        f.write(f'{name} пришел')
                    """Pereclichka"""
                else:
                    send_message(chat_id, 'Запрос неправильно написан.')
