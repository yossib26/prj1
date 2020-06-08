num1 = float(input("enetr first num: "))
op = input("enetr operator: ")
num2 = float(input("enetr second num: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid")

