from .rooftop import Rooftop

class TerrainModel(Rooftop):
    def __init__(self, geometry, elevation, cell_size):
        super().__init__(geometry)
        self.elevation = elevation
        self.cell_size = cell_size

    def derive_slope(self):
        return 10

    def derive_aspect(self):
        return "South"

    def describe(self):
        return f"TerrainModel: elevation={self.elevation}, cell_size={self.cell_size}"