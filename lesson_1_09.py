"""Разглаживание вложенных списков"""
n = [1, 2, [3, 4, [5, 6]], 7, [8]]
m = []
def fllaten_list (n):


     for  item in n:
        if isinstance(item,list):
          fllaten_list(item)
        else:
           m.append(item)
fllaten_list(n)
print(m)

""" По следам четных чисел: Количество
четных чисел во вложенных списках        """
n = [1, 2, [3, 4, [5, 6]], 7, [8]]
n = [1, [2, [3, [4, [5, [6, [7, [8, [9, [0]]]]]]]]]]
m = []
def count_even_numbers(n):
    for item in n:
        if isinstance(item,list):
           count_even_numbers(item)
        elif item % 2 == 0:
             m.append(item)
count_even_numbers(n)
print(len(m))


""" Поддиагональная сумма """

def sum_matrix_second_diagonal():
    n,m = map(int,input("Введи кол-во столбцов и строк через пробел чтоб сформировать матрицу:").split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input("Введи элементы  строки матрицы :").split())))
    s = min(n,m)
    dig = 0
    for i in range(s):
        dig +=mat[i][i]
    print(dig)
    for s in mat:
        print(*s)


sum_matrix_second_diagonal()



""" Матричное умножение  """
def multiply_matrices():

    n,m = map(int,input("Введи кол-во столбцов и строк через пробел чтоб сформировать матрицу:").split())
    matrix1 = []
    for i in range(n):
        matrix1.append(list(map(int,input("Введи элементы  строки матрицы :").split())))
    x,y = map(int,input("Введи кол-во столбцов и строк через пробел чтоб сформировать матрицу:").split())
    matrix2 = []
    for j in range(x):
        matrix2.append(list(map(int,input("Введи элементы  строки матрицы :").split())))
    if matrix1 != matrix2:
        print ([])
    else :
        res = []
        for i in range(n):
            row = []
            for j in range(x[0]):
                prod = 0
                for v in range(len(n[i])):
                    prod += n[i][v]*x[v][j]
                row.append(prod)
            res.append(row)

        print(res)
multiply_matrices()