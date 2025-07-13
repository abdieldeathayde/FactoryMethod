from factories import VehicleFactory
from vehicle import Car
from vehicle import Vehicle
from abc import abstractmethod

class CarFactory(VehicleFactory):
    @abstractmethod
    def getVehicle(self, vehicleName: str):
        return Car(vehicleName)
    
    def pickUp(self, customerName: str, vehicleName: str):
        car = self.getVehicle(vehicleName)
        car.pickUp(customerName)
        return car
    
    """
        vehicle = self.getVehicle(vehicleName)
        vehicle.pickUp(customerName)
        def __init__(self, car_class):
        self.car_class = car_class

    def create_car(self, model):
        return self.car_class(model)
    """
