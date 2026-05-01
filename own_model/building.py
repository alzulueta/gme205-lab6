from .spatial_object import SpatialObject

class Building(SpatialObject):
    def __init__(self, geometry, building, area):
        super().__init__(geometry)
        self.building = building
        self.area = area
        self.rooftop = None

    def extract_rooftop(self, rooftop):
        self.rooftop = rooftop

    def compute_area(self):
        return self.area

    def describe(self):
        return f"Building {self.building}, Area: {self.area}"