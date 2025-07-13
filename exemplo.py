from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def sayHi(self):
        pass

class ConcreteProduct(Product):
    def sayHi(self):
        print("Hi")

class Creator(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass

    def createAndShow(self):
        product = self.factoryMethod()
        print(product)

class ConcreteCreator(Creator):
    def factoryMethod(self):
        return ConcreteProduct()

creator = ConcreteCreator()
product = creator.factoryMethod()
product.sayHi()
creator.createAndShow()