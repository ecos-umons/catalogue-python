Title: Peewee
Created: 2010-10-18
Pip: peewee
Tags: manipulation, autre outil
Source_url: https://github.com/coleifer/peewee
Documentation_url: http://docs.peewee-orm.com/en/latest/
Sheet_creation: 2020-02-11
Redactors: André B.
Updated: 2020-03-03
Licenses: MIT



Peewee est un petit ORM (s'occupant du mapping objet-modèle relationnel), facile d'utilisation. La syntaxe se rapproche de celle de Django et Peewee supporte des connexions vers sqlite, mysql, postgresql et cockroachdb.

Peewee propose tous les services d'un ORM : définition d'un modèle, connexion à une base de données, entrer des données, trier, filtrer, aggréger et de manière générale effectuer des requêtes complexes. Un utilitaire permet de faire une requête SQL comme alternative à l'utilisation des filtres.

Voici un exemple de définition de modèle :
```Python
from peewee import *
import datetime


db = SqliteDatabase('my_database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
```

Des exemples d'utilisation dans des web-services (notamment avec Flask) sont disponibles dans la documentation.
