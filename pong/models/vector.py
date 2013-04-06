class Vector2d(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __str__(self):
        return "{%.2f, %.2f}" % (self.x, self.y)
