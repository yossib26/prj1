def translate(phrase):
    translation = ""
    for l in phrase:
        if l in "AEIOUaeiou":
            if l.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + l
    return translation


print(translate("AAfidsjfhdsojhfkAA"))
#print(translate("AAfidsjfhdsojhfkAA"))
print(translate("Aodubej"))



# comments
'''
test comments
test comments
test comments

'''