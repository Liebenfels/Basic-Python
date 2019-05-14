#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

from random import randint

# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# lst2 = []
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# lst2.sort()
# print("Элементы a)", lst2)

while True:
    enum = input("В ведите объем списка :")
    if enum.isdigit():
        break
    else:
        print("Вы ввели что то не то!")
        pass

lst = []
i = 0
while int(enum) > i:
    lst.append(randint(0, 50))
    i += 1
print("Все элементы", lst)
print("Элементы a)", list(set(lst)))
lst2 = []
for y in lst:
    if lst.count(y) == 1:
        lst2.append(y)
print("Элементы б)", lst2)
