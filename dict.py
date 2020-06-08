monthConv = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mqr": "Mars",
    "Apr": "April"
}

print(monthConv["Jan"])
print(monthConv.get("Jan1", "NON VALUE"))
print(monthConv.get("Apr", "NON VALUE"))

