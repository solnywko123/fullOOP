from datetime import date
from abc import ABC, abstractmethod


class IDateAndCopy(ABC):
    @abstractmethod
    def DeepCopy(self):
        pass
    
    @abstractmethod
    @property
    def Date(self):
        pass
    
    @abstractmethod
    @Date.setter
    def Date(self,new):
        pass

class Person:
    def __init__(self, __name, __last_name, __birthday):
        self.__name = __name
        self.__last_name = __last_name
        self.__birthday = __birthday
    #  для self.__birthday = __birthday (не забудь сначала обьявить метод age)
    # ------------------------------------------------------------------get set---------------------------------------------------------------------------------------------------------------
    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_birthday(self):
        return self.__birthday
    
    
    def set_name(self,new_name):
        if type(new_name) != str:
            raise ValueError("Имя должно быть строкой")
        if len(new_name) <= 1:
            raise ValueError("Имя должно быть большо одного символа")
        self.__name = new_name
        
    def set_last_name(self,new_last_name):
        if type(new_last_name) != str:
            raise ValueError("Фамилия должно быть строкой")
        if len(new_last_name) <= 1:
            raise ValueError("Фамилия должно быть большо одного символа")
        self.__last_name = new_last_name
        
    def set_birthday(self,new_date):
        if date.today() - new_date() < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if new_date() < date.today().year:
            raise ValueError("Возраст не может быть отрицательным")
        self.__birthday = new_date
    # --------------------------------------------------------------------Вывод str------------------------------------------------------------------------------------------
    def __str__(self):
        return f"Name: {self.__name}\nLast Name: {self.__last_name}\nBirthday: {self.__birthday}"
    
    def ToShortString(self):
        return str(f"Name: {self.__name}\nLast Name: {self.__last_name}")
    
  
    
    
                   
                 
    
    
    
    
        