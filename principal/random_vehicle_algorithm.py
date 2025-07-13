from factories.car_factory import CarFactory
from factories.bicycle_factory import BicycleFactory
import random

def randomVehicleAlgorithm():
    vehicle_type = random.choice(['car', 'bicycle'])
    if vehicle_type == 'car':
        return CarFactory().getVehicle('Sedan')
    else:
        return BicycleFactory().getVehicle('Mountain Bike')
