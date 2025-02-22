class Rectangular:
    def perimeter(self):
        return 0

class Perimeter(Rectangular):
    def __init__(self,length):
        self.length=length
    def perimeter(self):
        return self.length * 3
    