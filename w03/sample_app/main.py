import pymongo
import numpy as np
from models.jsonitem import JsonItem
from models.dfCollection import DfCollection
# from models.tfCollection import TfCollection
from helpers.collections import empty_and_insert
from helpers.indexing import *
import pdb

db = pymongo.MongoClient()['mec']
dataset = 'calzedoniajson_items_0'



if __name__ == '__main__':
    
    docs, df, tf = {}, {}, {}

    cursor = db[dataset].find(no_cursor_timeout=True).sort('_id', pymongo.ASCENDING) # optional no_cursor_timeout=True
    size = cursor.count()

    print 'Processing {0} documents from {1}'.format(size, dataset) 
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

    docs_map = [dict({'posting_key': k}.items() + v.items()) for k,v in docs.items()]
    print  '{0} docs collected'.format(empty_and_insert(db, 'calzedoniajson_docs_0', docs_map) )

    df_map = [dict({'tag': k}.items() + v.items()) for k,v in df.items()]
    print '{0} df collected'.format(empty_and_insert(db,'calzedoniajson_df_0', df_map) )

    tf_map = [dict({'tag': k}.items() + v.items()) for k,v in tf.items()]
    print '{0} tf collected'.format(empty_and_insert(db,'calzedoniajson_tf_0', df_map) )
