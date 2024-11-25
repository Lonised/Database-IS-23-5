class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

# А этот класс - новый. Наследник Counter
class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
    def dec(self):
        pass