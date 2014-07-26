import math

class Point(object):
    """Creates a point on a coordinate plane with values x, y, and z."""

    COUNT = 0

    def __init__(self):
        """ Create a new point at the origin """
        self.X = 0
        self.Y = 0
        self.Z = 0
        Point.COUNT += 1

    def __init__(self, x, y, z):
        """Defines x, y, and z variables"""
        self.X = x
        self.Y = y
        self.Z = z
        Point.COUNT += 1

    def move(self, dx, dy):
        """Determines where x and y move"""
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s,%s)"%(self.X, self.Y, self.Z) 

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        dz = self.Z - other.Z
        return math.sqrt(dx**2 + dy**2 + dz**2)

