# GmE 205 Lab 6 
## From UML Class Diagram to Python Code

## Overview
This laboratory focuses on translating UML class diagrams into working Python code using object-oriented programming principles. It builds on the Lecture 6 case study and extends it by implementing a custom UML design created in the pre-laboratory.

The main goal is to demonstrate how conceptual object models (UML) are transformed into functional software systems through classes, attributes, methods, inheritance, and object relationships.

## Part B Summary

1. The parent class in the system is `SpatialObject`, which contains shared spatial attributes and methods such as geometry, `distance_to()`, and `intersects()`.
2. The classes that inherited from `SpatialObject` are `Parcel`, `Building`, and `Road`. These classes reuse the shared spatial behavior while adding their own specific attributes.
3. The shared methods are `distance_to()` and `intersects()`, which are implemented once in `SpatialObject` and inherited by the spatial classes.
4. The relationships implemented include:
   - A `Building` is located on a `Parcel`
   - A `Household` lives in a `Building`
   - A `Road` is adjacent to one or more `Parcel` objects  
   These relationships were implemented using object references.

## Part C Summary

1. The classes in my model are:
   - `SpatialObject`
   - `Building`
   - `Rooftop`
   - `TerrainModel`
2. The attributes from the UML were translated into object state using the constructor (`__init__`). For example:
   - `area` became `self.area` in Building
   - `slope`, `aspect`, and `usable_area` became attributes in Rooftop
   - `elevation` and `cell_size` became attributes in TerrainModel
3. The methods in the UML were implemented as class methods. These include:
   - `compute_area()` in Building
   - `calculate_slope()`, `calculate_aspect()`, `classify_suitability()`, and `compute_usable_area()` in Rooftop
   - `derive_slope()` and `derive_aspect()` in TerrainModel
4. The relationships were implemented using object references. The most challenging part was connecting the `Building` and `Rooftop`, and ensuring that rooftop properties were derived using the `TerrainModel`. This required careful linking of objects and method calls.

## UML Evidence

- My case study UML diagram is stored at: uml/case_study_uml.jpg  
- My own UML diagram is stored at: uml/own_uml.jpg

## Reflection

1. The easiest to translate into code was attributes, because they directly map to variables inside the constructor. Methods required more thinking because they needed logic, and inheritance required understanding how classes are connected.
2. The hardest relationship to implement was between `Rooftop` and `TerrainModel`, because it involved deriving values (slope and aspect) rather than just storing references.
3. My code mostly matched my UML, but I made small adjustments during implementation, especially in how methods were structured and how values were computed.
4. This exercise showed the importance of OOAD because it helped organize the system before coding. By clearly defining classes, attributes, methods, and relationships, the implementation became more structured and easier to follow.

### B.2 Start with the base class: SpatialObject

1. SpatialObject owns geometry because all spatial entities share this property.
2. distance_to() should not be rewritten because it is a shared behavior applicable to all spatial objects.
3. This supports abstraction and reuse because shared logic is implemented once and inherited by subclasses.

### B.4 ocus on constructors (__init__) as the translation of UML attributes

1. Yes, I included the important attributes in each class based on the UML diagram. For example, Parcel has `area` and `zone`, Building has `height` and `usage`, Road has `length` and `road_type`, and Household has `income`.
2. Yes, I placed the attributes in the correct class. I made sure that each attribute belongs to the object it describes, such as `height` for Building and not for Parcel.
3. Yes, I avoided putting unrelated data in each object. I only included attributes that are relevant to the role of the class, and I did not mix attributes from different objects.

### B.6 Apply inheritance correctly

1. Yes, each spatial class (Parcel, Building, and Road) inherits from `SpatialObject`. This is shown in the class definitions using subclassing.
2. Yes, each class calls `super().__init__(geometry)` in the constructor to initialize the shared geometry attribute from the parent class.
3. Yes, shared methods such as `distance_to()` and `intersects()` are inherited from `SpatialObject` and are not rewritten in the subclasses. This avoids code duplication and follows the concept of reuse.

