# Список имен
my_list = input("Ведите список имен через пробел :").split()
print(sorted(my_list))


# Маркировка батончиков
good_bat = []
my_dict_1 = []
my_dict_2 = []
bad_bat = []

while True:
   bat = int(input("Введи массу батончика  :"))
   if bat == 0:
      break
   elif bat <= 50 and bat >= 40:
        good_bat.append(bat)

   elif  bat > 51 or bat < 39:
        bad_bat.append(bat)

for i in good_bat:
    a = id(i)
    my_dict_1 = dict.fromkeys(good_bat,a)

for j in bad_bat:
    b = id(j)
    my_dict_2 = dict.fromkeys(bad_bat,b)

new = {**my_dict_1,**my_dict_2}
new_dict = {v : k for k, v in new.items()}
print(new_dict)


#Список уникальных цифр числа
my_list = input("Введите цифры :")
new_list = list(set(my_list))
print(sorted(new_list))


# Самая популярная цифра
my_list = input("Введите цифры через запятую:").split(",")
num =[]
num_2 = []
for i in my_list:
    num_2.append(my_list.count(i)) # создаем список с подсчетом кол-ва вхождений элемента
    num.append(i) # создаем список из введеных элементов
j = num_2.index(max(num_2))
print(num[j])


# Два водителя

my_list_1 = input("Ведите список городов из маршрута через пробел :").split()
my_list_2 = input("Ведите список городов из маршрута через пробел :").split()

new_list = set(my_list_1) & set(my_list_2) # Амперсант служит для поиска пересечений во множестве
# и выводит одинаковые элементы


print(new_list)

