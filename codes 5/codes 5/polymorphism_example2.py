import math

class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass


class Square(Shape):
    def __init__(self, length):
        super().__init__('Square')
        self.length = length
    
    def area(self):
        return self.length**2
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius**2


    
####

s = Square(8)
c = Circle(2.5)

for _ in [s, c]:
    print(_.area())

