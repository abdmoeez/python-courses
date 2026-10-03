import json

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User): #check if instance of a class
        return {'name': o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('object of type is not json serializable')

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age':o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)
 
userjson = json.dumps(user, cls=UserEncoder )
print(userjson)