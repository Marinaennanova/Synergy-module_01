""" Генератор квадратов"""

def gen (n):
    i = 0
    while i !=n:
        yield i*i
        i += 1

g = gen(5)
for i in g:
    print (i)

""" Генератор квадратов-2"""
from datetime import date,timedelta
def year (start:date,end:date,step:timedelta):

    while start < end:
        yield start
        start+=step

print(*year(start=date(2023,1,1),end = date(2023,1,10),step=timedelta(days=1)),sep="\n")


