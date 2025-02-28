# Автомат с газировкой

n = int(input("Сколько хочешь газировки,введи число в милилитрах :"))
for i in range(0,1000,n):
    if i > 0 :

        print("ok")
else:
    print("Error : lack of water")

# Счетчик бракованных батончиков
choice = 0
choice_bad = 0

while choice <= 10:

   bat = int(input("Введи массу батончика  :"))

   choice += 1

   if bat in range(40,51):
       print("Ok")

   else:
       print("BAD")
       choice_bad += 1
print("Всего батончиков попало на конвеер",choice)
print("Кол-во  плохих батончиков",choice_bad)
res = round((choice_bad/choice),2)
print("Процент брака ",res)

#  Star stair

n = int(input("Введи количество рядов :"))
for i in range(0,n) :
    for j in range(0,i+1):
       print(" * ",end="")
    print()

# Счетчик счастливых чисел Тома

a = int(input("Введи первое положительное число :"))
b = int(input("Введи второе положительное число :"))

if a > b:

    print("Ошибка, певое число не может быть больше второго")


count = 0
for i in range(a,b):
    if  i  % 77 == 0:
      count +=1

print (f"Всего счастливых чилел в диапазоне от {a} до  {b} : {count}")

# Квадраты в диапазоне
import math
my_list=[]
a = int(input("Введи первое положительное число :"))
b = int(input("Введи второе положительное число :"))
if a > b:
  print("Ошибка, певое число не может быть больше второго")
elif a < 0:
     a = 1
for i in range(a,b):
    res = math.sqrt(i)
    if i % res == 0:
        my_list.append(res)
for j in my_list:
    print(round(math.pow(j,2)))

