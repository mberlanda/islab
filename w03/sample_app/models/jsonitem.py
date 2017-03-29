class JsonItem(object):

    def __init__(self, doc):
        self.doc = doc
        self.probs = self._probs()
        self.tags = self._tags()
        self.tags_len = len(self.tags)
        self.max_probs = max(self.probs)

    def _probs(self):
        try:
            return self.doc['clarifai_probs']
        except KeyError:
            return []

    def _tags(self):
        try:
            return self.doc['clarifai_tags']
        except KeyError:
            return []

    def posting_content(self, j):
        return {
            'raw_tf': 1, 'prob': self.probs[j],
            'norm_p': self.probs[j]/self.max_probs,
            'freq': 1.0 / self.tags_len
        }


