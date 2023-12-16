from random import randint
from sys import argv

def task1(num1: int, num2: int = 7, count: int= 4) -> bool:
    rand = randint(int(*num1), num2)
    print(rand)
    for _ in range(count):
        ask = int(input("guess number")) 
        if rand == ask:
            print("good")
            return 
        else:
            print("bigger" if ask < rand else "Less")
    return print("not good")

"""Создайте модуль с функцией внутри. Функция получает на вход загадку, список с
 возможными вариантами отгадок и количество попыток на угадывание. 
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны."""


def task4(riddle: str, correct_var: str, variants: str, attempts: int):
    print(f"you have{attempts =}\n{riddle = }\n{variants= }\n")
    for i in range(attempts):
        solution_attempts = input("what is your option: ").lower().strip()
        if solution_attempts == correct_var:
            print(f"total attemots used: {i+1}")
        else:
            print("try again")
    print("ups you failed")
         

"""5555          Добавьте в модуль с загадками функцию, которая хранит словарь списков. Ключ словаря -
 загадка, значение - список с отгадками.
 Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки."""


def task5(dict: dict, attempts: int):
    
    for key, value in dict.items():
        while attempts:    
            print(f"you have {attempts =}\n{key}\n")
            solution_attempts = input("what is your option: ").lower().strip()

            if solution_attempts in value.lower():
                print(f"total attemots used: 1")
                print("Great!")
                break
            else:
                attempts -=1
                print("try again")




"""6666666  
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания. 
Для хранения используйте защищённый словарь уровня модуля.

Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном 
для чтения виде. Для формирования результатов используйте генераторное выражение."""

_dictionary = {}
def taks6_1(stroka: str, attempts: int):
    _dictionary.update({stroka: attempts})
    return _dictionary

def print_tsk_6_1(dict: dict):
    for key, value in dict.items():
        print("\n", key, value, end="\n")



def task6(stroka: dict, attempts: int):
    
    for key, value in dict.items():
        while attempts:    
            print(f"you have {attempts =}\n{key}\n")
            solution_attempts = input("what is your option: ").lower().strip()

            if solution_attempts in value.lower():
                print(f"total attemots used: 1")
                print("Great!")
                pr = taks6_1(key, attempts)
                break
            else:
                attempts -=1
                print("try again")

    print_tsk_6_1(pr)



"""
7777777
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
и возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует
григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
"""
def leap(year):
    if (year % 4==0 and year % 40 != 0) or year % 400 == 0:
        return True
    return False

def task7(date):
    day, month, year = map(int, date.split("."))

    if 1 < year < 10_000 and 1 < month < 13 and 0 < day <= 31:
        if month == 2:
            print(2)  
            if leap(year):
                print(3)  
                if day <= 29:
                    print(29)
                    True
                else:
                    print(False)
            else:
                print(4)
                if day <= 28:
                    True
                    print(28)
                else:
                    print(False)

        elif month in [2, 4, 6, 9, 11] :
            if day <= 30:
                print(30)
                True

        else:
            if day <= 31:
                print(31)
                True

    else:
        return print(False)


dict = {
    "what is the tallest building in the world?":"abc, bnm, mnb",
    "Who is the richest man in the world?": "my_father, Mask, Bezos",
    "what is the best code": "my, his, her"
}

if __name__ == "__main__":  
    task6(stroka=dict,
          attempts=3)


