from math import sqrt

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def distance_to(self, other):
        dx = other.geometry["x"] - self.geometry["x"]
        dy = other.geometry["y"] - self.geometry["y"]
        return sqrt(dx ** 2 + dy ** 2)

    def intersects(self, other):
        return self.geometry == other.geometry