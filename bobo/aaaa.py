class Student:
   amount_of_studemts = 0
    def __init__(self,heinght= 160):
        self.height = heinght
        Student.amount_of_student += 1


print(Student.amount_of_studemts
nick = Student()
kate = Student(heinght= 165)
print(nick.amount_of_student)
print(Student.amount_of_student)
