from .spatial_object import SpatialObject

class Road(SpatialObject):
    def __init__(self, geometry, road_id, length, road_type):
        super().__init__(geometry)
        self.road_id = road_id
        self.length = length
        self.road_type = road_type
        self.adjacent_parcels = []

    def add_adjacent_parcel(self, parcel):
        self.adjacent_parcels.append(parcel)
        parcel.add_adjacent_road(self)

    def get_length(self):
        return self.length

    def describe(self):
        return f"Road {self.road_id}, Type: {self.road_type}, Length: {self.length}"