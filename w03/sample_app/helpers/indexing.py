import numpy as np

def process_tf(tf, i, j, tag, obj):
    try:
        posting = tf[tag]
    except KeyError:
        posting = {}
    posting[i] = obj.posting_content(j)
    tf[tag] = posting

def process_df(df, tag):
    try:
        df[tag]['df'] += 1
    except KeyError:
        df[tag] = {'df': 1.0}

def calculate_idf(nt, size):
    return np.log(1 + ((float(size)-nt) / nt))

def process_idf(df, tag, size):
    df[tag]['idf'] = calculate_idf(df[tag]['df'],size)


