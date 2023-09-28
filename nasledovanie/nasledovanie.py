"""


Объектно-ориентированная парадигма имеет несколько принципов:

1)Данные структурируются в виде объектов, каждый из которых имеет определенный тип, то есть принадлежит к какому-либо классу.
2)Классы – результат формализации решаемой задачи, выделения главных ее аспектов.
3)Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.
4)Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.
5)При этом объекты одного типа сходным образом отвечают на одни и те же запросы.
6)Объекты могут организовываться в более сложные структуры, например, включать другие объекты или наследовать от одного или нескольких объектов.




основные принципы ооп:
наследование полиморфизм инкапсуляция


остальные принципы:
ассоциация (агрегации,композиции), Абстракция


наследование - принцип ооп, в котором мы можем унаследовать переопределить и использовать методы и атрибуты родительского 

класса в дочернем классе. создаем новый класс на основе уже существуещего
"""
# class A:
#     def func1(self,a):
#         print(self,a)

# class B(A):
#     def __str__(self):
#         return ''

# b = B()
# b.func1(2)

# class C(A):
#     def func1(self):
#         pass



# tastk1 


# class Class1:
#     def first(self):
#         pass
        
#     def second(self):
#         pass
# class Class2(Class1):
#     def third(self):
#         pass
    
#     def fourth(self):
#         pass
    
# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

# task2



# class A:
#     def method(self):
#         print('Основной функционал')
    
# class B(A):
#     def method(self):
#         super().method()
#         print("Дополнительный функционал")

# obj = B()
# obj.method()


# task3


# class MyString(str):
#     def append(self,str):
#         returned = self + str
#         return returned
    
#     def pop(self):
#         return self[:-1]
        
    
# example = MyString('String')
# example = example.append('hello')
# # example = example.pop()
# print(example) 
        
# class MyList(list): 
#      def append(self, object): 
#          print('добавил!') 
#          return super().append(object) 
# lst = MyList([1, 2, 3]) 
# print(lst.append(4)) 
# print(lst) 

# task4 


# class MyDict(dict):
#     def get(self,key):
#         return super().get(key, 'Are you kidding?')
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 

# class A(list):
#     def my_range(self,range):
#         list_ = [i for i in range(range)]
#         return list_

# a = A()
# result = a.my_range(10)
# print(result)        


# class A:
    
#     def my_range(self, start,end,step = 1):
#         list_ = [i for i in range(start,end,step)]
#         return list_

# a = A()
# result = a.my_range(-10,10,1)
# print(result)


# task 5


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name, self.age)
        
# class Student(Person):
#     def __init__(self, name, age,faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         print(self.name, self.age,self.faculty)
        
# obj_student = Student('adilet','20','oop')
# obj_student.display() 
# obj_student.display_student() 
        
            
            
# task 6

# class ContactList(list):
#     def __init__(self,list_):
#         self.list_ = list_
#     def search_by_name(self,name):
#         list__ = []
#         for i in self.list_:
#             if name in i:
#                 list__.append(i)
#         return list__
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))
                
        
        
# # task 7
# import datetime
# class SmartPhones:
#     def __init__(self, name, color, memory, battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery
#     def __str__(self):
#         return f'{self.name} {self.memory}'
    
#     def charge(self,amount):
#         self.battery = self.battery + amount
    
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios, battery=0,):
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
    
#     def send_message(self,string):
#         return f'sending {string} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory,android, battery=0):
#         super().__init__(name, color, memory, battery)
#         self.android = android
#     def show_time(self):
#         current_time = datetime.datetime.now().time()
#         return current_time 
    
    
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_message('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())
        
# class MyList(list):
#     def insert(self, ind, elem):
#         return super().insert(elem,ind)

# my_list = MyList([i for i in range(1, 11)])
# print(my_list)    

# print('число 2 вставляем на 3 элемент:')
# my_list.insert(2,3)

# print(my_list)

        

    
        
# class Converter:
#     # @staticmethod
#     def meters_to_feet(meters):
#         feet = meters * 3.281
#         return feet


# distance_in_meters = 10
# distance_in_feet = Converter.meters_to_feet(distance_in_meters)
# print(distance_in_feet)  # Вывод: 32.81

"""
    isinstance() ->  проверяет является ли обьект экземпляром класса
    issubclass() ->  проверяет является ли класс подклассом
    
    """
    
# class A:
#     pass

# class B(A):
#     pass
     
# class C(B):
#     pass

# a = A()
# b = B()
# c = C()
# print(issubclass(C,A))
# print(issubclass(B,A))
# print(isinstance(a,object))
# print(isinstance(c,A))




# class User:
#     def __init__(self,username,age,city,password):
#         self.username = username
#         self.age = age
#         self.city = city
#         self.password = password
#     def profile_info(self):
#         print(f'имя пользователя: {self.username},город проживания {self.city}, возраст: {self.age}')
        
#     def greet_user(self):
#         print(f"Добро пожаловать {self.username}")
        
# class Admin(User):
#     def __init__(self, username, age, city, password):
#         super().__init__(username, age, city, password)
#         self.privileges = []
    
#     def __str__(self):
#         return self.username
    
#     def set_privilage(self,priv):
#         self.privileges.append(priv)
        
#     def show_privilages(self):
#         return self.privileges
    
# admin = Admin('admin',34,'Bishkek',1234567)
# admin.set_privilage('delete post')
# admin.set_privilage('delete comment')

# print(admin.show_privilages())
# admin.profile_info()
# admin.greet_user()
        
        
        
# class Lion:
#     color = 'black'
    
# class Lioness:
#     color = 'brown'
    
# class Child(Lion,Lioness):
#     pass

# obj = Child()

# print(obj.color)
# print(Child.__mro__)


"Проблемы множественного наследования"

# 1. Проблема ромба -> решена с помощью mro


# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass 
# class D(B,C):
#     pass
# print(D.mro())

# class X:
#     pass

# class Y:
#     pass

# class Z:
#     pass

# class A(X,Y):
#     pass

# class B(Y,Z):
#     pass

# class M(B,A,Z):
#     pass

# print(M.mro())
# 2) проблема скрещивания
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# class D(B,A):
#     pass
# class M(C,D):
#     pass
    

    
"""
Миксины -> классы которые используются для наследования но от них не создаются обьекты
"""

#  используются для добавления одних и тех же методов в разные классы
# Работа с Миксинами
# 1.принято давать имена заканчивающийся на миксин getlistMixin
# 2.он не предназначен для создания от него обьектов
# 3.нужны для расширения функционала


# class MoveMixin:
#     def move(self):
#         print(f'я двигаюсь {self}')
    
# class StopMixin:
#     def stop(self):
#         print('я стою')
# class Car(MoveMixin,StopMixin):
#     def __str__(self):
#         return 'красная машина'
# class Person(MoveMixin,StopMixin):
#     def __str__(self) -> str:
#         return 'я человек'
        
# car = Car() 
# car.move()
# car.stop()


# class CreateMixin:
#     def create(self,todo,key):
#         if key in self.todos:
#             return 'Задачи под таким номером уже существует'
#         else:
#             self.todos[key] = todo
#             return self.todos
        
# class DeleteMixin:
#     def delete(self,key):
#         deleted = self.todos.pop(key)
#         return deleted
        
# class Note(CreateMixin,DeleteMixin,UpdateMixin):
#     todos = {}
    
# class UpdateMixin:
#     def update(self,key,new_value):
#         if key in self.todos.keys():
#             self.todos[key] = new_value
#             return self.todos

# task = Note()
# print(task.create('h/w',1))
# print(task.create('h/w',2))

# Классная работа

# По теме: Множественное наследование,

# Миксины

# 1
# from datetime import datetime

# class Smartphone:
#     def call(self,phone_number):
#         print(f"Вы позвонили абоненту: {phone_number}")
#     def where_to_wear(self):
#         print('You can keep me anywhere')

# class Watch:
#     def see_time(self):
#         current_time = datetime.now().time()
#         print(f'Текущее время: {current_time}')
#     def where_to_wear(self):
#         print('You should wear me on your hand')

# class SmartWatch(Smartphone,Watch):
#     pass

# smart = SmartWatch()
# smart.call("+996552590770")
# smart.see_time()
# smart.where_to_wear()

# 2

    
        

        
        
# class Tiktok():
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password



# class AppMixin:
#     def check(self,password,username):
#         checked = input("Введите логин и пароль: ")
#         name = input("Логин: ")
#         pas = input("Пароль: ")
#         cheking = {name:pas}
#         if cheking in self.account:   
#             print('Successfully created')
#         else:
#             print("Неправильный логин или пароль")
            
# class Instagram(AppMixin):
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
    
#     def post_post(self,name_post,username,password):
#         print("Вы хотите запостить фотографию \n")
#         commit = input("Введите комментарий к посту: ")
#         username = input("Введите ваш логин: \n")
#         password = input("Введите ваш пароль: \n")
#         self.check(username,password)
        
        
# class CreateMixin:
#     def create(self,password,username):
#                 self.account[username] = password
#                 return self.account
           
# class Note(AppMixin,CreateMixin):
#     account = {}  
# print("Вход в систему")
# acc = Note()
# log = input('Создаем аккаунт \n1...\n2...\n3...\nСоздайте логин: \n')
# pas = input("Создайте пароль\n") 
# acc.create(log,pas)

# print("Регистрация в Instagram")
# log1 = input('Создаем аккаунт \n1...\n2...\n3...\nСоздайте логин: \n')
# pas1 = input("Создайте пароль\n") 
# inst = Instagram(log1,pas1)
# inst.post_post()






# 1.
# class RadioMixin:
#     def play_music(self,name_music):
#         print(f'играет песня : {name_music}')

# class Auto(RadioMixin):
#     def ride(self):
#         print("Riding on a ground")
        

# class Boat(RadioMixin):
#     def swim(self):
#         print("floating on water")
        
# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()
# obj.play_music('biber')
# import datetime

# class Clock:
#     def show_time(self):
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(f"Current time: {current_time}")

# class Alarm:
#     def __init__(self):
#         self.is_enabled = False

#     def turn_on(self):
#         self.is_enabled = True
#         print("Alarm turned on")

#     def turn_off(self):
#         self.is_enabled = False
#         print("Alarm turned off")

# class AlarmClock(Clock, Alarm):
#     def set_alarm(self):
#         self.turn_on()
#         print("Alarm is set")

# # Пример использования классов
# clock = Clock()
# clock.show_time()

# alarm_clock = AlarmClock()
# alarm_clock.show_time()

# alarm_clock.set_alarm()
# alarm_clock.show_time()

# alarm_clock.turn_off()
# alarm_clock.show_time()

# class UserInitial:
#     def init(self, username,password):
#         self.username = username
#         self.password = password

#     def check_pass(self, username, password):
#         return self.username == username and self.password == password


# class SocialMedia(UserInitial):
#     def init(self, username, password):
#         super().init(username, password)
#         self.posts = 0

#     def post(self, username,password):
#         if self.check_pass(username, password):
#             self.posts += 1
#             return 'Successfully created'
#         return 'You have no permission'


# class TikTok(SocialMedia):
#     def post_post(self, username, password):
#         super().post(username, password)


# class Instagram(SocialMedia):
#     def post_post(self, username,password):
#         super().post(username, password)







class check:
    def check_account(self,login,password):
        return self.login == login and self.password == password
    

class Instagram(check):
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.post = 0
        
    def post_post(self,title,login,password):
        if self.check_account(login,password):
            self.post +=1
            print("Successfully created")
        else:
             print("Authentication failed")
             
class TikTok(check):
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.post = 0
    def post_video(self,title,login,password):
        if self.check_account(login,password):
            self.post +=1
            print("Successfully created")
        else:
             print("Authentication failed")
             
instagram = Instagram("my_username", "my_password")
tiktok = TikTok("my_username", "my_password")

instagram.post_post("My Post", "my_username", "my_password")  # Верные данные аутентификации, успешное создание
tiktok.post_video("My Video", "my_username", "my_password")  # Верные данные аутентификации, успешное создание

instagram.post_post("Another Post", "wrong_username", "wrong_password")  # Неверные данные аутентификации, аутентификация не пройдена
tiktok.post_video("Another Video", "wrong_username", "wrong_password")  # Неверные данные аутентификации, аутентификация не пройдена

print(f"Instagram Posts: {instagram.post}")
print(f"TikTok Videos: {tiktok.post}")

            


