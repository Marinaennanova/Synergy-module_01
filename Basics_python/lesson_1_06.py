# Квадратный стиль
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new = []
# for i in list:
#     if i % 2 == 0:
#        a = i**2
#        new.append(a)
# print(new)

# Списковый синхрон
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 9, 8, 7, 6]
# min_count = 4
# new_1 = []
# new_2 = []
# res = []
#
# for i in range(len(list1)):
#     if len(list1) > min_count:
#        res.append(list1[i] * list2[i])
#
#     else:
#        new_1 = list1[0::]
#        new_2 = list2[0::]
# print(f"Срез списка № 1: {new_1} и срез списка № 2:{new_2}")
# print(res)

# Буквы любят цифры
# stroka = "a, 2, b, 4, c, 5, d, 8, e, 9"
# my_list = stroka.split(", ")
# new_list =[]
# for i in range (1,len (my_list)):
#     if i % 2 == 0 :
#         new_list.append(i * i)
#
# for i in new_list:
#     if i > 2:
#        break
#
#     else :
#          print("-".join(my_list))
# print(new_list)

# Гениратор

# a = input("Введи числа :").split(",")
# new = list(map(int,a))
# my_list = []
# spisok = [i * i for i in new if i % 2 == 0 ]
# my_list.append(spisok)
# total = sum(new)
#
# res = [spisok,[total]]
# print(res)



#Сортировка
# a = input("Введи числа:").split(",")
# b = list(map(int,a))
# b.sort()
# print(b)

# Фруктам нужен порядок
# sp = ["orange","grape","strawberry","banana" ,"kiwi"]
# n = len(sp)-1
# print(sp)
# while n > 0:
#     for i in range(n):
#         if sp[i] > sp [i + 1]:
#             sp[i],sp[i + 1] = sp[i + 1],sp[i]
#             print(sp)
#     n -= 1
# print(sp)
# sp.sort(key=len,reverse=False)
# print(sp)
