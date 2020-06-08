
try:
    v = 10 / 0
    numb = int(input("enter num: "))
    print(numb)
except ZeroDivisionError as err:
    print(err)
    print("Divided by ZERO")
except ValueError:
    print("value Error")

