#1
print("Hello world!")

#2
x = 10
if x == 1:
    print("x = 1")

#3
myInt = 7
print(myInt)
my_integer = 9
print(my_integer)

#4
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#5
mystring = 'he \n llo'
print(mystring)
mystring = "hello"
print(mystring)

#6
one = 1
two = 2
three = one + two
print(three)

one = "one"
two = "two"
three = one + " " + two
print(three)

one = 4
two = "two"
three = one * two
print(three)

one = 4
two = "two"
three = str(one) + str(two)
print(three)

#exerc
first = 7
second = 44.3
res = float(first) + second
print(res)
res = float(first) * second
print(res)
res = second / first
print(res)

mystring = "hello"
mystring2 = "world"
myfloat = 10.0
myint = 30
print("String: %s" % mystring)
print("String: %s %s" % (mystring, mystring2))
print("Float: %f" % myfloat)
print("String: %d" % myint)
print("Float: %.2f" % myfloat)


a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b= 8
print(str(a) + " " + str(b) + "  " + str(c))

str1 = 'hello "world"'
str2 = "hello 'world'"
str3 = "hel \n \t lo \"world\""
print(str1)
print(str2)
print(str3)


# in operator
name = "john2"
if name in ["dffds", "john", "david"]:
    print("your name is john")
else:
    print("your name is DAVID")


# is operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
print(isinstance(x, list))

mystring = "hello"
myfloat = 3.5
myint = 12
if mystring == "hello":
    print("String:  %s" % mystring)
if isinstance(myfloat, float):
    print("Float:  %f" % myfloat)
if isinstance(myint, int):
    print("Integer:  %d" % myint)

# mod operator
x = 9
res = x % 5
print(res)
squared = 7 ** 2
cubed= 2 ** 3
print(squared)
print(cubed)

l1 = [2, 3, 4, 5]
l2 = [5, 6, 7, 9]
print(l1+l2)
print(l1 * 3)


x = object()
y = object()
x_list = [x, x, x]
y_list = [y]
big_list = []
print("x_list : %s" % len(x_list))
print("y_list : %d" % len(y_list))
print("big_list : %d" % len(big_list))

if x_list.count(x) == 3 or y_list.count(x) == 10:
    print("Almost there ..")
if big_list.count(x) == 10:
    print("Well Done!")

# string formatting
name = "john"
age = 99
mylist = [4, 4, 5, 6, 8]
print("Hello: %s" % name)
print("Hello: %s -- %s old" % (name, age))
print("My Numbers: %s" % mylist)

#exerc
data = ("John", "Doe", 53.44)
# format_string = "Hello"
format_string = "Hello %s %s, your balance is $%s"
print(format_string % data)


s1 = "hello"
s2 = "world"
s3 = s1 + s2
print(s1 + s2)
print(len(s2))
print(s3.index("w"))
print(s3.count("l"))
print(s3[4:7])
print(s3[1:4:2])

# strrev
print(s3[::-1])

print(s3.upper())
print(s3.lower())
s3 = "Hello World"
print(s3.startswith("Hello"))
print(s3.endswith("dsadas"))
arrs3 = s3.split(" ")
print(arrs3)

s = "Hey there! what should this string be?"
print("Length of S: %s" % len(s))
print("the first occur of a is %d" % s.index("a"))
print("num of occurs of a is %d" % s.count("a"))
print("the first 5 characters is %s" % s[:5])
print("the next 5 characters is %s" % s[5:10])
print("the 12 character is %s" % s[12])
print("the last 5 characters is %s" % s[-5:])
print("the characters with odd index is %s" % s[1::2])
print("the string uppercase is %s" % s.upper())
print("the string lowercase is %s" % s.lower())
if s.startswith("str"):
    print("starts with str")
if s.endswith("str"):
    print("ends with str")
print(s.split(" "))


#loops
primes = [2, 4, 6, 8]
for prime in primes:
    print(prime)

for p in range(0, 10):
    print(p)

for p in range(6, 9 ):
    print(p)


for p in range(1, 9 , 3):
    print(p)

count = 0
while count < 6:
    print(count)
    count += 1

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)


count = 0
while count <= 5:
    print(count)
    count += 1
else:
    print("Exit Loop")

print("-------------------------------------------------------")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break


print("-------------------------------------------------------")
for number in numbers:

    if number == 237:
        break

    if number % 2 == 1:
        continue
    print(number)


pbook = {}
pbook["a"] = 111111
pbook["b"] = 222222
pbook["c"] = 333333
print(pbook)
# pbook = {"aaa" : 111111, "bbb" : 222222222}
for name, phone in pbook.items():
    print(name + " " + str(phone))
    print("my details %s %s" % (name, phone))

pbook.pop("c")
del pbook["b"]

for name, phone in pbook.items():
    print(name + " " + str(phone))
    print("my details %s %s" % (name, phone))



print("---------------------------------------------------")
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781 }

phonebook.update({"Jake" : 938273443})
phonebook.pop("Jill")
for name, phone in phonebook.items():
    print("my details %s %s" % (name, phone))

print("---------------------------------------------------")
sentence = "the quick brown fox jumps over the lazy dog"
srrw = sentence.split(" ")
word_length = []
for s in srrw:
    word_length.append(len(s))
print(srrw)
print(word_length)

print("---------------------------------------------------")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for n in numbers:
    if int(n) >= 0 and isinstance(n, float):
        print(int(n))

# set
s = set("my name is Eric and Eric is my name".split())
print(s)
a = set(["Jake", "Jake", "John", "Eric"])
print(a)

#  duplicte
a = set(["Jake", "John", "Eric"])
b = set(["Jake", "Jill", "Eric"])
print(a.intersection(b))
print(b.intersection(a))


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a.difference(b))
print(b.difference(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.union(b))

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
A = set(a)
B = set(b)
print(A.difference(B))













