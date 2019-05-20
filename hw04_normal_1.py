#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"

# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы. email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.
import re
name = str(input('Введите ваше имя: '))
surname = str(input('Введите вашу фамилию: '))
email = str(input('Введите вашу почту: '))

# email1 = email.lower()

if name.istitle():
    print('Данные введены верно')
else:
    name1 = name.capitalize()
    print("Вы должны были ввести:", name1)
if surname.istitle():
    print('Данные введены верно')
else:
    surname1 = surname.capitalize()
    print("Вы должны были ввести:", surname1)

# pattern1 = '([a-zA-Z_0-9]+@[a-z]+\.[a-z]+)'
pattern2 = '([a-z_0-9]+@[a-z]+\.[a-z]+)'

if re.match(pattern2, email):
    print(email, "- верно указан email")

else:
    print(email, '- не верно указан email')

