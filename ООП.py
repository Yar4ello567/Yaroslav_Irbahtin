from abc import ABC, abstractmethod


class Vehicle(ABC):

    __static_field = "Static field"

    def __init__(self, brand, year):
        self.__brand: str = brand
        self._year: int = year

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        self.__brand = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def check_age(self) -> str:
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

    @engine_volume.setter
    def engine_volume(self, value: float) -> None:
        self._engine_volume = value

    @property
    def transmission(self) -> str:
        return self._transmission

    @transmission.setter
    def transmission(self, value: str) -> None:
        self._transmission = value

    def description(self) -> str:
        return (f"Легковой автомобиль {self.brand} {self.year} года,"
                f" объем двигателя {self.engine_volume} л,"
                f" трансмиссия {self.transmission}")

    def check_age(self) -> str:
        current_year = 2024
        age = current_year - self.year
        if age < 5:
            return f"{self.brand} - новый автомобиль."
        else:
            return f"{self.brand} - старый автомобиль."


class Truck(Vehicle):

    def __init__(self, brand: str, year: int, carrying_capacity: int, trailer_presence: bool) -> None:
        super().__init__(brand, year)
        self._carrying_capacity: int = carrying_capacity
        self._trailer_presence: bool = trailer_presence

    @property
    def carrying_capacity(self) -> int:
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, value: int) -> None:
        self._carrying_capacity = value

    @property
    def trailer_presence(self) -> bool:
        return self._trailer_presence

    @trailer_presence.setter
    def trailer_presence(self, value: bool) -> None:
        self._trailer_presence = value

    def description(self) -> str:
        if self.trailer_presence:
            return (f"Грузовой автомобиль {self.brand} {self.year} года,"
                    f" грузоподъемность {self.carrying_capacity} кг, с прицепом")
        else:
            return (f"Грузовой автомобиль {self.brand} {self.year} года,"
                    f" грузоподъемность {self.carrying_capacity} кг, без прицепа")

    def check_age(self) -> str:
        current_year = 2024
        age = current_year - self.year
        if age < 10:
            return f"{self.brand} - новый автомобиль."
        else:
            return f"{self.brand} - старый автомобиль."


class HybridCar(Car):

    def __init__(self, brand: str, year: int, engine_volume: float, transmission: str, battery_capacity: float) -> None:
        super().__init__(brand, year, engine_volume, transmission)
        self._battery_capacity: float = battery_capacity

    @property
    def battery_capacity(self) -> float:
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: float) -> None:
        self._battery_capacity = value

    def description(self) -> str:
        return (f"Гибридлный автомобиль {self.brand} {self.year} года,"
                f" объем двигателя {self.engine_volume} л,"
                f" трансмиссия {self.transmission},"
                f" емкость батареи {self.battery_capacity} кВт*ч")

    def check_age(self) -> str:
        current_year = 2024
        age = current_year - self.year
        if age < 8:
            return f"{self.brand} - новый автомобиль."
        else:
            return f"{self.brand} - старый автомобиль."


vehicles = [
    Car("Toyota", 2020, 2.0, "автоматическая"),
    Truck("MAN", 2011, 5000, True),
    HybridCar("Nissan", 2022, 1.2, "вариатор", 75)
]

for vehicle in vehicles:
    print(vehicle.description())
    print(vehicle.check_age())

print(Vehicle.get_static_field())
