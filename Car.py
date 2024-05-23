# Car.py



class Car:
    def __init__(self, color, mileage, typeCar):
        self.color = color
        self.mileage = mileage
        self.type = typeCar
    
    def __str__(self):
        return f"The {self.color} {self.type} car has {self.mileage:,} miles"

    @classmethod
    def sound(cls, sound):
        return f"The car makes {sound}"

    @staticmethod
    def stop(brk):
        return f"Out of control. please {brk}"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value.upper()


blue = Car("Blue", 20000000, "SUV")
red = Car("Red", 30000, "Sedan")
print(red.sound("whoom"))

print(blue)
print(red)

print(Car.sound("Drummm"))
print(Car.stop("break"))