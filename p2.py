import os
print(os.path.abspath(__file__))

isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"

if a < b:
    print('%d is lower then %0.2f' % (a, b))

if strOne != strThree:
    print("Strings are different")
else:
    print("String are equals")

if strOne != strThree and a < b:
    print("a is different from b")

if strOne != strThree or not a > b:
    print("a is different from b")

if a ==4:
    print(1)
elif a < 2.5:
    print(2)
else:
    print(3)

print(a == 5)

name = "john"
if name in ("john", "david"):
    print("we found john")
else:
    print("not found")

# print(strOne.lower() + "\n" + strThree.upper())

x = [1, 2, 3]
y = [1, 2, 3]
# memory address
if x is y:
    print("x is y")
else:
    print("x is not y")

if type(x) is list:
    print("x is LIST")

print(not False)
print((not False) == (False))

number = 10
second_number = 10
first_array = []
second_array = [5, 6, 7]

if number > 15:
    print(1)

# def main():
#     print("DDDDDDDD")
#
# if __name__ == "__main__":
#     main()

if first_array:
    print("first array")

if len(second_array) == 3:
    print("second array")

print(second_array.__len__())

if len(first_array) + len(second_array) == 5:
    print("len of two arrays")

# loops
for e in second_array:
    print(str(e))

for e in range(len(second_array)):
    print(e)

a = list(range(10))
print(a)

a = list(range(2, 6))
print(a)

a = list(range(10, -1, -2))
print(a)


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
print("------------------------------------------")

for p in range(3, 8, 2):
    print(p)

print("------------------------------------------")
for a in range(len(second_array)):
    print(second_array[a])


print("------------------------------------------")
count = 0
sLength = len(second_array)
while count < sLength:
    print(second_array[count])
    count += 1


#  break, continue, pass
if a == 4:
    pass
else:
    print("conitnue")

print("----------------- 7 BOOM -----------------------")
for b in range(1, 100, 1):
    if b % 7 == 0:
        print(b, end=' ')
        print("mysql%03d" % (b + 1))
    if b % 1 == b and b % b == 0:
        break

print("---------------------------------------------------")

count = 0
while count < 5:
    print(count, end=' ')
    count += 1
    # if count < 2:
    #     break
else:
    print("count values reached %d" % count)

print("-----------------------------------------")
for i in range(5):
    pass
else:
    print("everything is OK")



print("-----------------------------------")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]
for num in numbers:
    if num % 2 == 0:
        print(num, end=' ')
    elif num == 237:
        break

print("---------------------------------")
for num in numbers:
    if num == 237:
        break
    elif num % 2 == 0:
        print(num, end=' ')


print("--------------  while true  ---------------------------")
# myinput = str(input("Enter Num:"))
# while True:
#     print("WOW!")
#     if myinput == "q":
#        break
#     myinput = str(input("Enter Num:"))

print("----------------  Module ------------------")
# import fibo
from fibo import fib
# fibo.fib(5)
fib(8)

print("-----------------  funcs --------------------")


def print_hello():
    print("Hello World")

for i in range(3):
    print_hello()

# a between 1 to 10
if 1 < a < 10:
    print_hello()


def calc_square(num = 10):
    # print("Square of %d is %d" % (num, num * num))
    res = num * num
    return res


for i in range(1, 3, 1):
    a = calc_square(i)
    print("Square of %d is %d" % (i, a))

print(calc_square())


def print_name(name = ''):
    print("Hello %s" % name)


# myinput = str(input("Enter Num:"))
# while True:
#     if myinput == "haim":
#         break
#     print_name(myinput)
#     myinput = str(input("Enter Name:"))


#  ---------------------  Variables --------------------------------

def square(num = 10):
    # print("Square of %d is %d" % (num, num * num))
    res = num * num
    fac_res = 1
    for i in range(1, num + 1):
        fac_res = fac_res * i
    # retun tuple
    return (res, fac_res)


# myArr = ["aa", 33, True]
# for i in myArr:
#     print(i)

a = 4
# return tuple
print(str(square(a)[0]) + "   " + str(square(a)[1]))

# -------------------  Dictionary  ------------------------------------

myDict = {"name": "aviel",
          "age": 28,
          "hobbies": ["Skiing","Cooking"],
          "children": None}

myDict["age"] = 30
print(myDict["name"])
print(myDict["age"])
print(myDict["hobbies"])
for i in myDict:
    print(i)

print(myDict.keys())

myDict2 = myDict.copy()
print(myDict2.keys())


