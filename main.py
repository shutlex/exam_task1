from abc import ABC, abstractmethod



class IDrawable(ABC):

    @abstractmethod
    def draw(self):
        pass



class Shape(IDrawable):

    @abstractmethod
    def calculate_area(self):
        pass

    def draw(self):
        raise NotImplementedError("Метод Draw має бути реалізований у похідних класах.")



class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def draw(self):
        print(f"Креслення кола з радіусом {self.radius}")



class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def draw(self):
        print(f"Малювання квадрата зі стороною {self.side}")



class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print(f"Креслення трикутника з основою {self.base} і висота {self.height}")


def main():
    shapes = [Circle(5), Square(4), Triangle(3, 6)]

    for shape in shapes:
        area = shape.calculate_area()
        shape.draw()
        print(f"Площа: {area}")
        print()


if __name__ == "__main__":
    main()

