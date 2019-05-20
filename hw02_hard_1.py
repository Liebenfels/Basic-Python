# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print(equation, "x =", x)
lst = equation.split()
lst2 = str(lst[2])
lst[2] = lst2[:-1]
# print(lst)
y = int(lst[2]) * x + float(lst[4])
print("y =", y)