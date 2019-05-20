#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"
from random import randint
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

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
    lists.append(randint(0, 100))
    i += 1
print(lists)

new_list = []
for t in lists:
    new_l = t ** 0.5
    if new_l.is_integer():
        new_list.append(int(new_l))
    else:
        # print(new_l)
        pass

print(new_list)