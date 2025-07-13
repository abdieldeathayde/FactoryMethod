
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def pickUp(self, customerName: str):
        pass

    @abstractmethod
    def stop(self):
        pass
    