from factories import VehicleFactory
from vehicle import Vehicle

class BicycleFactory(VehicleFactory):
    def getVehicle(self, vehicleName: str):
        return BicycleFactory(vehicleName)
    
  