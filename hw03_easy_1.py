#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"

# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def user(name, age, city):
    final = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
    return result
name = input('Введите ваше имя: ')
age = input('Ваш возраст: ')
city = input('Город: ')

final = user(name, age, city)
print(final)