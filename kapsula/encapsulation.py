# # # Основные принципы ООП: Инкапсуляция


# # # Принцип ООП у которого есть две трактовки 
# # # 1. Обьединение всех свойств и методов в единую капсулу или класс
# # # 2. Cокрытие данных ограничение доступа к методам и атрибутам 

# # # 1. Инкапсуляция как связь

# # # class Phone:
# # #     def __init__(self,number):
# # #         self.number = number
    
# # #     def print_number(self):
# # #         print(f'Мой номер: {self.number}')
# # # nokia = Phone("+9965552590770")
# # # nokia.print_number()
# # ####Связали поведение обьекта с его данными ########################


# # # 2. Инкапсуляция как сокрытие данных (управление доступом)

# # # class Point:
# # #     def __init__(self,x,y):
# # #         self.x = x
# # #         self.y = y

    
# # # pt = Point(2,3)
# # # print (pt.x,pt.y)
# # # pt.x = 5
# # # pt.y = '23'
# # # print(pt.x,pt.y)



# # # модификаторы доступа

# # #1. public -> публичный класс
# # #2. _protected -> защищенный (с одним нижним подчеркиванием вначале)-> доступны как внутри класса так и у дочерних
# # #3. __private -> приватный(с двумя подчеркиванием) -> данные доступны только внутри класса которому они принадлежат
# # # protected
# # # class Point:
# # #     def __init__(self,x,y):
# # #         self._x = x
# # #         self._y = y

# # # pt = Point(5,7) 
# # # print(pt._x,pt._y)
# # # pt._x = 'hello'
# # # print(pt._x,pt._y)



# # # class Point:
# # #     def __init__(self,x,y):
# # #         self.__x = x
# # #         self.__y = y
    
# # #     def set_coord(self,new_x,new_y):
# # #         if type(new_x) in (int,float) and type(new_y) in (int,float):
# # #             self.x = new_x
# # #             self.y = new_y
# # #         else:
# # #             raise ValueError("координаты должны быть числами")
# # #     def get_coords(self):
# # #         return self.__x,self.__y
        
        
# # # pt = Point(5,7)
# # # pt.set_coord(2,4)
# # # print(pt.get_coords())

# # # pt = Point(5,7) 
# # # print(pt.__x,pt.__y)
# # # pt._x = 'hello'



# # # class Car:
# # #     __speed = 0
    
# # #     @property
# # #     def speed(self):
# # #         return self.__speed


# # #     @speed.setter
# # #     def speed(self, new_speed):
# # #         if type(new_speed) != int:
# # #             raise ValueError("Скорость должна быть числом")
# # #         if self.__speed < 0:
# # #             raise ValueError("Скорость не может быть меньше 0")
# # #         else:
# # #             self.__speed = new_speed


    
# # # car1 = Car()
# # # print(car1.speed)
# # # car1.speed = 20
# # # print(car1.speed)
# # # --------------------------------------------------------------------------------------------------
# # # class Game:
# # #     __level = 0
# # #     def __init__(self,name):
# # #         self.name = name
        
# # #     def set
    
# # #     def play(self,hours):
# # #         if hours > 2:
# # #             self.__level +=1

# # #     def get_level(self):
# # #         return self.__level
    
# # # game = Game('Adilet')
# # # game.play(3)
# # # game.play(6)
# # # print(game.get_level())


# # # class Person:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.__age = age

# # # # делает из метода атрибут позволяет обращаться к методу как к атрибуду передоставляемый атрибут применяется для вызова декораторов геттер сеттер
    
# # #     @property
# # #     def age(self):
# # #         return self.__age
    
# # #     @age.setter
# # #     def age_setter(self,new_age):
# # #         if type (new_age) !=int:
# # #             raise ValueError('Возраст должен быть числом! ')
# # #         if new_age<self.__age:
# # #             raise ValueError('Вы не могли помодеть')
# # #         if 0<new_age<110:
# # #             self.__age = new_age
# # #         else:
# # #             print('Invalid age')
    
# # #     @age.getter
# # #     def age_getter(self):
# # #        return self.__age

# # # a = Person("kate" ,2)
# # # a.age_setter = 5
# # # print(a.age_getter)





# # # class Person:
# # #     def __init__(self,name = None,last_name = None ,age = None ,email = None):
# # #         self.name = name
# # #         self.last_name = last_name
# # #         self.age = age
# # #         self.email = email 
# # #     # ------------------------------------------------   
# # #     def get_name(self):
# # #         return self.name
    
# # #     def set_name(self,new_name):
# # #         self.name = new_name
# # #     # ----------------------------------------------   
# # #     def get_last_name(self):
# # #         return self.last_name
        
# # #     def set_last_name(self,new_last_name):
# # #         self.last_name = new_last_name
# # #     # ----------------------------------------------
# # #     def get_age(self):
# # #         return self.age
    
# # #     def set_age(self,new_age):
# # #         self.age = new_age
# # #     # ------------------------------------------
# # #     def get_email(self):
# # #         return self.email
    
# # #     def set_email(self,new_email):
# # #         self.email = new_email

# # # john = Person()
# # # print(john.get_name()) # None
# # # print(john.get_last_name()) # None
# # # print(john.get_age()) # None
# # # print(john.get_email()) # None
# # # john.set_name('John')
# # # john.set_last_name('Snow')
# # # john.set_age(30)
# # # john.set_email('johnsnow@gmail.com')
# # # print(john.get_name()) # John
# # # print(john.get_last_name()) # Snow
# # # print(john.get_age()) # 30
# # # print(john.get_email()) # johnsnow@gmail.com
    
    
# # # class Game:
# # #     __level = 0
# # #     def __init__(self,name):
# # #         self.name = self.__validate_name(name)

# # #     def set_level(self,level):
# # #         if self.name == 'Tolik':
# # #             self.__level =level
# # #         else:
# # #             print(f"{self.name} ты не Tolik!'.")

# # #     def __validate_name(self,name):
# # #         return name.capitalize()
    
# # # game = Game('Tolik')
# # # print(game.name)
# # # game.set_level(3)
# # # print(game._Game__level)
# # # game.set_level(51)
# # # print(game._Game__level)
# # # game.set_level(14)
# # # print(game._Game__level)
# # # game.set_level(26)
# # # print(game._Game__level)
# # # game.set_level(56)
# # # print(game._Game__level)
# # # game.set_level(42)
# # # print(game._Game__level)



# # # class Game:
# # #     __level = 0
    
# # #     @property
# # #     def level(self):
# # #         return self.__level
    
# # #     @level.setter
# # #     def level(self,level):
# # #         self.__level = level
        
    
# # # game = Game() 
# # # print(game.level)
# # # game.level = 10
# # # print(game.level)

# # class Person:
# #     def __init__(self,__name = None,__last_name = None ,__age = None ,__email = None):
# #         self.name = __name
# #         self.last_name = __last_name
# #         self.age = __age
# #         self.email = __email 
        
# #     @property
# #     def name(self):
# #         return self.__name

# #     @name.setter
# #     def name(self, new_name):
# #         self.__name = new_name

# #     @property
# #     def last_name(self):
# #         return self.__last_name

# #     @last_name.setter
# #     def last_name(self, new_last_name):
# #         self.__last_name = new_last_name

# #     @property
# #     def age(self):
# #         return self.__age

# #     @age.setter
# #     def age(self, new_age):
# #         self.__age = new_age

# #     @property
# #     def email(self):
# #         return self.__email

# #     @email.setter
# #     def email(self, new_email):
# #         self.__email = new_email
    
# # john = Person()
# # print(john.name) # None
# # print(john.last_name) # None
# # print(john.age) # None
# # print(john.email) # None
# # john.name = 'John'
# # john.last_name = 'Snow'
# # john.age = 30
# # john.email = 'johnsnow@gmail.com'
# # print(john.name) # John
# # print(john.last_name) # Snow
# # print(john.age) # 30
# # print(john.email) # johnsnow@gmail.com

# # class Dad:
# #     name = 'John'
# #     _last_name = 'Snow'
# #     __age = 40

# # class Me(Dad):
# #     name = 'Sam'
# #     _last_name = Dad._last_name
# #     __age = 10
    
# #     def about_me(self):
# #         print(f'My name is {self.name} {self._last_name} and I am {self.__age} years old')
        
# #     def about_dad(self):
# #         print(f"My father is {Dad.name} {Dad._last_name}")
# # me = Me()

# # # Вызываем метод about_me
# # me.about_me()
# # me.about_dad()
        
        
# # class Person:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.__age = age 
    
# #     @property
# #     def age(self):
# #         return self.__age
    
# #     @age.setter
# #     def set_age(self,new_age):
# #         if type(new_age) != int:
# #             raise ValueError("age must be integer")
# #         if 100 >= new_age and new_age > 0:
# #             self.__age = new_age
# #         else:
# #             raise Exception('age must be in range(0,100)')
    
# #     @age.getter
# #     def get_age(self):
# #         return self.__age
    
# #     @age.deleter
# #     def delete_age(self):
# #         if self.__age < 99:
# #             raise Exception('Мы не можем удалить возраст') 
# #         del self.__age 

# # john = Person('John', 18)

# # # Получаем возраст
# # print(john.name)
# # print(john.get_age)

# # # Устанавливаем новый возраст
# # john.set_age = 100

# # # Удаляем возраст (не сработает, так как он меньше 99)
# # try:
# #     john.delete_age
# # except Exception as e:
# #     print(e)

# # # Проверяем возраст
# # print(john.get_age)

# class BankAccount():
#     def __init__(self,account_number,balance):
#         self.__account_number = account_number
#         self.balance = balance
    
    
#     def set_balance(self,new_balance):
#         self.balance = new_balance
    
#     def get_balance(self):
#         return self.balance
    
#     def minus(self,cash):
#         if cash < self.balance:
#             self.balance -=cash
#         else:
#             raise Exception("Не хватает денег")
    
#     @property
#     def account_number(self):
#         return self.__account_number
#     @account_number.getter
#     def get_account_number(self):
#         return self.__account_number
    
# card = BankAccount(2341,500)
# print(card.get_balance())

# card.set_balance(1000)

# card.minus(100)

# print(card.get_balance())



class Terminal():
    def __init__(self,number_card,PIN):
        self.number_card = number_card
        self.PIN = PIN
        self.sum = 0
    
    def put(self,PIN,count):
        if PIN == self.PIN:
            self.sum +=count
            
    def get_money(self,PIN,count):
        if PIN == self.PIN and count % 10 == 0 and self.sum > count:
            self.sum -=count
        else:
            raise Exception("Проверьте Пинкод или валидацию чисел")
        
        
    
    def get_number_card(self):
        if len(self.number_card) != 16:
            raise Exception("У карты должно быть 16 чисел")
        return self.number_card
    
    def get_PIN(self):
        if len(self.PIN) != 4:
            raise Exception("У карты должно быть 4 чисел")
        return self.PIN
terminal = Terminal("1234567890123456", "1234")

terminal.put("1234", 500)

try:
    card_number = terminal.get_number_card()
    print(f"Номер карты: {card_number}")
except Exception as e:
    print(e)

try:
    pin = terminal.get_PIN()
    print(f"PIN-код: {pin}")
except Exception as e:
    print(e)

try:
    terminal.get_money("1234", 200)
    print("Снято 200 рублей")
except Exception as e:
    print(e)
try:
    terminal.get_money("1234", 15)  # Неверная сумма 
except Exception as e:
    print(e)

try:
    terminal.get_money("1234", 4000)  # Больше, чем есть на счете
except Exception as e:
    print(e)

print(f"Текущий баланс: {terminal.sum} рублей")

    
    
        
        
    





