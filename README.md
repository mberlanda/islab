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
$ docker pull mongo:3.6.4
$ docker run --name islab_mongodb -p 27017:27017 -v /Users/mberlanda/Misc/py/islab/collections:/backup -d mongo:3.6.4
$ docker run --name islab-mongo  -v /Users/mberlanda/Misc/py/islab/collections:/backup -p '27010:27017' -d mongo:3.6.4 \
 bash -c 'mongorestore -d mec -c calzedoniajson_items_0 /backup/calzedoniajson_items_0.bson --host mongo:27017'

```
docker run --name some-mongo -d mongo