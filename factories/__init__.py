# factories/__init__.py

from .vehicle_factory import randomVehicleAlgorithm
from .bicycle_factory import BicycleFactory
from .car_factory import CarFactory

__all__ = [
    "randomVehicleAlgorithm",
    "BicycleFactory",
    "CarFactory",
    "VehicleFactory",
]

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"


    
