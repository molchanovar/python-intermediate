import json
from typing import Any 

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    

# userJSON = json.dumps(user, default=encode_user)
# userJSON = json.dumps(user, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)
# {"name": "Max", "age": 27, "User": true}

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user)) # <class '__main__.User'>
print(user.name) # Max
print(user) # <__main__.User object at 0x1006a3890>
# {'name': 'Max', 'age': 27, 'User': True}