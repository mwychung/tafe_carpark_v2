from sensor import Sensor
from display import Display

class Carpark:

    def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None, displays=None, plates=None):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or [] # list to store detected car plates

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} bays."

    def register(self, object):
        #allow the carpark to register sensors and displays
        if isinstance(object, Sensor):
            self.sensors.append(object)
            # it checks whether this object is a type of sensor class, if yes, register to the list of sensors in carpark class
        elif isinstance(object, Display):
            self.displays.append(object)
            # it checks whether this object is a type of display class, if yes, register to the list of displays in carpark class
        else:
            raise TypeError("Object must be a Sensor or Display.")

    def add_car(self, plate):
        #add car to carpark, record the plate number and update the displays in carpark class.
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        #remove car in carpark, remove the plate number and update the displays in carpark class.
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()

    def update_displays(self):
        #when the carpark needs to update the displays. It will iterate through the displays and call their update method.
        for display in self.displays:
            display.update()



