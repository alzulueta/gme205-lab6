class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def distance_to(self, other):
        return f"Distance from {self.geometry} to {other.geometry}"

    def intersects(self, other):
        return f"{self.geometry} intersects with {other.geometry}"