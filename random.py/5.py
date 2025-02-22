class Triangle:
    def __init__(self, length):
        self.length=length
    def perimeter(self):
        return 3 * self.length
triangle=Triangle(5)
print(triangle.perimeter())