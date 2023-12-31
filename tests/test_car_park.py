import unittest
from car_park import CarPark
from pathlib import Path
import json



class TestCarPark(unittest.TestCase):

    log_file = "log.txt"

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100, log_file=self.log_file)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        #new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path(self.log_file).exists())


    def tearDown(self):
        Path(self.log_file).unlink(missing_ok=True)

    # inside the TestCarPark class
    def test_car_logged_when_entering(self):
        self.car_park.add_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        # the last time contains {plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
        # example: NEW-001 entered at 2023-12-01 23:47:35
        self.assertIn("NEW-001", last_line) # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line
        # put plate as member and last_line as container
        # check whether substring plate and action are present in last_line

    def test_car_logged_when_exiting(self):
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.car_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_park_initialized_with_write_config_file_and_from_config_file(self):
        config_file_path = "sample_config.json"
        self.car_park.write_config(config_file=Path(config_file_path))

        # from_config (@staticmethod) belongs to CarPark class, not object of class
        # create new object from config file
        new_car_park = CarPark.from_config(config_file=Path(config_file_path))

        self.assertIsInstance(new_car_park, CarPark)
        self.assertEqual(new_car_park.location, "123 Example Street")
        self.assertEqual(new_car_park.capacity, 100)
        self.assertEqual(new_car_park.log_file, Path("log.txt"))


if __name__ == "__main__":
    unittest.main()
