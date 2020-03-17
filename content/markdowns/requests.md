Title: Requests
Created: 2011-02-13
Pip: requests
Tags: acquisition, autre outil
Website_url: https://2.python-requests.org/en/master/
Source_url: https://github.com/psf/requests
Sheet_creation: 2019-12-02
Redactors: André B.
Updated: 2020-03-04
Licenses: Apache 2.0



Requests permet d'envoyer des requêtes HTTP/1.1 extrêment facilement. La librairie permet de ne pas avoir à ajouter des commandes de requêtes aux urls ou d'encoder les données d'un POST. Le maintient de la connexion et la mise en commun des ressources est automatisée grâce à `urllib3`.

Concrètement, une requête effectué avec Requests ressemble à ceci :

```python
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
```

Diverses métadonnées sur la requête sont aussi disponibles (ici dans l'objet "r"). Parmi celles-ci, le code de statut, le contenu, les en-têtes.

Requests est la librairie la plus téléchargée et un projet soutenu directement par la Python Software Foundation.
