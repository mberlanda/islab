class DfCollection(object):

    def __init__(self, db, collection):
        self.conn = db[collection]
