class JsonItem(object):

    def __init__(self, doc):
        self.doc = doc

    def probs(self):
        try:
            self.doc['clarifai_probs']
        except KeyError:
            []

    def tags(self):
        try:
            self.doc['clarifai_tags']
        except KeyError:
            []

    def posting_content(self, j):
        return {
            'raw_tf': 1, 'prob': self.probs[j],
            'norm_p': probs[j]/self.max_probs,
            'freq': 1.0 / self.tags_len
        }

    def tags_len(self):
        len(self.tags)

    def max_probs(self):
        max(self.probs)


def process_tf(tf, i, j, tag, obj):
    try:
        posting = tf[tag]
    except KeyError:
        posting = {}
    posting[i] = obj.posting_content(j)
    tf[tag] = posting
