def cube(x):
    x*x
    print(x*x)
    return x*x*x


res = cube(4)
print(res)
print(cube(5))


def say_hi():
    print("Hello USer")
    return 1

print(say_hi())


def func1(name, age):
    print("FUNCS")
    print(name)
    print(str(age))


func1("aaaaa", 55)

print("TOP")
say_hi()
print("bottom")