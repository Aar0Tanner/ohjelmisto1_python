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

class Race:

    def __init__(self, name, length, vehicles):
        self.name = name
        self.length = length
        self.vehicles =vehicles

    def raceover(self):
        for c in self.vehicles:
            if c.distance >= self.length:
                return True
        return False

    def hourpasses(self):
        for c in self.vehicles:
            speed_change = random.randint(-10, 15)
            c.accelerate(speed_change)
            c.travel(1)


    def printstats(self):
        sorted_vehicles = sorted(self.vehicles, key=lambda c: c.distance, reverse=True)
        for c in sorted_vehicles:
            print(f"rekisterikilpi: {c.plate:}, maksiminopeus: {c.max_speed:}, nykyinen nopeus: {c.current_speed:}, kuljettu matka: {c.distance:}")


cars = []

for i in range(1,11):
    maxspeed = random.randint(100, 200)
    carplate = f"ABC-{i}"
    cars.append(CarClass(carplate, maxspeed))

romuralli = Race("Suuri romuralli", 8000, cars)

hours = 0
while not romuralli.raceover():
    romuralli.hourpasses()
    hours += 1

    if hours % 10 == 0:
        print(f"Tunti {hours}")
        romuralli.printstats()

print(f"\nKilpailu päättyi! Aikaa kului {hours} tuntia.")
romuralli.printstats()