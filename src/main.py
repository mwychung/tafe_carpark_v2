from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
moondalup_car_park = CarPark(location="moondalup", capacity=100, log_file="moondalup.txt")

# create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(sensor_id=1, sensor_is_active=True, car_park=moondalup_car_park)

# create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(sensor_id=2, sensor_is_active=True, car_park=moondalup_car_park)

# create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=moondalup_car_park)

# drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for car_entry_count in range(10):
    entry_sensor.detect_vehicle()

# drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for car_exit_count in range(2):
    exit_sensor.detect_vehicle()


