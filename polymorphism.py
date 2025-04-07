class Vehicle:
    """
    Base class representing a general vehicle, now includes speed and fuel_type 
    attributes to demonstrate additional features.
    """
    def __init__(self, speed, fuel_type):
        """
        Initializes the Vehicle object with speed and fuel_type.
        Parameters:
        - speed: The speed of the vehicle (e.g., in km/h).
        - fuel_type: The type of fuel the vehicle uses (e.g., 'Petrol', 'Diesel', or 'Electric').
        """
        self.speed = speed
        self.fuel_type = fuel_type

    def move(self):
        """
        Default move method, meant to be overridden by subclasses.
        """
        return "This vehicle moves."

    def vehicle_info(self):
        """
        Provides information about the vehicle's speed and fuel type.
        """
        return f"Speed: {self.speed} km/h, Fuel Type: {self.fuel_type}"

# Subclass for Car
class Car(Vehicle):
    """
    Represents a car. Overrides the move method to define how cars move.
    """
    def move(self):
        """
        Car-specific implementation of the move method.
        """
        return "Driving 🚗"

# Subclass for Plane
class Plane(Vehicle):
    """
    Represents a plane. Overrides the move method to define how planes move.
    """
    def move(self):
        """
        Plane-specific implementation of the move method.
        """
        return "Flying ✈️"

# Subclass for Bicycle
class Bicycle(Vehicle):
    """
    Represents a bicycle. Since bicycles don't use fuel, override the fuel_type attribute.
    """
    def __init__(self, speed):
        """
        Initializes the Bicycle object with speed but sets fuel_type to 'Calories'.
        """
        super().__init__(speed, fuel_type="Calories")

    def move(self):
        """
        Bicycle-specific implementation of the move method.
        """
        return "Pedaling 🚴"

# Subclass for Motorbike (New Addition!)
class Motorbike(Vehicle):
    """
    Represents a motorbike. Overrides the move method to define how motorbikes move.
    """
    def move(self):
        """
        Motorbike-specific implementation of the move method.
        """
        return "Riding 🏍️"

# Demonstrating object instantiation with personalized attributes
# Example: Change speed and fuel type for vehicles to reflect your scenario.
car = Car(speed=120, fuel_type="Diesel")
plane = Plane(speed=900, fuel_type="Jet Fuel")
bicycle = Bicycle(speed=25)
motorbike = Motorbike(speed=150, fuel_type="Petrol")

# Demonstrating polymorphism and additional methods
print(car.move())            # Outputs: Driving 🚗
print(car.vehicle_info())    # Outputs: Speed: 120 km/h, Fuel Type: Petrol

print(plane.move())          # Outputs: Flying ✈️
print(plane.vehicle_info())  # Outputs: Speed: 900 km/h, Fuel Type: Jet Fuel

print(bicycle.move())        # Outputs: Pedaling 🚴
print(bicycle.vehicle_info()) # Outputs: Speed: 25 km/h, Fuel Type: None

print(motorbike.move())      # Outputs: Riding 🏍️
print(motorbike.vehicle_info()) # Outputs: Speed: 150 km/h, Fuel Type: Petrol