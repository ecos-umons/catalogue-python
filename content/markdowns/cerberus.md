Title: Cerberus
Created: 2012-10-16
Pip: cerberus
Tags: validation
Source_url: https://github.com/pyeve/cerberus
Documentation_url: http://docs.python-cerberus.org/en/stable/
Sheet_creation: 2019-12-04
Redactors: André B.
Updated: 2020-02-18
Licenses: ISCL



Cerberus est une librairie extensible et légère de validation de données.

L'exemple ci-dessous, tiré de la documentation, met en avant l'utilisation simple.

```python
>>> v = Validator({'name': {'type': 'string'}})
>>> v.validate({'name': 'john doe'})
True
```

Cerberus permet de valider le type et d'autres fonctionnalités de base pour permettre une utilisation immédiate. Par contre, un travail supplémentaire est necéssaire pour une validation plus spécifique (telle donnée est-elle une adresse ? une date ?). La librairie n'a pas de dépendance et peut s'entendre pour une validation personnalisée.
