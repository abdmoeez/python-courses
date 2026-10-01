import json

person = {"name": "John","age": 30 , 
          "city": "New York", "hasChildren": False,
            "titles" : ["engineer", "Programmer"]
    }

personjson = json.dumps(person)
print(personjson)

person2json = json.dumps(person, indent=5, separators= (': ', "= ")) #simple formatting like rather than , use semi colon to sepearate each key and to tell value of key dont use colon :  use =
print(person2json)

with open('person.json', 'w') as file: #creates file person.json
    json.dump(person, file, indent=4)

person = json.loads(personjson) #changed json to dictionary this is for loading from a string in the program
print(person) 

#load from a json file to python dictionary
with open('person.json', 'r') as file:
    person.json.load(file)
    print(person)