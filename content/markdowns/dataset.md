Title: Dataset
Created: 2013-04-01
Pip: dataset
Tags: acquisition, autre outil
Source_url: https://github.com/pudo/dataset
Documentation_url: https://dataset.readthedocs.io/en/latest/
Sheet_creation: 2020-01-08
Redactors: André B.
Updated: 2020-02-19
Licenses: MIT



Dataset rend une base de données la solution la plus facile pour sauvegarder des données structurées, devant le format CSV.

La base de données relationnelle a besoin d'un schéma. Celui-ci est créé automatiquement. Aussi, les données sont créées ou mises à jour en fonction de la situation : pas besoin de vérifier leur existence. L'utilisateur fourni un dictionnaire et Dataset crééee les colonnes manquantes à la volée. Les outils de recherche, de comparaison, de tri sont également fourni.

Le langage SQL est pour l'essentiel caché et la plupart des types de données sont compatibles (Dataset reposant sur SQLAlchemy). Cependant, il reste possible d'effectuer une requête SQL pour profiter de toute la puissance des bases de données relationnelles.


Voici un exemple d'utilisation, tiré de la documentation :
```python
import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='John Doe', age=37))
table.insert(dict(name='Jane Doe', age=34, gender='female'))

john = table.find_one(name='John Doe')
```
