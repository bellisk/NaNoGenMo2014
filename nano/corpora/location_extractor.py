# coding: utf-8

import csv
import sys
import json

csv.field_size_limit(sys.maxsize)


buildings = [
    'building',
    'retailstore',
    'hospital',
    'trainstation',
    'placeofworship',
    'stadiumoreventvenue',
    'museum',
    'airport',
    'shoppingmall',
    'bridge',
    'hotel',
    'restaurant',
    'skyscraper',
    'monument'
]


with open('NELL/NELL.08m.880.esv.csv') as f:
    reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
    locations = {}
    for row in reader:
        for building_type in buildings:
            if not building_type in locations:
                locations[building_type] = []
            if 'concept:' + building_type + ':' in row ['Entity']:
                locations[building_type].append(row['Best Entity literalString'])
                print row['Entity']
        if 'concept:geopoliticallocation' in row['Entity']:
            if 'geopolitical' not in locations:
                locations['geopolitical'] = [row['Best Entity literalString']]
            else:
                locations['geopolitical'].append(row['Best Entity literalString'])
        if 'concept:landscapefeatures' in row['Entity'] and 'generalizations' in row['Relation']:
            if 'landscape' not in locations:
                locations['landscape'] = []
            else:
                locations['landscape'].append(row['Best Entity literalString'])

# Remove repeated entries
for key in locations:
    locations[key] = list(set(locations[key]))

    with open('locations.json', 'w') as g:
        json.dump(locations, g)
