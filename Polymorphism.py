"""
The word "polymorphism" means "many forms", and in programming it refers to
methods/functions/operators with the same name that can be executed on many objects or classes.

"""

x = "Hello World!"

print(len(x))
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

