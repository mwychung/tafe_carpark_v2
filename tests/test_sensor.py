import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(sensor_id=2, sensor_is_active=True, car_park=self.car_park)
        self.exit_sensor = ExitSensor(sensor_id=3, sensor_is_active=True, car_park=self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.sensor_id, 2)
        self.assertEqual(self.entry_sensor.sensor_is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_entry_sensor_detect_vehicle_add_car_to_car_park(self):
        #test detect_vehicle adds car to the car park
        self.entry_sensor.detect_vehicle()
        self.assertIn(self.entry_sensor.car_park.plates[0], self.entry_sensor.car_park.plates)

    def test_entry_sensor_detect_vehicle_car_park_capacity(self):
        #test detect_vehicle updates the car park capacity
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.entry_sensor.car_park.available_bays, 99)

    def test_exit_sensor_remove_car(self):
        #test if the exit sensor updates the car park capacity
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 100)


if __name__ == "__main__":
    unittest.main()