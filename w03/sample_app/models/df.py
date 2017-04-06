# db.calzedoniajson_df_0.find({'tag': 'casual'}, {'df':1, '_id':0})

def get_tf(tag, doc, metric='norm_p'):
    try:
        w = tf[tag][doc][metric]
    except KeyError:
        w = 0.0
    return w

def get_idf(tag, metric='idf'):
    try:
        w = df[tag][metric]
    except KeyError:
        w = 0.0
    return w

def bag(doc, tfm='norm_p', idfm='idf'):
    try:
        tgs = docs[doc]['tags']
        b = np.array([get_tf(x, doc, metric=tfm) * get_idf(x, metric=idfm)
                     for x in tgs])
    except KeyError:
        tgs = []
        b = np.array([])
    return tgs, b

def get_posting(tag, tfm='norm_p', idfm='idf'):
    p = []
    idf = get_idf(tag, metric=idfm)
    try:
        pd = tf[tag]
        for d, m in pd.items():
            p.append((d, m[tfm]*idf))
    except KeyError:
        pass
    return sorted(p, key=lambda x: -x[0])

print get_posting('girl')
