def empty_and_insert(db, collection_name, data):
    if db[collection_name].count() > 0:
        db[collection_name].drop()
    db[collection_name].insert_many(data)
    return db[collection_name].count()
