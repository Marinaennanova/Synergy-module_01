""" Анализ данных о космических кораблях """

import csv



with open(" spaceships.csv","w",encoding="utf-8") as f:

    file_writer = csv.writer(f, delimiter=",", lineterminator="\r")
    file_writer.writerow(["Название","Тип","Год запуска","Максимальная скорость (км/ч)","Страна производитель"])
    file_writer.writerow(["Аполлон" ,"Лунный модуль","1968","38969","США"])
    file_writer.writerow(["Союз-ТМ","Космический корабль","2002" ,"27720" ,"Россия"])
    file_writer.writerow(["Фалькон-9","Ракета-носитель","1999" ,"28000" ,"США"])
    file_writer.writerow(["Юнион-2" ,"Космический корабль","2010" ,"27700" ,"Россия"])
    file_writer.writerow(["Ариан-5" ,"Ракета-носитель","1989" ,"26500" ,"Европейский союз"])
    file_writer.writerow(["Шаттл-Дискавери" ,"Космический корабль","1986" ,"25680" ,"США"])
    file_writer.writerow(["Тяньгун-11","Космическая станция","2011" ,"28000" ,"Китай"])


with open(" spaceships.csv", "r", encoding="utf-8") as f:

    csv_reader = csv.reader(f)


    count = 0
    num_list = []
    num_list_2 = []
    skor_1 = []

    for row in csv_reader:
        skor = row[3]
        skor_1.append(skor)

        a = skor_1[1::]
        result_2 = list(map(int, a))
        for i in row:

            if i == "Космический корабль":
               count+=1
            if i.isnumeric():
               num_list.append(i)
            result = list(map(int,num_list))

    for j in result:
        if j > 2000 and j < 2020:
           num_list_2.append(j)




print("Кол-во космических кораблей :",count)
print("Кол-во кораблей запущенных после 2000г.:", len(num_list_2))
print("Корабль с максимальной скоростью :",max(result_2))


""" Анализ данных о фильмах """
import csv
import  pandas as pd
import openpyxl


with open("movies.csv ","w",encoding="utf-8") as f:

     file_writer = csv.writer(f, delimiter=",", lineterminator="\r")
     file_writer.writerow(["Название","Год выпуска","Жанр","Режиссер","Сбор"])
     file_writer.writerow(["Звёздные войны:Эпизод IX - Скайуокер.Восход","2019","Фантастика","Джей Джей Абрамс","1074 "])
     file_writer.writerow(["Аватар","2019","Фантастика","Джеймс Камерон","2788 "])
     file_writer.writerow(["Темный рыцарь","1999","Боевик","Кристофер Нолан","1040 "])
     file_writer.writerow(["История игрушек-3","2008","Анималистика","Ли Анкчир","1079 "])

data = pd.read_csv("movies.csv ")
data.to_excel("movies.xlsx",index=False)

col = pd.DataFrame(data)
column = col["Название"]
for i in column:
    print(i)
print("Всего фильмов:",len(column))
column_2 = col[["Год выпуска","Сбор"]]
res = column_2.loc[col["Год выпуска"] > 2010,["Сбор"]].sum()
print(res)
column_3 = max(col["Сбор"])
print(column_3)
print("Фильм с самым высоким сбором")
res_2 = data.iloc[[1]]
print(res_2)


""" Вывод загадочных данных"""
import json
with open("1kb.json","r") as f:
    data = json.load(f)
print(data)

for item in data:
    print(item["name"],item["address"])
    print("*"* 50)
    print(item["name"],item["phoneNumber"])

