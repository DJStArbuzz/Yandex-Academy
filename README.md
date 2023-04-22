<h1 align="center">Проект Flask «Яндекс Академия»</h1>

## 1. Задачи проекта

Создать электронный дневник - сеть для обучающихся образовательного учереждения.
Написать ТГ- и ВК-ботов для дневника.

Приложение должно иметь следующие функции:

* просмотр всех пользователей (если вы Администратор)
* просмотр своих оценок (если вы ученик)
* редактирование новостей
* выход к ВК- ТГ-ботам и их использование.

## 2. Установка и запуск приложения

Приложение протестировано для Python версии 3.9.
Для установки зависимостей приложения создайте новое виртуальное окружение Python 3, активируйте его и выполните команду

```
pip install -r requirements.txt
```

После этого приложение можно будет запустить командой
```
python3 main.py
```
Или, при работе с *nix, командой
```
./main.py
```

## 3. Работа с приложением

Основная работа с приложением производится через web-приложение.
Через этот сайт можно получить доступ к спец. ботам в Telegram и ВКонтакте.
Пользователь может запросить список домашнего задания, расписание, оценки, расписание
будущих работ (КР, ПР, ВПР и т.д.).
На сайте у пользователя есть возможность просмотреть страницы (Главная, История, Группа ВКонтакта, Канал Телеграмма).
На сайте можно авторизоваться.
Если пользователь - учитель, то открывается доп. вкладка с электронным журналом.

p.s Если вы работаете в совместном проекте, то не работайте один. Валите с проекта, если вы выполняется все за всех. Иначе будете как я за пару дней до защиты писать всю кривую основу.


