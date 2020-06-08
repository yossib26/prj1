# A
print("-----------------  A  -------------------")
class Dog:

    def __init__(self, name = "No Name", age = -1):
        self.name = name
        self.age = age

    def main():
        print("----  main() ----")

    if __name__ == "__main__":
        main()

    def printName(self):
        return self.name

dog1 = Dog("Raxi", 12)
print(dog1.printName())

# B
print("-----------------  B  XXXXXXXXXXXXXXXXXXX  -------------------")
class ConstructedShark:

    def __init__(self, age):
        self.age = age

    def main():
        # stevie = ConstructedShark(3)
        # print(stevie.age)
        print("------- main ------------")

    if __name__ == "__main__":
        main()

c = ConstructedShark(10)


# C
print("-----------------  C XXXXXXXXXXXXXXXXXXXXXXXXXx  -------------------")
class Car:

    def __init__(self, model):
        self.model = model

    @staticmethod
    def start():
        print("Start Engine !!!!!!!!!!!!")

    def main():
        print("----------  main -------------")


    if __name__ == "__main__":
        main()

car1 = Car("Toyota")
# Car.start()


# D
print("-----------------  D  -------------------")
class Dog:

    def __init__(self, name = "No Name", age = -1):
        self.name = name
        self.age = age

class Husky(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)

    def howl(self):
        print("ahooooo")

    # if __name__ == "__main__":
    #     Hus = Husky("Lassie", 11)

dog1 = Husky("Lassie", 15)
dog1.howl()


# E
print("-----------------  E  XXXXXXXXXXXXXXXXXXXXX -------------------")

# class BlackHuskey(Husky):
#
#     def __init__(self, name, age):
#         super().__init__(name, age)

    # def return_color(self):
    #     return "Black"

# dog2 = BlackHuskey()
# print(dog2.return_color())


# F
print("-----------------  F  XXXXXXXXXXXXXXXXXX  -------------------")

class DogF:

    @staticmethod
    def bark(self):
        print(123)

    # if __name__ == "__main__":
    #     DogF.bark()

dog3 = DogF()


# G
print("-----------------  G  -------------------")

arrNum = (3, 4, 5)
for a in arrNum:
    print(a)

arrDogs = [Dog("Max", 11), Dog("Lassie", 12), Dog("Jo", 13)]
for a in arrDogs:
    print("Dog Name: " + a.name + " is " + str(a.age) + " years old!")


# H
print("-----------------  H  -------------------")
