emp_file = open("emep.txt", "r")
print(emp_file.readable())

if emp_file.readable():
    print("read")

    # print(emp_file.read())
    '''
    print(emp_file.readline())
    print(emp_file.readline())
    print(emp_file.readline())
    print(emp_file.readline())
    print(emp_file.readline())
    '''

    '''
    for e in emp_file.readlines():
        print(e)
    '''

emp_file.close()

emp2_file = open("emep.txt", "a")
emp2_file.write("\n5555555555555")
emp2_file.write("\nkllllllll")

emp2_file.close()

# overwrite
emp2_file = open("emep1.txt", "w")
emp2_file.write("\n5555555555555")
emp2_file.write("\nkllllllll")
emp2_file.close()

# overwrite
emp2_file = open("index.html", "w")
emp2_file.write("<p>this is html page</p>")
emp2_file.write("\nkllllllll")
emp2_file.close()


