# GmE 205 Lab 6 
## From UML Class Diagram to Python Code

## Overview
This laboratory focuses on translating UML class diagrams into working Python code using object-oriented programming principles. It builds on the Lecture 6 case study and extends it by implementing a custom UML design created in the pre-laboratory.

The main goal is to demonstrate how conceptual object models (UML) are transformed into functional software systems through classes, attributes, methods, inheritance, and object relationships.

## Reflection

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