# Фильтр конвеера батончиков
good_bat = []
my_list = []
baton = []
while True:
   bat = int(input("Введи массу батончика  :"))
   if bat == 0:
      break
   good_bat.append(bat)
for i in good_bat:
    my_list.append(i)
for j in my_list:
   if j >= 40 and j <=50:
     baton.append(j)
print("Список хороших батончиков:",baton)

# Возврат бракованных батончиков
bats = []
my_list_2 = []
bad_baton = []
while True:
   bat = int(input("Введи массу батончика  :"))
   if bat == 0:
      break
   bats.append(bat)
for i in bats:
    my_list_2.append(i)
for j in my_list_2:
   if j > 50 :
      bad_baton.append(j)
   elif   40 > j > 0:
      bad_baton.append(j)
print(sorted(bad_baton))

# Список цифр числа
my_list = []
num = int(input("Введите целое неотрицательное число :"))
while num > 0:
    res = num % 10
    my_list.append(res)
    num = num //10
my_list.reverse()
print(my_list)

# Странный регулировщик

my_list = []
left = []
right = []
while True:
    number = int(input("Введите целое неотрицательное число(нажми -1 для выхода):"))
    if number == -1:
        break

    my_list.append(number)

for i in my_list[1:]:

    if i % 2 == 0:
       right.append(i)
    else:
       left.append(i)

print(sorted(right))
left.reverse()
print(left)

# Порядочные списки

numb = []
numbers_1 = input ("Введи числа первого списка через пробел:").split()
numbers_2 = input ("Введи числа второго  списка через пробел:").split()
numbers_1.extend(numbers_2)
new_list = list(set(numbers_1))
new_list.sort()
# for i in new_list:
#     numb.append(i)
# new = sorted(numb)
print(new_list)














