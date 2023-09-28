from datetime import date

class Exam:
    def __init__(self, subject=' ', score=0, date_time=date.today()):
        self.__subject = subject
        self.__score = score
        self.__date_time = date_time

    @property
    def subject(self):
        return self.__subject
    
    @subject.setter
    def subject(self, new_subject):
        self.__subject = new_subject
        
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, new_score):
        self.__score = new_score
        
    @property
    def date_time(self):
        return self.__date_time
    
    @date_time.setter
    def date_time(self, new_date_time):
        if not isinstance(new_date_time, date):
            raise ValueError("Значение должно быть типа datetime.date")
        self.__date_time = new_date_time

    def __str__(self):
        return f"Subject name: {self.subject}, Score subject: {self.score}, Date exam: {self.date_time}"
    