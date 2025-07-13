import Vehicle

class Bicycle(Vehicle):
    def __init__(self, name: str):
        self.name = name
    
    def pickUp(self, CustomerName: str):
        print(f"{self.name} está buscando {CustomerName}")
    
    def stop(self):
        print(f"{self.name} parou")