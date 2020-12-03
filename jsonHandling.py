import json

data = {
    "id": 0,
    "name": "Hud Hudson",
    "age": 24,
    "position": "Car"
}

data_as_json = json.dumps(data)
print(data_as_json)
print(type(data_as_json))

with open('data.json','w') as json_file:
    json.dump(data,json_file)

with open('data.json','r') as json_file:
    pythonic_json = json.load(json_file)

print(pythonic_json)
print(type(pythonic_json))