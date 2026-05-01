from .spatial_object import SpatialObject

class Parcel(SpatialObject):
    def __init__(self, geometry, parcel_id, area, zone):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.area = area
        self.zone = zone
        self.buildings = []
        self.adjacent_roads = []

    def add_building(self, building):
        self.buildings.append(building)

    def add_adjacent_road(self, road):
        self.adjacent_roads.append(road)

    def compute_area(self):
        return self.area

    def describe(self):
        return f"Parcel {self.parcel_id}, Zone: {self.zone}, Area: {self.area}"