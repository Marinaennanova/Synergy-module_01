# """ Оркестр животных и их симфония методов   """
# class Animal:
#     def __init__(self,name,poroda):
#         self.name = name
#         self.poroda = poroda
#
#     def make_sound(self):
#         print(f"{self.name} породы {self.poroda}  произносит chif-chif-chif")
# class Mammal(Animal):
#     def give_birth(self):
#         print("У нас родились малыши!")
# class Bitd(Animal):
#     def can_fly(self):
#         print("Ура!Я лечу!")
#
# animal = Animal("Пингвин","Королевский")
# print(animal.name)
# print(animal.poroda)
# animal.make_sound()
# mammal = Mammal("Кит","Синий")
# print(mammal.name)
# print(mammal.poroda)
# mammal.give_birth()
# bird = Bitd("Колибри","Розовый")
# print(bird.name)
# bird.can_fly()
#
# """Библиотечная """
# class Book:
#     def __init__(self,name,aftor,year):
#         self.name = name
#         self.year = year
#         self.aftor = aftor
# class Library(Book):
#     def __init__(self,name,aftor,year):
#         super().__init__(name,aftor,year)
#
#
#
#     def nova_book(self,name:str,aftor:str,year:str):
#         spisok_name = []
#         spisok_aftor =[]
#         spisok_year = []
#
#         book_name = input("Введите название книги:")
#         book_aftor = input("Введите автора книги:")
#         book_year = input("Введите год издания книги :")
#         spisok_name.append(book_name)
#         spisok_aftor.append(book_aftor)
#         spisok_year.append(book_year)
#         spisok_1_ = spisok_name + spisok_aftor + spisok_year
#         print(spisok_1_)
#    def __del__(self):
#        print("Книга удалена")
#
# if __name__== "__main__":
#
#     lib = Library("Дети капитана Гранта","Ж.Верн",1954)
#     lib_2 = Library("Бесы","Ф.Достоевский",1959)
#     lib_3 = Library("Король артур","Т.Мэлори",1985)
#     print(lib.name)
#     print(lib.aftor)
#     print(lib.year)
#     print(lib_2.name)
#     print(lib.nova_book())
#     del lib_2
#
#
#
# """ Калькулятор """
# class Calc:
#     def __init__(self):
#         self.res = 0
#
#     def add(self,a, b):
#         self.res =  a + b
#         return self.res
#
#     def sub(self,a, b):
#         self.res =  a - b
#         return self.res
#
#     def div(self,a, b):
#         try:
#              self.res = a / b
#              return self.res
#         except ZeroDivisionError :
#             print("На ноль делить нельзя")
#             return 0
#
#     def mult(self,a, b):
#         self.res =  a * b
#         return self.res
# if __name__ == "__main__":
#     calc = Calc()
#     print(calc.div(10, 0))
#     print(calc.div(10, 2))
#     print(calc.add(8, 10))
#     print(calc.sub(12, 4))
#     print(calc.mult(8, 8))
#
# """Калькулятор 2"""
#
# class Calc_2(Calc):
#     def power(self,a, b):
#         self.res =  a ** b
#         return self.res
#
#     def root(self,a,b):
#
#         self.res =a**b
#         return self.res
#
# if __name__ == "__main__":
#     calc_2 = Calc_2()
#     print(calc_2.power(3,3))
#     print(calc_2.power(16,b=0.5))
#     print(calc_2.power(9,b=0.5))