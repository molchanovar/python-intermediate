import json 

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
# """ will print: 
# {
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "name": "John",
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }
# """

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# with open('person.json', 'r') as file:
#     person = json.loads(personJSON)
#     print(person)