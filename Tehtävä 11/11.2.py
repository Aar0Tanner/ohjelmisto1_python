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


class ElectricCar(CarClass):
    def __init__(self, plate, max_speed, kwhcapacity):
        super().__init__(plate, max_speed)
        self.kwhcapacity = kwhcapacity


class GasCar(CarClass):
    def __init__(self, plate, max_speed, tanklitres):
        super().__init__(plate, max_speed)
        self.tanklitres = tanklitres


car1 = ElectricCar("ABC-123", 180, 52.5)
car2 = GasCar("ABC-123", 165, 32.3)

car1.accelerate(70)
car2.accelerate(80)

car1.travel(3)
car2.travel(3)

print(f"tällä hetkellä auto on kulkenut {car1.distance} km, ja nopeus on {car1.current_speed} km/h")
print(f"tällä hetkellä auto on kulkenut {car2.distance} km, ja nopeus on {car2.current_speed} km/h")
