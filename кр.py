class Device:
    def __init__(self, name, battery_life):
        self.__name = name
        self.__battery_life = battery_life

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self, battery_life):
        self.__battery_life = battery_life

    def use(self):
        pass


class Smartphone(Device):
    def call(self):
        print("Телефон звонит")

    def use(self):
        print("мы юзаем смартфон")


class Laptop(Device):
    def compile_code(self):
        print("Ноутбук компилирует код")
        
    def use(self):
        print("мы юзаем ноутбук")

class Tablet(Device):
    def draw(self):
        print("Планшет используется для рисования")
        
    def use(self):
        print("мы юзаем планшет")
    
  
smartphone = Smartphone("Xiaomi 12T", 6)
laptop = Laptop("Lenovo legion", 5)
tablet = Tablet("Galaxy Tab 4", 7)

obj_list = [smartphone, laptop, tablet]

for obj in obj_list:
    obj.use()