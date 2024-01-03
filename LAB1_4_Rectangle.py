"""."""
class Rectangle:
    """calss"""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        """method"""
        return self.height*self.width

    def calculate_perimeter(self):
        """method"""
        return (2*self.height)+(2*self.width)

rectangle = Rectangle(float(input()), float(input())) #input(h, w)

condition = input() #condition -> area / perimeter
if condition == "area":
    result = rectangle.calculate_area()
else:
    result = rectangle.calculate_perimeter()
print("%.2f" % result)
