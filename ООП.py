from abc import ABC, abstractmethod


class Vehicle(ABC):

    __static_field = "Static field"

    def __init__(self, brand, year):
        self.__brand: str = brand
        self._year: int = year

    @property
    def brand(self) -> str:
        return self.__brand

    @property
    def year(self) -> int:
        return self._year

    @abstractmethod
    def description(self) -> str:
        pass

    @staticmethod
    def get_static_field() -> str:
        return Vehicle.__static_field


class Car(Vehicle):

    def __init__(self, brand: str, year: int, engine_volume: float, transmission: str) -> None:
        super().__init__(brand, year)
        self._engine_volume: float = engine_volume
        self._transmission: str = transmission

    @property
    def engine_volume(self) -> float:
        return self._engine_volume

    @property
    def transmission(self) -> str:
        return self._transmission

    def description(self) -> str:
        return f"Легковой автомобиль {self.brand} {self.year} года, объем двигателя {self.engine_volume} л, трансмиссия {self.transmission}"


class Truck(Vehicle):

    def __init__(self, brand: str, year: int, carrying_capacity: int, trailer_presence: bool) -> None:
        super().__init__(brand, year)
        self._carrying_capacity: int = carrying_capacity
        self._trailer_presence: bool = trailer_presence

    @property
    def carrying_capacity(self) -> int:
        return self._carrying_capacity

    @property
    def trailer_presence(self) -> bool:
        return self._trailer_presence

    def description(self) -> str:
        if self.trailer_presence:
            return f"Грузовой автомобиль {self.brand} {self.year} года, грузоподъемность {self.carrying_capacity} кг, с прицепом"
        else:
            return f"Грузовой автомобиль {self.brand} {self.year} года, грузоподъемность {self.carrying_capacity} кг, без прицепа"


class HybridCar(Car):

    def __init__(self, brand: str, year: int, engine_volume: float, transmission: str, battery_capacity: float) -> None:
        super().__init__(brand, year, engine_volume, transmission)
        self._battery_capacity: float = battery_capacity

    @property
    def battery_capacity(self) -> float:
        return self._battery_capacity

    def description(self) -> str:
        return f"Гибридлный автомобиль {self.brand} {self.year} года, объем двигателя {self.engine_volume} л, трансмиссия {self.transmission}, емкость батареи {self.battery_capacity} кВт*ч"


vehicles = [
    Car("Toyota", 2020, 2.0, "automatic"),
    Truck("MAN", 2015, 5000, True),
    HybridCar("Nissan", 2022, 2.5, "automatic", 75)
]

for vehicle in vehicles:
    print(vehicle.description())

print(Vehicle.get_static_field())
