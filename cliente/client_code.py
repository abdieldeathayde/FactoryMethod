from principal import randomVehicleAlgorithm
from utilitarios import VehicleFactory
from vehicle import Vehicle
from factories import BicycleFactory
from vehicle import CarFactory  

carFactory = CarFactory()
customerName = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Fernanda', 'Carlos', 'Juliana', 'Roberto', 'Sofia']

for i in range(10):
    vehicle = randomVehicleAlgorithm()
    name = customerName[i % len(customerName)]
    vehicle.pickUp(name)
    vehicle.stop()
    newCar = carFactory.pickUp(f"name, 'NOVO CARRO - ${vehicle.name}'")
    newCar.stop()
    print(f"Carro {newCar.name} foi retirado por {name}.")
    print('---')
    
    
"""

vehicle = randomVehicleAlgorithm()
vehicle.start_engine()


car_factory = CarFactory()
fusca = car_factory.getVehicle('Fusca')
fusca.pickUp('João')
fusca.stop()


from vehicle import Car

ecosport = Car('Ecosport')
ecosport.pickUp('Joana')
ecosport.stop()


"""