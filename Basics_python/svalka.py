# Линейный поиск

# def poisk(spisok,n,key):
#     for i in range(0,n):
#         if spisok[i] == key:
#             return i
#     return "Ключ не найден"
# spisok = [2,55,678,90,45,67,34,50,21]
# key = 99
# n = len(spisok)
# print(poisk(spisok,n,key))



# Время выполнения алгоритма
# import timeit
# def swap(arr,a,b):
#     temp = arr[a]
#     arr[a]=arr[b]
#     arr[b]=temp
#     return arr
# s = """def swap_test():
#      arr = [2,8,9,5]
#      swap(arr,0,1)
# """
# print((timeit.timeit(stmt=s,number=10)))
# print()

def process_secret_code(code: str):
    try:

        allowed_operators = {'+', '-', '*', '/'}

        parts = code.split()

        if len(parts) != 3:
            raise ValueError("Некорректный формат ввода. Допустимые операторы: +, -, *, /.")

        num1, operator, num2 = parts

        if operator not in allowed_operators:
            raise ValueError("Некорректный формат ввода. Допустимые операторы: +, -, *, /.")

        num1, num2 = float(num1), float(num2)

        if operator == '+':

            return num1 + num2

        elif operator == '-':

            return num1 - num2

        elif operator == '*':

            return num1 * num2

        elif operator == '/':

            if num2 == 0:
                raise ZeroDivisionError("Деление на 0 недопустимо.")

            return num1 / num2

    except ValueError as ve:

        raise ve

    except ZeroDivisionError as zde:

        raise zde

    except Exception:

        raise TypeError("Невозможно выполнить операцию.")


print(process_secret_code("10 + 5"))  # 15.0

print(process_secret_code("20 / 2"))  # Ошибка деления на ноль