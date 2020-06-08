

def max_str(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

# call function
print(max_str(4, 15 , 9))

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

# call function
print(max_num(4, 15 , 9))


is_male = True
is_tall = False

if is_male and is_tall:
    print("male")
    print("222")
elif is_male and not is_tall:
    print("Else If")
else:
    print("DDDDD")
