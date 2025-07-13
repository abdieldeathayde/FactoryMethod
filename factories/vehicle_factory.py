import abc

from vehicle import Car
from vehicle import Vehicle

class VehicleFactory(abc.ABC):
    ## facotry method
    @abc.abstractmethod
    def getVehicle(self, vehicleName: str):
        return Vehicle
    
    def pickUp(self, customerName: str, vehicleName: str):
        vehicle = self.getVehicle(vehicleName)
        vehicle.pickUp(customerName)
        car = self.getVehicle(vehicleName)
        car.pickUp(customerName)
        return car
        
       ## if vehicleName == "Fusca":
         ##   return Car('Fusca')
   
