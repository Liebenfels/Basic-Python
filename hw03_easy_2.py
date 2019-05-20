#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"

# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
# Мы и это на уроке проходили
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
#
# list1 = [num1, num2, num3]
# print("Вы ввели данные числа: ", list1)
# list2 = max(list1)
# print("Максимальное введеное число: ", list2)

def maximum(a, b, c):
    num_list = [a,b,c]
    m = (max(num_list))
    return m

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

final = maximum(num1, num2, num3)
print('Максимальное введеное число: ', final)
