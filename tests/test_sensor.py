import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = EntrySensor(sensor_id=2, sensor_is_active=True, car_park=CarPark("123 Example Street", 100))

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, EntrySensor)
        self.assertEqual(self.sensor.sensor_id, 2)
        self.assertEqual(self.sensor.sensor_is_active, True)
        self.assertIsInstance(self.sensor.car_park, CarPark)

    # def test_update_car_park(self):
    #     self.sensor.update_car_park("FAKE-001")
    #     self.assertEqual(self.sensor.update_car_park, second="FAKE-001")

if __name__ == "__main__":
    unittest.main()