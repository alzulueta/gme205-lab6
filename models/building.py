from .spatial_object import SpatialObject

class Building(SpatialObject):
    def __init__(self, geometry, building_id, height, usage, parcel=None):
        super().__init__(geometry)
        self.building_id = building_id
        self.height = height
        self.usage = usage
        self.parcel = parcel
        self.households = []

        if self.parcel is not None:
            self.parcel.add_building(self)

    def add_household(self, household):
        self.households.append(household)

    def get_height(self):
        return self.height

    def describe(self):
        return f"Building {self.building_id}, Usage: {self.usage}, Height: {self.height}"