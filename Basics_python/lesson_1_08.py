""" Вычисление степени без цикла"""
def power(x, n):
    return (x ** n)
print(power(5, 3))

""" Полидром без цикла"""
def is_polidrome(my_list):
    polidrom = my_list == my_list[::-1]
    return polidrom
my_list = input("Введите числа через запятую:").split(",")
print(is_polidrome(my_list))


"""Арифметическая прогрессия"""
def progretion(a_1, a_2, n=5):
    def begin():
        return [a_1 + a_2 * i for i in range(n)]
    return begin
f = progretion(3, 5)
print(f())
f = progretion(12, -7)
print(f())
f = progretion(6, 0)
print(f())

""" Аргументирующий декоратор"""

def arg_decor(function):
    def wrapper(a, b, c):

        res = function(a, b, c)
        return res

    return wrapper


@arg_decor
def some_func(a, b, c):


    print(f"{a},{b},{c}")
    print(type(a))
    print(type(b))
    print(type(c))
some_func(3, "Помидор", 3.14)

@arg_decor
def some_func_2(*call_arg):
    print(f"{call_arg}")
    print(type(call_arg))


some_func_2(3, "Помидор", 3.14)

"""Скобочные последовательности"""
def scobka (n):
   if n == 0:
      return []
   elif n == 1:
      return ["()" * n]
   string = " ".join(["(" *n, ")"*n,"()"*n ])
   return [string]

print(scobka(0))
print(scobka(1))
print(scobka(2))
print(scobka(3))