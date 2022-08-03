import math
from random import random, choice


class Vector2d:
    def random():
        choices = [-random(), random()]
        x = choice(choices)
        choices = [-random(), random()]
        y = choice(choices)
        vec = Vector2d(x, y)
        vec.normalize()
        return vec

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<{0}, {1}>".format(self.x, self.y)

    def mult(self, number):
        self.x *= number
        self.y *= number

    def multVec(self, vec):
        self.x *= vec.getX()
        self.y *= vec.getY()

    def add(self, vec):
        self.x += vec.getX()
        self.y += vec.getY()

    def sub(self, vec):
        self.x -= vec.getX()
        self.y -= vec.getY()

    def copy(self):
        return Vector2d(self.x, self.y)

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self):
        self.y = y

    def getMag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def getMagSq(self):
        return self.x**2 + self.y**2

    def setMag(self, mag):
        vec = self.getUnitVector()
        vec.mult(mag)
        self.x = vec.getX()
        self.y = vec.getY()

    def getUnitVector(self):
        mag = self.getMag()
        x = self.x / mag
        y = self.y / mag
        return Vector2d(x, y)

    def normalize(self):
        mag = self.getMag()
        self.x /= mag
        self.y /= mag

    def limit(self, limit):
        if self.getMag() > limit:
            self.setMag(limit)

    def equals(self, vec):
        return self.x == vec.getX() and self.y == vec.getY()

    def set(self, x, y):
        self.x = x
        self.y = y
