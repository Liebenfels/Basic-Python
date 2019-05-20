#!/usr/bin/env python3
# -- coding: utf-8 --
__author__ = "Karamalkin M.V."
__version__ = "3.6.8"
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

s_list1 = ['a','b','c','d','e','f']
s_list2 = ['e','f','g','k','l','m','n']
print(list(set(s_list1) - set(s_list2)))
