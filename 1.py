import random

class Device:
    def __init__(self, name, battery_life):
        self.__name = name
        self.__battery_life = battery_life

    def get_name(self):
        return self.__name

    def get_battery(self):
        return self.__battery_life
    
    def set_name(self, name):
        self.__name = name
    
    def set_battery(self, battery_life):
        self.__battery_life = battery_life
    

class SmartPhone(Device):
    def call(self, num):
        self.__name == num
        print(f"Номер {self.__num} звонит вам")
    def use(self, phone):
        
        self.__phone == phone
        print(f"Мы используем {self.__phone}")


class Laptor(Device):
    def compile_code(self, code1, code2, code3):
        self.__code1 == code1
        self.__code2 == code2
        self.__code3 == code3
        self.__rand == 0
        if random.randint(1, 3) == 1:
            self.__rand == code1
        if random.randint(1, 3) == 2:
            self.__rand == code2
        else:
            self.__rand == code3
        print(f"Ноутбук компилирует код на языке программирования {self.__rand}")

    def use(self, lap):
        self.__lap == lap
        print(f"Мы используем {self.__lap}")


class Tablet(Device):
    def draw(self, model):
        print(f"Планшет используется для рисования")

    def use(self, model):
        self.__model == model
        print(f"Мы используем {self.__model}")
