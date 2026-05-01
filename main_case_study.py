from models.parcel import Parcel
from models.building import Building
from models.road import Road
from models.household import Household

# Create parcel objects
parcel1 = Parcel({"x": 10, "y": 10}, "P1", 500, "Residential")
parcel2 = Parcel({"x": 30, "y": 15}, "P2", 750, "Commercial")

# Create building objects and connect them to parcels
building1 = Building({"x": 11, "y": 10}, "B1", 10, "Residential", parcel1)
building2 = Building({"x": 31, "y": 15}, "B2", 15, "Commercial", parcel2)

# Create household objects and connect them to buildings
household1 = Household("H1", 4, 20000, "Owner", building1)
household2 = Household("H2", 3, 18000, "Renter", building1)
household3 = Household("H3", 5, 30000, "Owner", building2)

# Create road object and connect it to parcels
road1 = Road({"x": 20, "y": 12}, "R1", 100, "Main Road")
road1.add_adjacent_parcel(parcel1)
road1.add_adjacent_parcel(parcel2)

# Display object descriptions
print("OBJECT DESCRIPTIONS")
print(parcel1.describe())
print(parcel2.describe())
print(building1.describe())
print(building2.describe())
print(household1.describe())
print(household2.describe())
print(household3.describe())
print(road1.describe())

# Test class-specific methods
print("\nCLASS-SPECIFIC METHODS")
print("Parcel 1 area:", parcel1.compute_area())
print("Building 1 height:", building1.get_height())
print("Road 1 length:", road1.get_length())
print("Household 1 income:", household1.calculate_total_income())

# Test shared methods from SpatialObject
print("\nSHARED SPATIAL METHODS")
print("Distance from Parcel 1 to Parcel 2:", parcel1.distance_to(parcel2))
print("Distance from Building 1 to Road 1:", building1.distance_to(road1))
print("Does Parcel 1 intersect Building 1?", parcel1.intersects(building1))

# Show relationships between objects
print("\nRELATIONSHIPS")
print("Building", building1.building_id, "is located on Parcel", building1.parcel.parcel_id)
print("Building", building2.building_id, "is located on Parcel", building2.parcel.parcel_id)

print("Household", household1.household_id, "lives in Building", household1.building.building_id)
print("Household", household2.household_id, "lives in Building", household2.building.building_id)
print("Household", household3.household_id, "lives in Building", household3.building.building_id)

print("Road", road1.road_id, "is adjacent to:")
for parcel in road1.adjacent_parcels:
    print("-", parcel.parcel_id)