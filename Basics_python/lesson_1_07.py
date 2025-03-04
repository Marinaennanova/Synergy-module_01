# Высокосный год

# def year_is_leap(n):
#     if n % 400 == 0 or n % 4 == 0:
#         return "LEAP"
#     return "IS NOT LEAP"
# print(year_is_leap(1880))
# print(year_is_leap(1881))
# print(year_is_leap(2024))
# print(year_is_leap(2025))
# print(year_is_leap(2028))
# print(year_is_leap(2029))
# print(year_is_leap(2012))
# print(year_is_leap(2013))

# Неравенство треугольника
# def triangule_exists(a,b,c):
#     if a + b > c:
#         return True
#     return False
# print(triangule_exists(2,3,4))
# print(triangule_exists(2,3,5))
# print(triangule_exists(2,3,6))

# Квадрат наибольшего числа

# def max_square(*a):
#
#     for i in a:
#
#        return max(a)**2
#
# print(max_square(3))
# print(max_square(3,7,0,1))

# Очень четные элементы
# d =[]
# def very_even ():
#     numlist = list(map(int, input("Введи чиста через пробел:").split()))
#     for i in range(1, len(numlist)):
#         if i % 2 == 0 :
#            d.append(i)
#     print(d,end = " ")
#
# very_even()

#Сладкий бизнес




# def profit (day,buyer,course,):
#
#
#
#     prof = buyer * 2 # выручка за день в долларах
#     convect = prof * course # выручка за день в ватиках
#     chistaya_prof = convect - (30 * buyer)  # чистая прибыль
#     print(f"Чистая прибыль за {day} в ватиках : {chistaya_prof}")
#     chistaya_prof_2 = chistaya_prof - 500
#     print(f"Чистая прибыль , если день {day} явился выходным: {chistaya_prof_2} ")
#
# day = input("Введи день недели:")
# buyer = int(input("Введи кол-во покупателей за день:"))
# course = int(input("Введи курс ватика в этот день :"))
#
#
# profit(day,buyer,course)

