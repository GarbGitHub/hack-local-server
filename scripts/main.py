import random

print('https://repl.it/@Levashov/hack')
1
1.5
'123abc'
True, False
None

def multiply_str(s, n=3):
    """
    'abc', 3 -> 'abcabcabc'
    'a', 1 -> 'a'
    'a', 0 -> ''
    'a', -1 -> Error
    """
    if n >= 0:
        return s * n
    else:
        raise ValueError


# print(multiply_str('abc'))
# print(multiply_str('abc', 5))
# print(multiply_str('abc', n=10))
# print(multiply_str(s='abc', n=15))
print()


def good_password_generator(length=10):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += '0123456789'
    alphabet += '!@#$%^&*()_-=<>/?|'

    password = ''
    for i in range(length):
        password += random.choice(alphabet)
    return password

# print(good_password_generator(3))
# print(good_password_generator(5))
# print(good_password_generator())
# print(good_password_generator(10))
# print(good_password_generator(15))
# print(good_password_generator(20))


with open('../pop_passwords.txt') as f:
    pop_passwords = f.read()

# print(pop_passwords[:100])
pop_passwords = pop_passwords.split('\n')
i = 0
# print(pop_passwords[:10])

def bad_password_generator():
    global i
    password = pop_passwords[i]
    i += 1
    return password

print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
print(bad_password_generator())
