# polymorphism.py

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
  	print("Move")

class Car(Vehicle):
  	pass

class Boat(Vehicle):
  	def move(self):
  		print("Sail!")

class Plane(Vehicle):
  	def move(self):
  		print("Fly!")


car1 = Car("Mazda", "CX-5")
boat1 = Boat("Titanic", "007")
plane1 = Plane("Boing", 777)


for x in (car1, boat1, plane1):
	print(x.brand)
	print(x.model)
	x.move()