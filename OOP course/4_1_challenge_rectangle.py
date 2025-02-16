class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        self.area = self.length * self.width
        return self.area

    def get_perimeter(self):
        self.perimeter = (self.length * 2) + (self.width * 2)
        return self.perimeter

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
