#!/usr/bin/env python3
# -- coding: utf-8 --
from random import randint
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

while True:
    num = input("В ведите объем списка :  ")
    if num.isdigit():
        break
    else:
        pass

lists = []
i = 0
while int(num) > i:
    lists.append(randint(-100, 100))
    i += 1

print(lists)