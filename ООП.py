from abc import ABC, abstractmethod

class Vehicle(ABC):

    static_field = "Static field"

    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    @property
    def brand(self):
        return self._brand

    @property
    def year(self):
        return self._year

    @abstractmethod
    def description(self):
        pass

    @staticmethod
    def get_static_field():
        return Vehicle.static_field

class Car(Vehicle):

    def __init__(self, brand, year, engine_volume, transmission):
        super().__init__(brand, year)
        self._engine_volume = engine_volume
        self._transmission = transmission

    @property
    def engine_volume(self):
        return self._engine_volume

    @property
    def transmission(self):
        return self._transmission

    def description(self):
        return f"Легковой автомобиль {self.brand} {self.year} года, объем двигателя {self.engine_volume} л, трансмиссия {self.transmission}"

class Truck(Vehicle):

    def __init__(self, brand, year, carrying_capacity, trailer_presence):
        super().__init__(brand, year)
        self._carrying_capacity = carrying_capacity
        self._trailer_presence = trailer_presence

    @property
    def carrying_capacity(self):
        return self._carrying_capacity

    @property
    def trailer_presence(self):
        return self._trailer_presence

    def description(self):
        if self.trailer_presence:
            return f"Грузовой автомобиль {self.brand} {self.year} года, грузоподъемность {self.carrying_capacity} кг, с прицепом"
        else:
            return f"Грузовой автомобиль {self.brand} {self.year} года, грузоподъемность {self.carrying_capacity} кг, без прицепа"

class HybridCar(Car):

    def __init__(self, brand, year, engine_volume, transmission, battery_capacity):
        super().__init__(brand, year, engine_volume, transmission)
        self._battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self._battery_capacity

    def description(self):
        return f"Гибридлный автомобиль {self.brand} {self.year} года, объем двигателя {self.engine_volume} л, трансмиссия {self.transmission}, емкость батареи {self.battery_capacity} кВт*ч"

car = Car("Toyota", 2020, 2.0, "automatic")
print(car.description())

truck = Truck("MAN", 2015, 5000, True)
print(truck.description())

electric_car = HybridCar("Tesla", 2022, 2.5, "automatic", 75)
print(electric_car.description())

print(Vehicle.get_static_field())
