#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

list1 = ['Олег', 'Женя', 'Алена', 'Оксана']
list2 = ['130000', '70000', '500800', '300000']

res = {name: cash for name, cash in zip(list1, list2) if int(cash) < 500000}

with open('salary.txt', 'w') as salary:
    salary.writelines(('%s - %s\n' % i for i in res.items()))

with open('salary.txt', 'r') as salary:
    for line in salary.read().splitlines():
        print(line[:line.find('-')-1].capitalize(), int(int(line[line.find('-')+1:]) * 0.87))
