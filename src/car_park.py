from sensor import Sensor
from display import Display
import time
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
import json


class CarPark:

    def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None,
                 displays=None, plates=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or []  # list to store detected car plates
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)


    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):  # allow the car park to register sensors and displays
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)  # register to sensor list if it is sensor object
        elif isinstance(component, Display):
            self.displays.append(component)  # register to display list if it is display object

    def add_car(self, plate):
        # add car to car park, record the plate number and update the displays
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        # remove car in car park, remove the plate number and update the displays
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "exited")
        else:
            raise ValueError(f"Car plate {plate} does not exist.")

    # when the car park needs to update the displays. It will iterate through the displays and call their update method.

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 37,
                "time": time.strftime("%Y/%m/%d, %H:%M:%S", time.localtime())}
        # update to the actual temperature
        for display in self.displays:
            display.update(data)

    @property
    # property - access like attribute
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))
    # max capacity minus current number of cars in car_park
    # if the number of plates exceeds the capacity, will return 0


    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")


