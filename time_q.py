# Вывод текущего времени
def choice_time():
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
