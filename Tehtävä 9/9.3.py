class Car:

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

car1 = Car("ABC-123",142)

car1.accelerate(30)
car1.accelerate(70)

print(car1.current_speed)

car1.travel(4)

print(f"tällä hetkellä auto on kulkenut {car1.distance} km, ja nopeus on {car1.current_speed} km/h")
