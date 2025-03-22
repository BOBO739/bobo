class Stu
    def __init__(self):
        self.height = 170
    height = 160
    def prenter(self):
        print(self.height)
    def change_height(self, new_height):
        self.height = new_height
nick = Student()
nick.print()
nick.change_height(174)
nick.print()