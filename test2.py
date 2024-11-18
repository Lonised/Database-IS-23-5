#1 вариант

class Vehicle():
    def __init__ (self, _speed, _color):
        self._speed = _speed
        self._color = _color
    
    def set_speed(self, _speed):
        return _speed

    def set_color(self, _color):
        return _color 
    
    def get_speed(self):
        self._speed

    def get_color(self):
        self._color 
    

class Car(Vehicle):
    def __init__(self, _speed, _color):
        super().__init__(_speed, _color)

    def drive():
        return f"Машина едет"

    def move():
        return f"лодка плывет"

    
    
class Bike(Vehicle):
    def __init__(self, _speed, _color):
        super().__init__(_speed, _color)

    def pedal():
        return f"велосипед крутит педали логикал"

    def move():
        return f"лодка плывет"
    
    
class Boat(Vehicle):
    def __init__(self, _speed, _color):
        super().__init__(_speed, _color)

    def sail():
        return f"лодка плывет"

    def move():
        return f"лодка плывет"
       
       