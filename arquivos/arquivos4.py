
import json


d1 = {
    'Pessoa 1': {
        'nome': 'Rose',
        'idade': 25,
     },
    
    'Pessoa 2': {
        'nome': 'Luiz',
        'idade': 21,
     },

    'Pessoa 3': {
        'nome': 'Luan',
        'idade': 17,
     },
}


d1_json = json.dumps(d1, indent=True)

with open('abc4.json','w+') as file:
    file.write(d1_json)

