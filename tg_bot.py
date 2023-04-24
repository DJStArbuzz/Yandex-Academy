import logging
import datetime
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
import sqlite3


with open('info_tg.txt') as f:
    sp = f.readlines()
    sp = [i[:-1] for i in sp]
BOT_TOKEN = sp[0]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

weekdays = ['понедельник',
            'вторник',
            'среда',
            'четверг',
            'пятница',
            'суббота',
            'воскресенье']


exams = ['КР',
         'ПР',
         'ЕГЭ',
         'ОГЭ',
         'ВПР',
         'ПА',
         'Олимпиада',
         'Соревнования']


objects = ['Математика',
           'Русский язык',
           'Химия',
           'Физкультура',
           'Информатика']


async def start(update, context):
    """Отправляет сообщение, когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        f"Привет {user.mention_html()}! Я специальный бот Яндекс Академии. Напишите мне что-нибудь, "
        f"и я отвечу!",
    )


async def help_command(update, context):
    """Отправляет сообщение, когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def time(update, context):
    result = str(datetime.datetime.now()).split()
    result_final = f"Время: {result[1][:result[1].find('.')]}"
    """Отправляет сообщение с текущим временем, когда получена команда /time"""
    await update.message.reply_text(result_final)


async def date(update, context):
    result = str(datetime.datetime.now()).split()
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    result_final = f'Сегодняшнее число: {result[0]}. День недели: {weekdays[weekday]}'
    """Отправляет сообщение с текущей датой, когда получена команда /date"""
    await update.message.reply_text(result_final)


async def echo(update, context):
    await update.message.reply_text('Я получил сообщение: ' + update.message.text)


async def akk(update, context):
    with open('akk_info.txt') as f:
        sp = f.readlines()
    res = f'Ваше ФИО: {sp[0]}' \
          f'Ваш телефон {sp[1]}' \
          f'Ваша дата рождения {sp[2]}' \
          f'Рейтинг {sp[3]}' \
          f'Нынешний балл {sp[4]}'
    await update.message.reply_text(res)


async def schedule(update, context):
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    name = f'schedule/{weekday}.txt'
    with open(name) as f:
        sp = f.readlines()
    res = ''
    for i in sp:
        res += i
    await update.message.reply_text(res)


async def homework(update, context):
    weekday = datetime.datetime.weekday(datetime.datetime.now())
    name = f'schedule/homework_{weekday}.txt'
    with open(name) as f:
        sp = f.readlines()
    res = ''
    for i in sp:
        res += i
    await update.message.reply_text(res)


async def ex(update, context):
    with open('schedule/exams.txt', encoding='utf8') as f:
        sp = f.readlines()
    for i in range(len(exams)):
        await update.message.reply_text(f'{exams[i]} - {sp[i]}')


async def mark(update, context):
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
        await update.message.reply_text(f'{objects[i]} - {sp_ob[i] / n}')


async def projects(update, context):
    name = f'schedule/projects.txt'
    with open(name, encoding='utf8') as f:
        sp = f.readlines()
    res = ''
    for i in sp:
        res += i
    await update.message.reply_text(res)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("date", date))
    application.add_handler(CommandHandler("akk", akk))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("hw", homework))
    application.add_handler(CommandHandler("projects", projects))
    application.add_handler(CommandHandler("marks", mark))
    application.add_handler(CommandHandler("ex", ex))
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
