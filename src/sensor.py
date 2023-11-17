class Sensor:

    def __init__(self, sensor_id, sensor_is_active=False, carpark=None):
        self.sensor_id = sensor_id
        self.sensor_is_active = sensor_is_active
        self.carpark = carpark

    def __str__(self):
        return f"Sensor id: {self.sensor_id} and status is {self.sensor_is_active}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
