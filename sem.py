"""Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. 
Сформируйте словарь, где:
● второе и третье число являются ключами
● первое число является значением для первого ключа
● четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа"""

from asyncio import IncompleteReadError


def task_1_1():
    data_inp= input().split("/")
    res = {}
    res.update({data_inp[1]:data_inp[0]})
    res.update({data_inp[2]: tuple(data_inp[3:])})
    print(res, sep="/")


def task_1_2(numbers_str: str) -> dict:
    v1, k1, k2, *v2 = map(int, numbers_str.split('/'))
    return {k1: v1, k2: tuple(v2)}
    

"""Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, где ключ - буква,
 a значение - код буквы. Напишите преобразование в одну строку."""


def task2():
    text = "teaxt"
    res = {i: ord(i) for i in text}
    print(res)



"""Продолжаем развивать задачу 2. Возьмите словарь, который вы получили. Сохраните его итераторатор.
 Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю."""

def task_3_1():
    res = {i: ord(i) for i in input()}
    my_iter = iter(res.values())
    print(next(my_iter))
    print(next(my_iter))



"""Создайте генератор чётных чисел от нуля до 100.
 Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку."""

def task_4():
    res = [i for i in range(0, 100, 2) if i > 8 or all(i +x != 8 for x in range(-8, 8, 2) if x !=i)]
    print(res)

def task_4_2():
    res = (i for i in range(0, 100, 2) if sum(int(j) for j in str(i)) != 8)
    print(*res)
# task_4_2()


"""Напишите программу, которая выводит на экран числа от 1 до 100.
 При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», 
 а вместо чисел, кратных пяти — слово «Buzz».
   Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
*Превратите решение в генераторное выражение."""
def task_5():
    print(*("fizzbuzz" if i%15== 0 else "buzz" if i%3 == 0 else "fizz"
         if i % 5 == 0 else i  for i in range (10)))
    

#############################    wooow #############
def task_5_1():
    return((i, "fizzbuzz", "Buzz", "Fizz")[(not i %3) + 2 * (not i % 5)] for i in range(100))







"""Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
 Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - 
 отдельный пример таблицы умножения.
 Для вывода результата используйте “принт” без перехода на новую строку."""


def task6():
    # print(*(f"\n{i} * {j} = "+ str(i*j) for i in range(2, 10) for j in range(2, 10)))
    # print(*res)

    for i in range(2, 10):
        for j in range(2,10):

            print(f"{i} * {j} = "+ str(i*j), sep="\t")
            # print(END)     




def task6_ilya():
    for i in range(2, 10, 4):
        for j in range(2, 10):
            for k in range(4):
                print(f"{i + k} * {j} = {(k + i) * j}", end="\t")
            print()
        print()

def task6_viktoriya():
        print(
            *(
            ' \t'.join(f'{j} x {i} = {i*j:2}' for j in range(2, 6)) for i in range(2, 10)
            ),
            '\n\n', # Добавляем две пустые строки между частями
            *(
            '\t '.join(f'{j} x {i} = {i*j:2}' for j in range(7, 11)) for i in range(4, 10)
            ),
            sep='\n'
            )
        
def task6_stanislav():
    table_str = ""
    for i in range(2, 10, 4):
        for j in range(2, 11):
            for k in range(i, i + 4):
                if k != i + 4 - 1:
                    table_str += f'{k:>2} x {j:>2} = {k * j:>2}\t'
                else:
                    if j != 10:
                        table_str += f'{k:>2} x {j:>2} = {k * j:>2}\n'
                    else:
                        table_str += f'{k:>2} x {j:>2} = {k * j:>2}\n\n'

    print(table_str, end='')


"""Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
 Для проверки числа на простоту используйте правило:
 “число является простым, если делится нацело только на единицу и на себя”."""

def task7():
    N = int(input("any num: ") or 10)
    res = set(i for j in range(2, N) for i in range(2, N+1) if i % j == 0 and j != i)
    print(*res)
task7()
