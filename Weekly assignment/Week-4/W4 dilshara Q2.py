import math

class Circle:
    def __init__(self):
        self.a = float(input("Enter the x-coordinate of the center: "))
        self.b = float(input("Enter the y-coordinate of the center: "))
        self.r = float(input("Enter the radius: "))

    def Area(self):
        return math.pi * self.r**2

    def Perimeter(self):
        return 2 * math.pi * self.r

    def testBelongs(self, x, y):
        if (x - self.a)**2 + (y - self.b)**2 - self.r**2 == 0:
            return True
        else:
            return False

class Cylinder(Circle):
    def __init__(self):
        super().__init__()
        self.height = float(input("Enter the height of the cylinder: "))

    def Volume(self):
        return math.pi * self.r**2 * self.height

# Create a Circle object
circle = Circle()
print("Area:", circle.Area())
print("Perimeter:", circle.Perimeter())
x = float(input("Enter the x-coordinate of the point to test: "))
y = float(input("Enter the y-coordinate of the point to test: "))
print("Belongs to circle:", circle.testBelongs(x, y))

# Create a Cylinder object
cylinder = Cylinder()
print("Volume:", cylinder.Volume())
