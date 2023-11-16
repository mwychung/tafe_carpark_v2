class Carpark:

    def __init__(self, location="Unknown", capacity=0, current_vehicle_count=0, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.current_vehicle_count = current_vehicle_count
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Carpark at {self.location}, with {self.capacity} bays."

# testing:
# create an object
# carpark = Carpark(location="188 Ford Street", capacity=50)
# print(carpark)

