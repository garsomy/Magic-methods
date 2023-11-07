class Vector3D:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f'({self.x}, {self.y}, {self.z}')

    def read(self):
        self.x = float(input('x координата: '))
        self.y = float(input('x координата: '))
        self.z = float(input('x координата: '))

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError('Ошибка.', format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError('Ошибка.', format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError('Ошибка', format(type(other)))

    def __matmul__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)
        else:
            raise TypeError('Ошибка.', format(type(other)))


v1 = Vector3D(4, 1, 2)
v1.display()
v2 = Vector3D()
v2.read()
v3 = Vector3D(1, 2, 3)
v4 = v1 + v2
v4.display()
a = v4 * v3
print(a)
v4 = v1 * 10
v4.display()
v4 = v1 @ v3
v4.display()
