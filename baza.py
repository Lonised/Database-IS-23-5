class Appliance:
    def __innit__(self, _brand, _power):
        self._brand = brand
        self._power = power

    def get_brand(self):
        return self._brand

    def set_brand(self, _brand):
        self._brand = brand

    def get_power(self):
        return self._power

    def set_power(self._power):
        self._power = power

    def operate():
        pass

class WashingMachine(Appliance):
    def wash(self):
        print("Стиральная машина стирает")

    def operate(self):
        self.wash()

class Refrigerator(Appliance):
    def cool(self):
        print("Холодильник охлаждает")

    def operate(self):
        self.cool()

class Microwave(Appliance):
    def heat(self):
        print("Микроволновка разогревает еду")  

    def operate():
        self.heat()

washingmachine = WashingMachine(LG, "2500")
refrigerator = Refrigerator(Samsung, "3200")
microwave = Microwave(Razer, "5500")

appliance = [washingmachine, refrigerator, microwave]

for Appliance in appliance
    Appliance(operate)