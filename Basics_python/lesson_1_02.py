#Задача №1   /Сортировка чисел/


a = input("Введите первое число  : ")
b = input("Введите второе  число  : ")
c = input("Введите третье  число  : ")
if a > b :
    a,b = b,a
if a > c:
    a,c = c,a
if b > c :
    b,c = c,b
print("Отсортированные числа " ,a+b+c)

# Задача №2 /Сортировка с параметром/
s = input("Введите знак > или < : ")
a = input("Введите первое число : ")
b = input("Введите второе  число : ")
if s == ">":
   if a > b :
      a,b = b,a
if s == "<":
   if a < b:
      a,b = a,b
print (a+b)

#Задача №3 /Чет-нечет/
s = int(input("Введите число :"))
if s % 2 == 0:
    print("Введенное число четное : ",s)
else :
    print("Введеное число нечетное :",s)

# Задача №4 /Треугольный вопрос/
print("Введи значения длин сторон треугольника ABC  ")
a = int(input("Длина стороны АВ = "))
b = int(input("Длина стороны ВС = "))
c = int(input("Длина стороны СА = "))

if a == b == c :
   print(f"Данный треугольник с введеными значениями {a,b,c} - равносторонний")
elif a == b or a == c or b == c :
   print(f"Данный треугольник с введеными значениями {a, b, c} - равнобедренный")
elif a == 0 or b == 0 or c == 0:
    print("Ошибка")

else :
    print(f"Данный треугольник с введеными значениями {a, b, c} - разносторонний")

#Задача №5 /Камень,ножницы ,бумага/

game_1 = input("Игрок №1 введите одно слово из трех: камень,ножницы или бумага : ")
game_2 = input("Игрок №2 введите одно слово из трех: камень,ножницы или бумага : ")
game_1.lower()
game_2.lower()
if game_1 == game_2:
    print("Ничья")
elif game_1 > game_2:
    print("Выйграл второй игрок")
elif game_1 < game_2:
    print("Выйграл первый игрок")

