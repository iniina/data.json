import json

with open('data.json', 'r') as file:
    data = json.load(file)

data['kota'] = 'Malang' 

with open('data.json', 'w') as file:
    json.dump(data, file, indent=3)
