#Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

#Task 1: Vehicle Registration System

#Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
#Code Example: Provide a basic structure for the Vehicle class without methods.
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
#Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Creating instances of Vehicle

vehicle1 = Vehicle("ABC123", "Car", "John Doe")
vehicle2 = Vehicle("XYZ789", "Motorcycle", "Jane Smith")
vehicle3 = Vehicle("DEF456", "Truck", "Alice Johnson")

# Updating owners

vehicle1.update_owner("Michael Brown")
vehicle2.update_owner("Sarah Lee")
vehicle3.update_owner("David Wilson")

# Displaying updated owners

print(vehicle1.owner)
print(vehicle2.owner)
print(vehicle3.owner)