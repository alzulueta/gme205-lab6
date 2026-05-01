# GmE 205 Lab 6 
## From UML Class Diagram to Python Code

## Overview
This laboratory focuses on translating UML class diagrams into working Python code using object-oriented programming principles. It builds on the Lecture 6 case study and extends it by implementing a custom UML design created in the pre-laboratory.

The main goal is to demonstrate how conceptual object models (UML) are transformed into functional software systems through classes, attributes, methods, inheritance, and object relationships.

## Reflection

### B.2 

1. SpatialObject owns geometry because all spatial entities share this property.
2. distance_to() should not be rewritten because it is a shared behavior applicable to all spatial objects.
3. This supports abstraction and reuse because shared logic is implemented once and inherited by subclasses.

