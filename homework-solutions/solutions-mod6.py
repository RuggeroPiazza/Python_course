class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return (self.height + self.width)*2

# create two instances of the class
rect1 = Rectangle()  # default values
rect2 = Rectangle(3, 7)


#outputs
print(f"Width: {rect1.width}\n"
      f"height: {rect1.height}\n"
      f"Area: {rect1.getArea()}\n"
      f"Perimeter {rect1.getPerimeter()}")
