from own_model.building import Building
from own_model.rooftop import Rooftop
from own_model.terrain_model import TerrainModel

# Create objects based on the UML diagram
building = Building({"x": 10, "y": 10}, "B1", 200)
rooftop = Rooftop({"x": 10, "y": 10})
terrain_model = TerrainModel({"x": 10, "y": 10}, 100, 5)

# Connect Building to Rooftop
building.extract_rooftop(rooftop)

# Derive rooftop values from TerrainModel
rooftop.calculate_slope(terrain_model.derive_slope())
rooftop.calculate_aspect(terrain_model.derive_aspect())

# Evaluate rooftop suitability
rooftop.compute_usable_area(2)
rooftop.classify_suitability(15, "South")

print("OBJECT DESCRIPTIONS")
print(building.describe())
print(rooftop.describe())
print(terrain_model.describe())

print("\nCLASS-SPECIFIC METHODS")
print("Building area:", building.compute_area())
print("Derived slope:", rooftop.slope)
print("Derived aspect:", rooftop.aspect)
print("Usable rooftop area:", rooftop.usable_area)
print("Suitability score:", rooftop.suitability_score)
print("Classification:", rooftop.classification)

print("\nSHARED SPATIAL METHODS")
print("Distance from Building to Rooftop:", building.distance_to(rooftop))
print("Does Building intersect Rooftop?", building.intersects(rooftop))

print("\nRELATIONSHIPS")
print("Building", building.building, "has a rooftop:", building.rooftop is not None)
print("Rooftop belongs to Building:", building.rooftop == rooftop)  
print("Rooftop properties were derived using TerrainModel")
print("TerrainModel inherits from Rooftop:", isinstance(terrain_model, Rooftop))