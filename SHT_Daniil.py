class Device:
    def __init__(self, name, battery_life):
        self._name = name
        self._battery_life = battery_life

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_battery_life(self):
        return self._battery_life

    def set_battery_life(self, battery_life):
        self._battery_life = battery_life


class Smartphone(Device):
    def call(self):
        print("Телефон звонит")

    def use(self):
        self.call()


class Laptop(Device):
    def compile_code(self):
        print("Ноутбук компилирует код")

    def use(self):
        self.compile_code()


class Tablet(Device):
    def draw(self):
        print("Планшет используется для рисования")

    def use(self):
        self.draw()


devices = [
    Smartphone("iPhone", 10),
    Laptop("MacBook", 8),
    Tablet("iPad", 6)
]

for device in devices:
    device.use()