from car_park import CarPark
from abc import ABC, abstractmethod
import random


# class Sensor is an abstract base class

class Sensor(ABC):

    def __init__(self, sensor_id, sensor_is_active, car_park):
        self.sensor_id = sensor_id
        self.sensor_is_active = sensor_is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor id: {self.sensor_id} and status is {'Active' if self.sensor_is_active else 'Inactive'}"

    def detect_vehicle(self):  # scan plate and notify car park
        plate = self._scan_plate()
        self.update_carpark(plate)

    @abstractmethod
    def update_carpark(self, plate):  # will be implemented in subclass EntrySensor and Exit Sensor
        pass

    def _scan_plate(self):  # underscore leading - private method - implement internal only within this class
        return 'FAKE-' + format(random.randint(0, 999), "03d")  # return a random plate


class EntrySensor(Sensor):
    def update_carpark(self, plate):
        self.car_park.add_car(plate)  # update car park, car enters car park
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_carpark(self, plate):
        self.car_park.remove_car(plate)  # update car park, car exits car park
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):  # override the _scan_plate method
        return random.choice(self.car_park.plates)
