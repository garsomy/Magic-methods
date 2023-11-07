import math

class RightTriangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plus_side(self, per):
        self.a *= (1 + per / 100)
        self.b *= (1 + per / 100)

    def minus_side(self, per):
        self.a *= (1 - per / 100)
        self.b *= (1 - per / 100)

    def circle_radius(self):
        r = (self.a + self.b - math.sqrt(self.a ** 2 + self.b ** 2)) / 2
        return r

    def perimeter(self):
        p = self.a + self.b + math.sqrt(self.a ** 2 + self.b ** 2)
        return p

    def angles(self):
        angle_A = math.degrees(math.atan(self.b / self.a))
        angle_B = math.degrees(math.atan(self.a / self.b))
        angle_C = 90
        return angle_A, angle_B, angle_C






t = RightTriangle(3, 4)
print("Начальные значения:")
print("Сторона a:", t.a)
print("Сторона b:", t.b)

t.plus_side(10)
print("Увеличения на 10%:")
print("Сторона a:", t.a)
print("Сторона b:", t.b)

t.minus_side(20)
print("Уменьшения на 20%:")
print("Сторона a:", t.a)
print("Сторона b:", t.b)

r = t.circle_radius()
print("Радиус описанной окружности:", r)

p = t.perimeter()
print("Периметр:", p)

angles = t.angles()
print("Значения углов:")
print("Угол A:", angles[0])
print("Угол B:", angles[1])
print("Угол C:", angles[2])