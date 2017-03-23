# Islab

```
$ sudo pip install venv
$ virtualenv venv
$ source venv/bin/activate
$ pip install pymongo nltk numpy scipy sklearn gensim
$ sudo service mongod start
$ jupyter nbconvert --execute mongodb.ipynb
$ python -m nltk.downloader omw snowball_data stopwords wordnet
$ jupyter notebook mecstats.ipynb
$ mongorestore -d mec -c collection_name collections/calzedoniajson_items_0.bson
```