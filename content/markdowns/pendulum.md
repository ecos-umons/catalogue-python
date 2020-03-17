Title: Pendulum
Created: 2016-07-04
Pip: pendulum
Tags: temporel, manipulation, autre outil
Website_url: https://pendulum.eustace.io/
Source_url: https://github.com/sdispater/pendulum
Documentation_url: https://pendulum.eustace.io/docs/
Sheet_creation: 2020-02-05
Redactors: André B.
Updated: 2020-03-03
Licenses: MIT



Pendulum est une solution de représentation du temps plus complète que le paquet `datetime` par défaut. Pour une meilleure intégration avec les projets existant, la classe `pendulum` est une sous-classe de `datetime`. Cela permet de remplacer naïvement toutes les instances dans le code à l'exception des comparaisons avec `type()` telles qu'elles peuvent être effectuées par les librairies sqlite3 ou MySQLdb. D'autres problèmes peuvent être rencontrés avec Django qui utilise `isoformat()`. En effet, toute date, dans pendulum, est relative à un fuseau horaire.

Pendulum se vente d'être plus stable que l'alternative la plus populaire, Arrow. En particulier, Arrow est critiquée pour le manque de fiabilité quand à ses méthodes de conversion de texte en date.

En particulier, pendulum supporte :

* L'encodage et la conversion du fuseau horaire (UTC par défaut)
* Les méthodes `now`, `today`, `yesterday`, `tomorrow`, acceptant un paramètre de fuseau horaire
* La lecture et l'écriture depuis différents formats (dont l'ISO 8601 et ses dérivés)
* Les décalages (de secondes, heures, jours, semaines,...)
* Les durées/intervalles
* Un format humanisé (par exemple, "il y a une heure"), en plusieurs langues
* Export du timestamp (en secondes depuis le 1 janvier 1970)
* La possibilité d'extension pour des besoins plus précis

## Exemple

```python
>>> now = pendulum.now('Europe/Paris') #'2020-02-03T14:38:58.502116+02:00'
>>> tomorrow = now.add(days=1) # obtenir demain
>>> now.in_timezone('UTC') # changer de fuseau horaire



>>> past = pendulum.now().subtract(minutes=2)
>>> past.diff_for_humans()
>>> '2 minutes ago'

>>> lastweek = now.substract(weeks=1)
>>> delta = past - lastweek
>>> delta.in_words(locale='en')
'6 days 23 hours 58 minutes'
```
