from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def _area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def _area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Uncommenting the following line will raise an error because we’re missing method implementations
# shape = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods #area, perimeter

circle = Circle(5)
print(f"Area: {circle._area()}")
print(f"Perimeter: {circle.perimeter()}")

# Area: 78.53975
# Perimeter: 31.4159