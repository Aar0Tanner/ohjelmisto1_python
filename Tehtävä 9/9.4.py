import random

class CarClass:

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

    def travel(self, travelhours):
        self.distance += travelhours * self.current_speed

cars = []

for i in range(1,11):
    maxspeed = random.randint(100, 200)
    carplate = f"ABC-{i}"
    cars.append(CarClass(carplate, maxspeed))

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

sorted_cars = sorted(cars, key=lambda c: c.distance, reverse=True)

for car in sorted_cars:
    print(f"[rekisterikilpi: {car.plate:}, maksiminopeus: {car.max_speed:}, nykyinen nopeus: {car.current_speed:}, kuljettu matka: {car.distance:}]")