people=[
    {"name":"Harry","age":35},
    {"name":"Jack","age":20},
    {"name":"Lin","age":22}
]


people.sort(key=lambda person: person['name'])

print(people)