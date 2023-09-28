# ''' Введение в ООП '''

# ''' 
# ООП -> парадигма программирования, в которой все 
# основывается на двух понятиях: Класс и обьект
# '''

# # Парадигма -> набор правил, идей, понятий которые определяют стиль написания кода

# '''
# Класс -> чертеж описание того, какими ссвойствами и поведение будет обладать обьект 
# '''
 
# '''
# Свойства -> обычные переменные
# Поведение -> обычные функции (их называют методами)
# '''

# '''
# Обьект = Экзепляр класса = Инстанция -> это экземпляр класса с собственным состоянием этих свойств
# Каждый обьект является экземпляром определенного класса
# '''

# '''Синтаксис'''

# '''
# class <Название>: -> Обьявили класс
#     string = '' -> Создали переменную класса 
#     (атрибут класса)

#     def some_methods(self): -> создали метод
#     (функция, которая определенна внутри класса) self -> ссылка на обьект
#         pass 
# '''
# # a = 'string'
# # str.upper(a)
# # a.upper()

# class Person:
#     legs = 2
#     arms = 2
    
#     def __init__(self, name, age):
#         """
#         отвечает за инициаоищацию обьекта вызывается когда мы создаем обект
#         self -> ссылка на созданный обьект здесь определяются атрибуты обьекта
#         self.name = name  создается новый атрибут у обьекта
#         """
#         self.name = name
#         self.age = age

# print(dir(Person))
# sam = Person('Sam', 24)
# print(dir(sam))




# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#             return f"Автор этой песни {self.author}"
#     def show_author(self):
#             return f"Название этой песни {self.title}"
#     def show_year(self):
#             return f"Эта песня вышла в {self.year} году"

# song = Song("Happy", "Pharrell Williams", 2013)

# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# import random

# class snaiper:
#     def __init__(self,person,hp):
#         self.person = person
#         self.hp = hp
# snaiper1 = snaiper('first snaiper',100)
# snaiper2 = snaiper('second snaiper',100)
# while snaiper1.hp != 0 and snaiper2.hp != 0:
#     random_number = random.randint(1,2)
#     if random_number == 1:
#         print(f"стреляет {snaiper1.person}!!!")
#         snaiper2.hp -=20
#     if random_number == 2:
#         print(f"стреляет {snaiper2.person}")
#         snaiper1.hp -=20
# if snaiper1.hp != 0:
#     print(f'Победил: {snaiper1.person}, осталось здоровья: {snaiper1.hp}')
# if snaiper2.hp != 0:
#     print(f'Победил: {snaiper2.person}, осталось здоровья: {snaiper2.hp}')
    
# class Hogwarts:
#     def __init__(self,courage, intelligence , justice , ambition) :
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#     def maximum(self):
     
#         attributes = {
#         'courage': self.courage,
#         'intelligence': self.intelligence,
#         'justice': self.justice,
#         'ambition': self.ambition
#         }
#         max_value = max(attributes.values())
#         result = [k for k,v in attributes.items() if v == max_value]
#         if 'courage' in result:
#             print(f'Преобладает courage -> Gryffindor')
#         elif 'intelligence' in result:
#             print(f'Преобладает intelligence -> Ravenclaw')
#         elif 'justice' in result:
#             print(f'Преобладает justice -> Hufflepuff')
#         elif 'ambition' in result:
#             print(f'Преобладает ambition -> Slytherin')

# person1 = Hogwarts(int(input('Введите значение Храбрости от 1 до 100:')),int((input('Введите значение Интелекта от 1 до 100: '))),int(input('Введите значение Cправедливости от 1 до 100:')),int(input('Введите значение Амбиции от 1 до 100:')))  
# # person1.courage=int(input('Введите значение Храбрости от 1 до 100: '))
# # person1.intelligence = int(input('Введите значение Храбрости от 1 до 100: '))
# # person1.justice = int(input('Введите значение Храбрости от 1 до 100: '))
# # person1.ambition = int(input('Введите значение Храбрости от 1 до 100: '))

# person1.maximum()
# class Phone:
#     name = ''
#     last_name = ''
#     phone = 532532
#     def get_info(self):
#         string = f'Контакт:{self.name} {self.last_name}, телефон: {self.phone}' 
#         return string
# phone = Phone()
# phone.name = 'John'
# phone.last_name = 'Snow'
# phone.phone = '+996707707707'

# info = phone.get_info()
# print(info)

# class Math:
#     def __init__(self,number):
#         self.number = number
#     def get_factorial(self):
#         sum1 = 1
#         for i in range(1,self.number+1):
#             sum1 *= i
#         return sum1
#     def get_sum(self):
#         returned = [int(i) for i in str(self.number)]
#         sum1 = 0
#         for i in range(len(returned)):
#             sum1 = sum1 + returned[i]
#         return sum1
#     def get_mul_table(self):
#         table = ''
#         for i in range(1, 11):
#             table += f'{self.number} x {i} = {self.number * i}\n'
#         return table
# math = Math(11)
# print(math.get_factorial(), math.get_sum(),math.get_mul_table())

# class MyString(str):
#     def __init__(self, string):
#         self.string = string
    
#     def append(self,string1):
#         self.string += string1
    
#     def pop(self):
#         last_char = self.string[-1]
#         self.string = self.string[:-1]
#         return last_char
    
#     def __str__(self):
#         return self.string
        
# example = MyString('String') 
# example.append('hello') 
# print(example.pop()) 
# print(example)

# class Animal():
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
# class Lion(Animal):
#     def speak(self):
#         print('arrr')
# class Elephant(Animal):
#     def speak(self):
#         print("whoo")
# class Giraffe(Animal):
#     def speak(self):
#         print("zhzhzh")


# lion = Lion("Simba", "Lion")


# elephant = Elephant("Dumbo", "Elephant")

# giraffe = Giraffe("Melman", "Giraffe")

# lion.speak()   
# elephant.speak()
# giraffe.speak()  
# import random
# class Language:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
#     countStudent = 50

# class Python(Language):
#     countStudentPython = 30
#     def coding(self):
#         print("I am Python student. I am coding now.")
# class JavaScript(Language):
#     countStudentJS = 20
#     def coding(self):
#         print("I am JavaScript student. I am coding now.")

# python = Python('Adilet', 'Isaev')

# js = JavaScript("Ayana", "Emileva")

# rand = random.randint(0,1)
# print(rand)
# print(f"Отгадайте студента: 0 - Python или 1 - JS ")

# answer = int(input())

# if answer == rand and answer == 0:
#     python.coding()
#     print("good job")
# elif answer == rand and answer == 1:
#     js.coding()
#     print("good job")
# else:
#     print("No bueno :(")


# class MyList(list):
#     def insert(self,index,value):
#         return super().insert(value,index)
    
    
# my_list = MyList([1, 2, 3, 4])
# my_list.insert(2, 5)

# print(my_list)
# import datetime
# class Smartphone():
#     def __init__(self,name,color,memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0
    
#     def __str__(self):
#         return f"Название телефона :{self.name}\nПамять телефона: {self.memory}\n"
    
#     def charge(self,plus):
#         self.battery +=plus
#         print(f"Заряд увеличен на {plus}, заряд - {self.battery}")
    
# class Iphone(Smartphone):
#     def __init__(self, name, color, memory,ios):
#         super().__init__(name, color, memory)
#         self.ios = ios
#     def send_message(self):
#         return f"Сообщение выслано с телефона {self.name}, {self.color}, {self.memory},{self.battery}"

        
# class Samsung(Smartphone):
#     def __init__(self, name, color, memory,android):
#         super().__init__(name, color, memory)
#         self.android = android
    
#     def show_time(self):
# #         return datetime.datetime.now()    
# iphone = Iphone("iPhone 12", "Черный", "128 ГБ", "iOS 15")

# samsung = Samsung("Samsung Galaxy S21", "Синий", "256 ГБ", "Android 12")

# print(iphone)
# print(samsung)

# iphone.charge(50)

# print(f"Заряд iPhone: {iphone.battery}")

# message = iphone.send_message()
# print(message)

# current_time = samsung.show_time()
# print(f"Текущее время на Samsung: {current_time}")






        



# class Phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class SmartPhone(Phone):
#     def make_call(self):
#         return self.brand, self.model
    
# class BasicPhone(Phone):
#     def make_call(self):
#         return self.brand, self.model

# smartphone = SmartPhone("Apple", "iPhone 15")
# basicphone = BasicPhone("Nokia", "3310")

# smartphone= smartphone.make_call()
# basicphone = basicphone.make_call()

# print("Smartphone call:", smartphone)  # Вывод: ("Apple", "iPhone 12")
# print("BasicPhone call:", basicphone)  # Вывод: ("Nokia", "3310")

    

# class MyDict(dict):
#     def get(self,key):
# #         if super.get(key
# #         return super.get(key)
# # my_dict = {"name": "Alice", "age": 30}

# # name = my_dict.get("name")
# # print(name) 

# # country = my_dict.get("country")
# # print(country)  


# # class W:
# #     def write(self):
# #         with open(self.name,'w') as file:
# #             file.write('f')
    
# # class R:
# #     def read(self):
# #         with open(self.name,'r') as file:
# #             f = file.read()
# #             print(len(f))
# # class A:
# #     def append(self):
# #         with open(self.name,'a') as file:
# #             data = 'this append method'
# #             file.write(data)
# # class RWA(R,W,A):
# #     def __init__(self,name):
# #         self.name = name
        
# # file = RWA('f.txt') 
# # file.write()
# # file.append()
# # file.read()





# class ColorMixin():
#     def __init__(self,color) -> None:
#          self.color  = color

#     def set_color(self,new_color):
#         self.color = new_color
        
#     def get_color(self):
#         return self.color
    
# class Fruit(ColorMixin):
#     pass
# class Car(ColorMixin):
#     pass

# fruit = Fruit('red')

# car = Car('blue')
# print(fruit.get_color())
# print(car.get_color())
# fruit.set_color('blue')
# car.set_color("red")


# print(fruit.get_color())
# print(car.get_color())