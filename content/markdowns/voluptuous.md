Title: Voluptuous
Created: 2010-07-15
Pip: voluptuous
Tags: validation
Source_url: https://github.com/alecthomas/voluptuous
Documentation_url: http://alecthomas.github.io/voluptuous/docs/_build/html/index.html
Sheet_creation: 2019-12-04
Redactors: André B.
Updated: 2020-03-05
Licenses: BSD



Voluptuous est un module de validation de données visant principalement les formats JSON et YAML. Ses trois buts sont :

* La simplicité
* Le support de structures complexes
* La génération de messages d'erreur utiles

Voici deux exemples venant du dépôt de Voluptuous.

La premier met en avant l'écriture claire et simple de requête de validation :

```python
from voluptuous import Required, All, Length, Range

schema_basique = Schema({
 'q': str,
 'per_page': int,
 'page': int,
})

schema = Schema({
  Required('q'): All(str, Length(min=1)),
  Required('per_page', default=5): All(int, Range(min=1, max=20)),'page': All(int, Range(min=0)),
})
```

Le second exemple, lui, présente les erreurs spécifiques de la librairie :
```python
from voluptuous import MultipleInvalid, Invalid
try:
  schema({})
  raise AssertionError('MultipleInvalid not raised')
except MultipleInvalid as e:
  exc = e
print(str(exc) == "required key not provided @ data['q']")#True
```
