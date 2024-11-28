#Variant 2
class Book:
    def __init__(self, title, author, available):
        self.__title = title
        self.__author = author
        self.__available = available

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.__title = title
  
    def borrow(self):
       


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info():
        return(f"Имя сотрудника: " {self.name}, "должность сотрудника: ", {self.position}, "зарплата: " {self.salary})

class Manager(Employee):
    def otdel(self, department):
        self.department = department
    return (f"Отдел: ," {department})

class Developer(Employee):
    def programm(self, programming_language):
        self.programming_language = programming_language
    return (f"Язык программирования: ," {programming_language})

sotrudnik = Employee("Artem", "CEO", 900000)
developer = Developer("Sanya","prog", 120000, "python")
manager = Manager("Vasya","Someone", 110000, "Thief")

employee = [sotrudnik, developer, manager]

class Device:
    def __init__(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_model(self, model) 
        self.model = model

    def turn_on():
        pass

class Phone(Device):
    def turn_on():
        print("Phone is now on")

class Laptop(Device):
    def turn_on():
        print("Laptop is booting up")

class Tablet(Device):
    def turn_on():
        print("Tablet is ready to use")

phone = Phone(Samsung)
laptop = Laptop(Asus)
tablet = Tablet(Apple)

devices = [phone, laptop, tablet]

for Device in devices:
    Device.turn_on()