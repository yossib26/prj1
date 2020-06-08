import json1
people_string = '''
{
    "people": [
        {
        "name": "john smith",
        "phone": "038484848",
        "emails": "aaaa@gmail.com", "bbbbbb@gmail.com"]
        },
        {
        "name": "john2 smith",
        "phone": "038484848",
        "emails": "aaaa@gmail.com", "bbbbbb@gmail.com"]
        }
    ]
}
'''
data = json1.loads(people_string)



'''
data = json.loads(people_string)
print(type(data))
for person in data['people']:
    print(person)


json_file = open("json.txt", "r", encoding="utf-8")

print(json_file.readlines())
print(json_file.readline())

data = json_file.readlines()
print(type(data))




json_file.close()
'''