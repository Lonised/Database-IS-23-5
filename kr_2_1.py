# Вариант 5

class Computer:
    def __init__(self, processor, ram, hd, graphics):
	self.processor = processor 
	self.ram = ram 
	self.hd = hd
	self.graphics = graphics


class Processor(Computer):
    def __init__(self, processor):
	self.processor = processor
    
class RAM(Computer):
    def __init__(self, ram):
	self.ram = ram
    
class HardDrive(Computer):
    def __init__(self, hd):
	self.hd = hd
    
class GraphicsCard(Computer):
    def __init__(self, graphics):
	self.graphics = graphics 

