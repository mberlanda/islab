import pymongo
import numpy as np
from models.jsonitem import JsonItem
from helpers.collections import empty_and_insert
from helpers.indexing import *
import pdb

db = pymongo.MongoClient()['mec']
dataset = 'calzedoniajson_items_0'



if __name__ == '__main__':
    
    docs, df, tf = {}, {}, {}

    cursor = db[dataset].find(no_cursor_timeout=True).sort('_id', pymongo.ASCENDING) # optional no_cursor_timeout=True
    size = cursor.count()
    for i, doc in enumerate(cursor) :
        try:
            item = JsonItem(doc)
            docs[i] = { 'id': item.doc['_id'], 'tags': item.tags }

            for j, tag in enumerate(item.tags):
                process_tf(tf, i, j, tag, item)
                process_df(df, tag)
                process_idf(df, tag, size)
        except ValueError:
            pass
    cursor.close()

    print(df)
