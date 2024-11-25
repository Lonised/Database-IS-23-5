class City:
    def __init__(self, road, building, park):
        self.road = road
        self.building = building
        self.park = park


class Road:
    def __init__(self, polosa, protyaj):
        self.polosa = polosa
        self.protyaj = protyaj

    def add_road(self):
    return f"Была добавлена новая полоса: {polosa}, протяженностью: {protyaj}"


class Building:
    def __init__(self, razmer):
        self.razmer = razmer

    def add_build(self):
    return f"Было построено новое здание, высотой {razmer} этажей"


class Park:
    def __init__(self, tree, s):
        self.tree = tree
        self.s = s

    def ploshad(self):
    return f"Площадь парка равняется: {s}, количество деревьев в парке: {tree}"

