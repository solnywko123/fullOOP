from task4 import Person
from exam import Exam
class Student:
    def __init__(self, __class_person, __education, __exam,):
        self.__class_person = __class_person
        self.__education = __education
        self.__exam = []
    
    def get_person(self):
        return self.__class_person
    def get_education(self):
        return self.__education
    def get_exam(self):
        return self.__exam
    
    def set_person(self,new):
        self.__class_person = new
    def set_education(self,new):
        self.__education = new
    def set_exam(self,new):
        self.__exam = new
    
    def average(self):
        
        if not self.__exam:
            return 0 
        
        total = sum(exam.score for exam in self.__exam)
        return total/len(self.__exam)
    
    def educate(self,education):
        if education == Person.Education.Specialist:
            return True
        if education == Person.Education.SecondEducation:
            return True
        if education == Person.Education.Вachelor:
            return True
    
   
    def AddExams(self, exams):
        for exam in exams:
            if not isinstance(exam, Exam):
                raise TypeError("Аргументы должны быть экземплярами класса Exam")
            self.__exam.append(exam)
            
    
    def __str__(self):
        exam_strings = [f"Subject name: {exam.subject}, Score subject: {exam.score}, Date exam: {exam.date_time}" for exam in self.__exam]
        exams_info = ", \n".join(exam_strings)
        return f'Person: {self.__class_person}, education: {self.__education}, exams: [{exams_info}]\n'
    
    def string(self):
        average = self.average()
        
        return f'Person: {self.__class_person}, education: {self.__education}, exams points: {average}'
    
    

    
    
        