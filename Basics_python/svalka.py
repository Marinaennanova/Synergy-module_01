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
import timeit
def swap(arr,a,b):
    temp = arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    return arr
s = """def swap_test():
     arr = [2,8,9,5]
     swap(arr,0,1)
"""
print((timeit.timeit(stmt=s,number=10)))


