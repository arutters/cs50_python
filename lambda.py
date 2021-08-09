people =[
    {"name": "Harry", "House": "Gryffindor"},
    {"name": "Cho", "House": "Ravenclaw"},
    {"name": "Draco", "House": "Slytherin"}
    ]

# def f(person):
#     return person["House"]
# people.sort(key=f)
#  or you can do it like this which is a candensed way of saying the same thing:::

people.sort(key=lambda person: person["name"])
print(people)


