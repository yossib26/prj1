i = 1
while i <= 10:
 #   print(i)
    i +=1

#print("end loop")

secret = "giraffe"
guess = ""
res = False
c = 0
t = 3

while guess != secret and not(res):
    if c < t:
        guess = input("Enter Guess: ")
        c += 1
    else:
        res = True

if res:
    print("Our Of Guesses, You Loose")
else:
    print("You Win!!!!!1")



