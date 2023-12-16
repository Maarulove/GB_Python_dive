import random

"""
11111
Вручную создайте список с целыми числами, которые повторяются. 
Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
"""
 
def task1():
    data = [random.randint(1, 10) for i in range(50)]
    print(data)

    res_1 = list(set(data))
    print(res_1)

    res_2 = []

    for i in data:
        if i not in res_2:
            res_2.append(i)

    print(sorted(res_2))



"""
2222
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
● целое положительное число
● вещественное положительное или отрицательное число
● строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
● строку в верхнем регистре в остальных случаях
"""
def upper_case(text):
    for i in text:
        if i.isupper():
            return True
    return False

def is_float(text):
    if text.count(".")==1:
        for i in text.replace(".", ""):
            if i.isdigit():
                return True
    return False

def task2():
    my_input = input("type anything")
    if my_input.isdigit() and int(my_input) > 0:
        print("целое положительное число")
    elif is_float(my_input):
        print(12)
        if float(my_input) > 0: 
            print("вещественное положительное")
        else:
            print("вещественное отрицательное")
    elif upper_case(my_input):
        print(my_input.lower())
    
    elif not upper_case(my_input):
        print(my_input.upper())

"""
3333
Создайте вручную кортеж содержащий элементы разных типов.
 Получите из него словарь списков, где ключ - тип элемента,
   а значение - список элементов данного типа.
"""


def task3():
    data = (1221,(21312, "das"), "dasd", 123.4, "asd", "dasdas")
    dict = {}
    dicc = {}
    for i in data:
        dict[type(i)] = i
        dicc.setdefault(type(i), []).append(i)

    print(dicc)

"""
444
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
"""
def task4():
    my_list = [1,1,1,1,1, 2,2,2,2, 3, 5]
    edited = list(filter(lambda x: my_list.count(x) < 2, my_list ))
    
    for i in set(my_list):
        if my_list.count(i) >=2:
            list
            my_list.remove(i)
    print(my_list)
    print(edited)

def task4_ilya():
    my_list = [1, 2, 3, 4, 5, 3, 5, 6, 8, 2]
    # 1
    editted_list = [num for num in my_list if my_list.count(num) != 2]
    print(editted_list)
    # 2
    editted_list_v2 = list(filter(lambda x: my_list.count(x) != 2, my_list))
    print(editted_list_v2)
    # 3
    for num in set(my_list):
        if my_list.count(num) == 2:
            my_list.remove(num)
            my_list.remove(num)
    print(my_list)


"""
555
Создайте вручную список с повторяющимися целыми числами. 
Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
 Нумерация начинается с единицы.
"""
def task5():
    my_list = [1,32,4,5,6,75,7, 9]
    new = list(my_list.index(i) for i in my_list if i% 2 !=0)
    print(new)

"""
6666
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
● Строки нумеруются начиная с единицы
● Слова выводятся отсортированными согласно кодировки Unicode
● Текст выравнивается по правому краю так, чтобы у самого длинного
 слова был один пробел между ним и номером строки
"""
def task6():
    user_input = input("Type anything ")
    a = {}
    
    size = len(max(user_input.split(), key=len))
    # print(size)
    for i in user_input:
        print(f"{i[0]}: {i[1]:>{size}}")


def task6_ilya():
    data = [i for i in enumerate(sorted(input().lower().split()), 1)]

    length = len(max(data, key=lambda x: len(x[1]))[1])

    for i in data:
        print(f"{i[0]}: {' '*(length - len(i[1]))}{i[1]}")
        print(f"{i[0]}: {i[1]:>{length}}") 

task6_ilya()


gb.ru/lessons/379764#s5431