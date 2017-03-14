#!/usr/bin/python
# -*- coding: latin-1 -*-

import pymongo
import pprint
from datetime import datetime


db_name, host = 'mdb_tutorial', 'localhost'
db = pymongo.MongoClient(host=host)[db_name]
p = pprint.PrettyPrinter(indent=4)

doc1 = {'name': 'Napoléon', 'last_name': 'Bonaparte'}
doc2 = {
    'name': 'Napoléon', 
    'last_name': 'Bonaparte',
    'categories': ['historical figure', 'general']
}
doc3 = {
    'name': 'Napoléon', 
    'last_name': 'Bonaparte',
    'dates': {'birth': datetime(1769, 8, 15), 
              'death': datetime(1821, 5, 5)},
    'categories': ['historical figure', 'general']
}
doc4 = {
    'name': 'Napoléon', 
    'last_name': 'Bonaparte',
    'dates': {'birth': datetime(1769, 8, 15), 'death': datetime(1821, 5, 5)},
    'categories': ['historical figure', 'general'],
    'wifes': [
        {
            'name': 'Joséphine de Beauharnais', 
            'dates': {'birth': datetime(1793, 6, 23), 'death': datetime(1814, 5, 29)}
        },
        {
            'name': 'Marie Louise, Duchess of Parma', 
            'dates': {'birth': datetime(1791, 12, 12), 'death': datetime(1847, 12, 17)}
        }
    ]
}

#Insert one and multiple docs in collections

db['people'].drop()
db['people'].insert_one(doc1)
print db['people'].count()
db['people'].insert_many([doc2, doc3, doc4])
print db['people'].count()

# MongoDb cursors for query¶

cursor = db['people'].find().skip(2).limit(2)
for record in cursor:
    p.pprint(record)
    print ""
cursor.close()

# Simple queries

q1 = {'last_name': 'Bonaparte'}
p.pprint(db['people'].find_one(q1)) #find one record or none
p.pprint(db['people'].find(q1)) #multiple finding returns a cursor
p.pprint([x for x in db['people'].find(q1)]) #iterate on cursors

# Selection and projection operators

selection = {'dates.birth': {'$gte': datetime(1750, 1, 1)}}
projection = {'last_name': 1, '_id': 0}
for data in db['people'].find(selection, projection):
    print data