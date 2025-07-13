class Car:
	def __init__(self, modelo: str, motor: str):
		self.modelo = modelo
		self.motor = motor

	def carPrototype(self):
		print(self)

	def showDetails(self):
		print(f"Car Modelo: {self.modelo}, Motor: {self.motor}")

	def carFactory(modelo: str, motor: str):
		return Car(modelo, motor)

carro1 = Car("Fusca", "V8")
carro1.showDetails()
carro2 = Car("Celta", "ABDD1233")
carro2.showDetails()

