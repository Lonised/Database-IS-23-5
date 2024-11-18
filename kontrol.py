class Device:
    def __init__(self, name, battery_life):
        self.__name = name
        self.__battery_life = battery_life

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name = name

    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self):
        self.__battery_life = battery_life

    def use(self):
        pass

class Smartphone(Device):
    def call(self):
        print(f'Телефон звонит')

    def use(self):
        self.call()


class Laptor(Device):
    def compile_code(self):
        print(f"Ноутбук компилирует код")

    def use(self):
        self.compile_code()


class Tablet(Device):
    def draw(self):
        print(f"Планшет используется для рисования")

    def use(self):
        self.draw()
        
smartphone = Smartphone("Lenovo", "12")
laptor = Laptor("Lenovo", "2021")
tablet = Tablet("Levo", "2025")

devices = [smartphone, laptor, tablet]

for Device in devices:
    Device.use
