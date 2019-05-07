#!/usr/bin/env python3
# -- coding: utf-8 --
from random import randint
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
while True:
    enum = input("В ведите объем списка :")
    if enum.isdigit():
        break
    else:
        print("Вы ввели что то не то!")
        pass

lists = []
i = 0
while int(enum) > i:
    lists.append(randint(-100, 100))
    i += 1

new_list = []
for t in lists:
    if t % 2 == 0:
        new_l = t / 4
        new_list.append(new_l)
    else:
        new_l = t * 2
        new_list.append(new_l)
print(new_list)