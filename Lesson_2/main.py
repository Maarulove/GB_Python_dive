from sys import getsizeof


# # print(help(keywords))
# a = "ff"

# print(bin(a))

list =['hello world', 2, 3.4, [], {}, (), set()]

def task1(list):
    for i in list:
        print(i, type(i))

# task1(list=list)\

"""
2) Объедините студентов в команды по 2-5 человек в сессионных залах.
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
 Для каждого элемента в цикле выведите:
● порядковый номер начиная с единицы
● значение
● адрес в памяти
● размер в памяти
● хэш объекта
● результат проверки на целое число только если он положительный
● результат проверки на строку только если он положительный
*Добавьте в список повторяющиеся элементы и сравните на результаты.
"""


def task2():
    data = [1, "hello", 3.5, 2]
    for i, item in enumerate(data, start=1):
        print(i, item, getsizeof(item),id(item), isinstance(item, str), isinstance(item, int), hash(item))


def task3():
    data = [1, "hello", 3.5, 2]
    for i, item in enumerate(data, start=1):
    #     if int == type(item) and item > 0:
    #         temp = ", integer"
    #     elif str == type(item):
    #         temp = ", string"
    #     else :
    #         temp = ""

        print(
        f"number:{i}, value: {item}, id: {id(item)}",
        f"size: {getsizeof(item)}, hash:{hash(item)}",
        f"integer: {'yes' if isinstance (item, int) else 'no'}",
        f"string:{'yes' if isinstance(item, str) else 'no'}"
    )
        
def task3():
    DEAFULTNUMBER = "237"
    BIN, OCT = 2, 8
    number: int = int(input("Введите число ") or DEAFULTNUMBER)
    print(bin(number), oct(number))
    print(trans(number, BIN), trans(number, OCT))


def trans(num: int, n: int) -> int:
    result = []
    while num:
        result.append(num % n)
        num //= n
    return sum(result[i] * 10 ** i for i in range(len(result)))
    # result = [str(item) for item in result[::-1]]
    # return "".join(result)





"""
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
 Диаметр не превышает 1000 у.е.
   Точность вычислений должна составлять не менее 42 знаков после запятой.
"""

from math import pi, sqrt
import decimal
dec = decimal.Decimal
def task4 ():
    decimal.getcontext().prec = 20
    diameter = dec(input("input number: "))
    PI = dec(pi)
    print(" the lenght is: ", PI * diameter)
    print(" the square is: ", PI * (diameter / 2) ** 2)

# task4()


"""
Напишите программу, которая решает 
квадратные уравнения даже если дискриминант отрицательный.
 Используйте комплексные числа для извлечения квадратного корня.
    """


def task5():
    a, b, c = int(input()), int(input()), int(input())

    d = b**2 - 4*a*c

    if d > 0 and a > 0:
        print((-1 * b - sqrt(d)) / (2 * a))
        print((-1 * b + sqrt(d)) / (2 * a));
    elif d > 0 and a < 0:
        print((-1 * b + sqrt(d)) / (2 * a))
        print((-1 * b - sqrt(d)) / (2 * a));
    elif d == 0:
        print(-1 * (b / (2 * a)));
    else:
        print('Нет корней')






"""
Напишите программу банкомат.
● Начальная сумма равна нулю
● Допустимые действия: пополнить, снять, выйти
● Сумма пополнения и снятия кратны 50 у.е.
● Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
● После каждой третей операции пополнения или снятия начисляются проценты - 3%
● Нельзя снять больше, чем на счёте
● При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
● Любое действие выводит сумму денег
"""

def task66():
    def tax():  
        global money_in_atm
        if money_in_atm > 5_000_000:
            money_in_atm *= decimal.Decimal(0.9)
            print(" Налог 10% при сумме более 5_000_000 у.е.")


    def is_multiple_of_50(value):
        return value % 50 == 0


    def count_increase():
        global count_operation
        count_operation += 1
        if not count_operation % 3:
            global money_in_atm
            money_in_atm *= decimal.Decimal(1.03)
            print("Начисление 3%")


    def put_money(value):
        tax()
        global money_in_atm
        if is_multiple_of_50(value):
            money_in_atm += value
            count_increase()
            return f"Счет пополнен на {value} у.е."
        else:
            return "Можно пополнять на сумму кратную 50"


    def take_money(value):
        tax()
        TAXFORTAKEMONEY = 1.5
        global money_in_atm
        if is_multiple_of_50(value):
            if money_in_atm > value:
                comisia = decimal.Decimal(value * 0.015)
                if comisia < 30:
                    comisia = 30
                else:
                    comisia = 600
    # t = value / 100 * TAXFORTAKEMONEY
                    money_in_atm -= decimal.Decimal(value + comisia)
                    count_increase()
                    return f"Вы сняли {value} у.е. Налог на снятие {comisia:.2f}"

    # return "Вы можете снять в пределах 30..600"
            else:
                return "На Вашем счету не достаточно средств"
        else:
            return "Можно снять сумму кратную 50"


    def task6():

        while True: 
            print(f"На Вашем счету {money_in_atm:.2f} у.е.")
            print("Введите от 1 до 3")
            print("1 - Пополнить счет")
            print("2 - Снять со счета")
            print("3 - Выйти")
            choice = input()
            match choice:
                case "1":
                    print(put_money(int(input("Введите сумму на которую вы хотите пополнить счет: "))))
                case "2":
                    print(take_money(int(input("Введите сумму снятия: "))))
                case "3":
                    break
                case _:
                    print("Введено не верное значение")

    task6()

task66()