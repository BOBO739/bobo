class Student(object):
    def __init__(self, name=None, height = 160 ):
        self.name = name
        self.height = height
    def __bool__(self):
        return bool(self.height)
    def __str__(self)
        return f"яка довжина в нас зріст = {self.name}"
    def __del____(self):
        print("Студкнт все ...")
nick = Student()
print(nick.__bool__())