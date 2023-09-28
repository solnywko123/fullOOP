# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}"
        
        
# class Employee(Person):
#     def __init__(self, person_instance, work, status):
#         super().__init__(person_instance.name, person_instance.last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}."

# class Student(Person):
#     def __init__(self,person_instance, university, course,):
#         super().__init__(person_instance.name,person_instance.last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе"
    
# import math 
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         return 0.5 * self.base * self.height
        

# class Square(Shape):
#     def __init__(self,lenght):
#         self.lenght = lenght
#     def get_area(self):
#         return self.lenght * self.lenght

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         return math.pi * self.radius **2

        

# class OS:
#     def __init__(self, version):
#         self.version = version

# class Windows(OS):
#     def copy(self,text):
#         return f"скопирован текст {text} горячими клавишами CTRL + C"

# class MacOS(OS):
#     def copy(self,text):
#         return f'скопирован текст {text} горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self,text):
#         return f'скопирован текст {text} горячими клавишами CTRL + SHIFT + C'


class Language:
    def __init__(self,level,type):
        self.level = level
        self.type = type


class JavaScript(Language):
    def write_function(self, func_name, arg):
        return f"function {func_name}({arg}) {{    }};"

    def create_variable(self, var_name, value):
        return f"let {var_name} = '{value}'"
    
    
class Python(Language):
    def write_function(self,func_name,arg):
        return f'def {func_name}({arg}):'
    def create_variable(self,var_name,value):
        return f'{var_name} = {value}'
    

     