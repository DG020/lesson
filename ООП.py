class Person():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def whatsup(self):
        print("Васап,меня зовут " + self.name + self.surname)
human = Person("Карл ","Джонсон")
human.whatsup()


    