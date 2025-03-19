"""Подсчет гласных букв"""

def count_vowels(word):
    my_glas = ("аяуюыийэео")
    gl = 0
    flag = False
    for j in word:
       if j in my_glas:
          gl += 1
       elif j.isdigit():
            flag = True
       break

    print("Гласных в слове:",gl)
    if flag:
       print("Слово должно состоять из букв")

count_vowels(input("Введите слово:"))

""" Перевод в верхний регистр"""

def process_word(word):

    flag = True
    for i in word:
        if i.isdigit():
           flag = False
        break
    if flag:
       print(word.upper())
    else:
       print("Должны быть только буквы")

process_word(input("Введите слово:"))

"""Путишествие во времени"""

from datetime import datetime

def time_travel (y):
    current_yaer = datetime.now().year


    if current_yaer  > y:
        raise ValueError ("Вы не можете путишествовать в прошлое!")
    elif y % 2 == 0 :
        raise RuntimeError ("Ой,что-то пошло не так !Машина времени сломана.")
    elif y >= 2125:
        raise UserWarning ("Машина времени предупреждает:выбранный год слишком далеко в будущем.")
    else:
        print("Путишествие во времени прошло успешно!")

time_travel(int(input("Введи год:")))

"""  Числовая головоломка"""

def solve_math_puzzle(a):


    try :
           res =  eval(a)
           print(res)

    except ValueError:
           print(" В головоломке присутствуют некорректные символы или операции")

    except TypeError:
           print("Невозможно выполнить преобразование типов")

solve_math_puzzle(input("Введи математическую цепочку:"))

""" Операция секретного кода"""
def process_secret_code(code):
    try:

             res = eval(code)
             print(res)
    except ZeroDivisionError:
            print("На ноль делить нельзя!")
    except ValueError:
            print(" В головоломке присутствуют некорректные символы или операции")

    except TypeError:
            print("Невозможно выполнить преобразование типов")

process_secret_code(input("Введи математическую цепочку:"))