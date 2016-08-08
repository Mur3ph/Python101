__author__ = 'Paul'
import math

class Vector2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __divmod__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def getLengthOfVector(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        length = self.getLengthOfVector()
        if length != 0:
            return Vector2D(self.x / length, self.y / length)
        return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def __str__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y)
