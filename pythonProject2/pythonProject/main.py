import redis
import json



red = redis.Redis(
    host='redis-16799.c278.us-east-1-4.ec2.cloud.redislabs.com',
    port=16799,
    password='LWuhL746W5fUaQdRQgPVyMpWHidyh4ua'
)
cont = True

while cont:
    action = input('Действие:\t')
    if action == 'Запись':
        name = input('Имя:\t')
        phone = input('Номер Телефона:\t')
        red.set(name, phone)
    elif action == 'Показать телефон':
        name = input('Имя:\t')
        phone = red.get(name)
        if phone:
            print(f' Номер {str(phone)}  принадлежит {name}')
    elif action == 'Удалить':
        name = input('Имя:\t')
        phone = red.delete(name)
        if phone:
            print(f"Номер телефона {name} удален")
        else:
            print(f"Не найдено: {name}")
    elif action == 'Выход':
        break