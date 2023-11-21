from sensor import Sensor
from display import Display
import time


class Carpark:

    def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None, displays=None,
                 plates=None):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or []  # list to store detected car plates

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} bays."

    def register(self, new_object):  # allow the carpark to register sensors and displays
        if isinstance(new_object, Sensor):
            self.sensors.append(
                new_object)  # it checks whether this object is a type of sensor class, if yes, register to the list of sensors in carpark class
        elif isinstance(new_object, Display):
            self.displays.append(
                new_object)  # it checks whether this object is a type of display class, if yes, register to the list of displays in carpark class
        else:
            raise TypeError("Object must be a Sensor or Display.")

    def add_car(self, plate):
        # add car to carpark, record the plate number and update the displays in carpark class.
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        # remove car in carpark, remove the plate number and update the displays in carpark class.
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()

    # when the carpark needs to update the displays. It will iterate through the displays and call their update method.

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 37,
                "time": time.strftime("%Y/%m/%d, %H:%M:%S", time.localtime())}
        # update to the actual temperature
        for display in self.displays:
            display.update()

    @property
    # property - access like attribute
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))
    # max capacity minus current number of cars in carpark
    # if the number of plates exceeds the capacity, will return 0
