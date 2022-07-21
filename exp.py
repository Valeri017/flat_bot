import json
import pprint



with open('state_moscow.json') as f:
    templates = json.load(f)
print(type(templates[0]))
b = templates[0]
for k, v in b.items():
#    pprint.pprint(repr(k))
    b.get('name')
    print(b)