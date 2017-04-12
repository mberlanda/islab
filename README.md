# Islab

```
$ sudo pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m nltk.downloader omw snowball_data stopwords wordnet
$ sudo service mongod start
$ mongorestore -d mec -c calzedoniajson_items_0 collections/calzedoniajson_items_0.bson
$ mongorestore -d mec -c petitbateaujson_items_0 collections/petitbateaujson_items_0.bson
$ jupyter notebook mecstats.ipynb
$ jupyter nbconvert --execute mongodb.ipynb
```
