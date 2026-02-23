import random

class Car_class:

    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, amount_kmh):
        self.current_speed += amount_kmh

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def travel(self, hours):
        self.distance += hours * self.current_speed

cars = []

for i in range(1,11):
    maxspeed = random.randint(100, 200)
    carplate = f"ABC-{i}"
    cars.append(Car_class(carplate, maxspeed))

race_on = True
hours = 0

while race_on:

    hours += 1

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.travel(1)

        if car.distance >= 10000:
            race_on = False


for i in cars:
    print(i.__dict__)