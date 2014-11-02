# coding: utf-8

import csv
import sys
import json

csv.field_size_limit(sys.maxsize)

with open('NELL/NELL.08m.880.esv.csv') as f:
    reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    # Build a list of types of clothing, and add which types can be worn together
    clothing = {}
    for row in reader:
        if 'concept:clothing' in row['Entity'] and 'clothingtogowithclothing' in row['Relation']:
            clothing_type = row['Best Entity literalString'].lower()
            pair = row['Best Value literalString'].lower()
            if clothing_type in clothing:
                if not pair in clothing[clothing_type]['goes-with']:
                    clothing[clothing_type]['goes-with'].append(pair)
            else:
                clothing[clothing_type] = {'goes-with': [pair]}
                print clothing_type
    print len(clothing)
    
# Fix plurals
new_clothing = {}
for clothing_type in clothing:
    singular = ''
    if clothing_type[-2:] == 'es' and clothing_type[:-2] in clothing:
        singular = clothing_type[:-2]
    elif clothing_type[-1:] == 's' and clothing_type[:-1] in clothing:
        singular = clothing_type[:-1]
    if singular:
        new_clothing[singular] = clothing[singular]
        # Don't bother copying over the goes-with values for the plural clothing type
        print clothing_type + ' merged with ' + singular
    else:
        new_clothing[clothing_type] = clothing[clothing_type]
clothing = new_clothing
print len(clothing)

with open('NELL/NELL.08m.880.esv.csv') as f:
    reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    # Add specific items of clothing for each type
    for row in reader:
        if 'concept:clothing' in row['Entity'] and 'generalizations' in row['Relation']:
            name = row['Best Entity literalString']
            n = 0
            for clothing_type in clothing:
                if clothing_type in name.lower():
                    if 'types' in clothing[clothing_type]:
                        clothing[clothing_type]['types'].append(name)
                    else:
                        clothing[clothing_type]['types'] = [name]
                    n += 1
            # What items of clothing don't fit into a type?
            #if n == 0:
            #    print name

with open('/home/rachel/Desktop/NELL.clothes.json', 'w') as g:
    json.dump(clothing, g)
