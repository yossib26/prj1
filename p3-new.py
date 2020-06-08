# myFile = open("C:/Yossi/DevOps/Lesson 3/readme.txt", "w")

myFile = open("C:/Yossi/DevOps/Lesson 3/readme.txt", "r+")
content = myFile.read()

# myFile = open("C:/Yossi/DevOps/Lesson 3/readme2.txt", "w")
myFile = open("C:/Yossi/DevOps/Lesson 3/readme2.txt", "r+")
content = myFile.write("AAAAAAAAAAAA")
# content = myFile.read()

myFile = open("C:/Yossi/DevOps/Lesson 3/readme2.txt", "r", encoding='utf-8')
content = myFile.read()
myFile.close()
print(content)

# error handling
print("-------------------------------------------")
try:
    f = open("c:\aaa.txt", "r")
    f.read()
except IOError:
    print("Error open file!!")

print("-------------------------------------------")
try:
    f = open("c:\aaa.txt", "r")
    f.read()
except IOError:
    print("Error open file!!")
finally:
    print("must execute !!")



