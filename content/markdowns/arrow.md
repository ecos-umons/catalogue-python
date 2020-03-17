Title: Arrow
Created: 2012-11-19
Pip: arrow
Tags: temporel, manipulation, autre outil
Source_url: https://github.com/crsmithdev/arrow
Documentation_url: https://arrow.readthedocs.io/en/latest/
Sheet_creation: 2020-01-07
Redactors: André B.
Updated: 2020-02-18
Licenses: Apache 2.0



Arrow offre une solution unifiée pour la création, la manipulation, la conversion et la présentation de dates et autres données temporelles.
L'intérêt mis en avant est de minimiser le nombre d'imports et le code necéssaire pour couvrir les différents scénarios liés aux dates. En particulier, Arrow peut remplacer le module par défaut (datetime) sans modification supplémentaire.

Arrow tire son nom de la ligne du temps et est inspiré de moment.js et de requests.

Arrow supporte :

* L'encodage et la conversion du fuseau horaire (UTC par défaut)
* Plusieurs façons d'enregistrer une date
* La norme ISO 8601
* Les décalages (de secondes, heures, jours, semaines,...)
* Les durées
* Un format humanisé (par exemple, "il y a une heure"), en plusieurs langues
* Export du timestamp (en secondes depuis le 1 janvier 1970)
* La possibilité d'extension pour des besoins plus précis



Voici un exemple d'utilisation tiré de la documentation :
```python
>>> import arrow
>>> arrow.get('2013-05-11T21:23:58.970460+07:00')
<Arrow [2013-05-11T21:23:58.970460+07:00]>

>>> utc = arrow.utcnow()
>>> utc
<Arrow [2013-05-11T21:23:58.970460+00:00]>

>>> utc = utc.shift(hours=-1)
>>> utc
<Arrow [2013-05-11T20:23:58.970460+00:00]>
```
