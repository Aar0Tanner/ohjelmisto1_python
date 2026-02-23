class Car:

    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, amount):
        self.current_speed += amount

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

car1 = Car("ABC-123",142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print(car1.current_speed)

car1.accelerate(-200)

print(car1.current_speed)

