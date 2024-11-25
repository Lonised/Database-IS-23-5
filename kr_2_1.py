# Вариант 5

class Processor:
    def __init__(self, model):
        if not isinstance(model, str):
            raise ValueError("Processor model must be a string.")
        self.model = model


class RAM:
    def __init__(self, size):
        if not isinstance(size, int) or size <= 0:
            raise ValueError("RAM size must be a positive integer.")
        self.size = size


class HardDrive:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Hard drive capacity must be a positive integer.")
        self.capacity = capacity


class GraphicsCard:
    def __init__(self, model):
        if not isinstance(model, str):
            raise ValueError("Graphics card model must be a string.")
        self.model = model


class Computer:
    def __init__(self, processor, ram, hd, graphics):
        if not isinstance(processor, Processor):
            raise TypeError("processor must be an instance of Processor.")
        if not isinstance(ram, RAM):
            raise TypeError("ram must be an instance of RAM.")
        if not isinstance(hd, HardDrive):
            raise TypeError("hd must be an instance of HardDrive.")
        if not isinstance(graphics, GraphicsCard):
            raise TypeError("graphics must be an instance of GraphicsCard.")
        
        self.processor = processor
        self.ram = ram
        self.hd = hd
        self.graphics = graphics

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"Processor: {self.processor.model}\n"
                f"RAM: {self.ram.size} GB\n"
                f"Hard Drive: {self.hd.capacity} GB\n"
                f"Graphics Card: {self.graphics.model}")
