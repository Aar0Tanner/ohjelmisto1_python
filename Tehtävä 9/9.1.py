class Car:
    def __init__(self, plate, max_speed):
        self.plate = plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

car1 = Car("ABC-123",142)

print(car1.__dict__)

