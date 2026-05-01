from .spatial_object import SpatialObject

class Rooftop(SpatialObject):
    def __init__(self, geometry):
        super().__init__(geometry)
        self.slope = None
        self.aspect = None
        self.usable_area = None
        self.suitability_score = None
        self.classification = None

    def calculate_slope(self, slope):
        self.slope = slope

    def calculate_aspect(self, aspect):
        self.aspect = aspect

    def classify_suitability(self, slope_threshold, aspect_preference):
        if self.slope <= slope_threshold and self.aspect == aspect_preference:
            self.suitability_score = 1
            self.classification = "Suitable"
        else:
            self.suitability_score = 0
            self.classification = "Not Suitable"

        return self.classification

    def compute_usable_area(self, panel_size):
        self.usable_area = 100 / panel_size
        return self.usable_area

    def describe(self):
        return (
            f"Rooftop: slope={self.slope}, aspect={self.aspect}, "
            f"usable_area={self.usable_area}, classification={self.classification}"
        )