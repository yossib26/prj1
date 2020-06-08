class Dog:
    isMamma = True

    def __init__(self, name = "No Name", age = -1):
        self.name = name
        self.age = age

    def bark(self):
        print("whoof! whoof! whoof! whoof!" + self.name)


Lassie = Dog("Lassie", 12)
Lassie.bark()

# Dog Snoopy = Dog("Snoopy", 15)

print("---------------------------------------")

class Rectangle:

    def __init__(self, rLength = 0, rWidth = 0):
        self.length = rLength
        self.width = rWidth

    def calcArea(self):
        return self.length * self.width

Rec = Rectangle(28, 44)
print("Recatcglw Area = " + str(Rec.calcArea()))

print("---------------------------------------")
#  pow
class Pow:

    def __init__(self, pBase = 0, pPow = 0):
        self.pBase = pBase
        self.pPow = pPow

    def calcPow(self):
        resPow = self.pBase
        for p in range(self.pPow-1):
            resPow = resPow * self.pBase
            print(resPow)
        return resPow

p = Pow(8, 3)
print("Pow Result = " + str(p.calcPow()))


print("--------------  Inherite 2  -------------------------")
class Dog:

    dSpec = ""

    def __init__(self, name = "No Name", age = -1):
        self.name = name
        self.age = age

    def setSpecies(self, species):
        self.dSpec = species

    def speak(self):
        return "Burk! Burk! Burk! Burk!"

    def description(self):
        return "Dog name is : " + self.name + " " + str(self.age)


class RussleTerrir(Dog):

    def __init__(self):
        super().__init__("RusselTerrier", 15)

    def speak(self):
        return "RussleTerrir Bark !!!"

class Bulldog(Dog):

    def __init__(self):
        super().__init__("Bulldog", 25)

    def speak(self):
        return "Bulldog Bark !!!"

rt = RussleTerrir()
rt.setSpecies("species")
print(rt.description())
print(rt.speak())
bd = Bulldog()
print(bd.description())
print(bd.speak())
# print(super(rt.speak()))


print("--------------  Inherite static method  -------------------------")
import math
class my_math_utils:

    Pi1 = 3.14

    @staticmethod
    def calcCircleArea(radius):
        return math.pi * radius * radius

print(my_math_utils.calcCircleArea(3))


print("--------------  packages  -------------------------")
import datetime
print(datetime.datetime.now())