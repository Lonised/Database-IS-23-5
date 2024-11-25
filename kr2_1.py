class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

     
class FieldPlayer(Player):
    def __init__(self, name, status, heath):
        self.name = name
        self.status = status
        self.health = health

class Goalkeeper(Player):
    def __init__(self, name, form, mood):
        self.name = name
        self.form = form
        self.mood = mood


class Team:
    self.name = name