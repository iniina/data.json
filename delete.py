import json

with open('data.json', 'r') as file:
  data = json.load(file)

del data['tempat']