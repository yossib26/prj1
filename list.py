lucky = [4, 52, 23, 12]
num = [4, 5, 23, 12]
friends = ["gggg", "bbbb", "cccccc", "bbbb", "dddddd"]


friends2 = friends.copy()
print(friends2)

lucky.reverse()
print(lucky)

friends.sort()
lucky.sort()


print(friends.count("bbbb"))

print(friends.index("cccccc"))


print(friends)

friends.remove("bbbb")

friends.insert(1, "KELLY")

num.clear()
print(num)

friends.append("Creed")
print(friends)

friends.extend(lucky)



print(lucky)

print(friends[2])
print(friends)

friends[0] = "YYYY"

print(friends[1:])
print(friends[2:])

for x in friends:
    print(x)
