from datetime import date
from task4 import Person
from exam import Exam
from student import Student
from my_enum import Education
def main():
    
    birth = date(2004,9,1)
    person = Person("Ayana","Isaeva",birth)
    
    exams = [
        Exam("Math", 90, date(2023, 5, 10)),
        Exam("English", 80, date(2023, 5, 15)),
        Exam("History", 70, date(2023, 5, 20))
    ]

    
    # Создаем экземпляр класса Student и добавляем экзамены
    student = Student(person,Education.Specialist.value, 101)
    student.AddExams(exams)

    # Получаем текстовое представление без списка экзаменов
    short_string = student.__str__()
    string = student.string()
    
    # Выводим данные
    print(short_string)
    print(string)
    
if __name__ == "__main__":
    main()
