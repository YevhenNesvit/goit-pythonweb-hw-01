from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# Клас Car, що успадковується від Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.spec}: Двигун запущено")


# Клас Motorcycle, що успадковується від Vehicle
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} {self.spec}: Мотор заведено")


# Абстрактний клас VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


# Клас USVehicleFactory
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "(US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "(US Spec)")


# Клас EUVehicleFactory
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "(EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "(EU Spec)")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів для США
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

# Створення транспортних засобів для ЄС
vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("BMW", "R1250")
vehicle4.start_engine()
