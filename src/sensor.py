class Sensor:

    def __init__(self, sensor_id, sensor_is_active, carpark):
        self.sensor_id = sensor_id
        self.sensor_is_active = sensor_is_active
        self.carpark = carpark

    def __str__(self):
        return f"Sensor id: {self.sensor_id} and status is {'Active' if self.sensor_is_active else 'Inactive'}"


class EntrySensor(Sensor):
    def detect_vehicle_entry(self):
        pass

class ExitSensor(Sensor):
    def detect_vehicle_exit(self):
        pass

