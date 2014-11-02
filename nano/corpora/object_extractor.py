# coding: utf-8

import csv
import sys
import json

csv.field_size_limit(sys.maxsize)

object_types = [
    'householditem',
    'hallwayitem',
    'furniture',
    'tableitem',
    'bedroomitem',
    'kitchenitem',
    'flooritem',
    'bathroomitem',
    'wallitem',
    'weapon',
    'musicinstrument',
    'food',
    'fruit',
    'grain',
    'nut',
    'legume',
    'condiment',
    'bakedgood',
    'beverage',
    'wine',
    'vegetable',
    'cheese',
    'meat',
    'candy',
    'personalcareitem',
    'drug'
]

with open('NELL/NELL.08m.880.esv.csv') as f:
    reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    objects = {}
    for row in reader:
        for object_type in object_types:
            if not object_type in objects:
                objects[object_type] = []
            if 'concept:' + object_type + ':' in row ['Entity']:
                objects[object_type].append(row['Best Entity literalString'])
                print row['Entity']

# Remove repeated entries
for key in objects:
    objects[key] = list(set(objects[key]))

with open('objects.json', 'w') as g:
    json.dump(objects, g)
