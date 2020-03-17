Title: Mimesis
Created: 2017-07-15
Pip: mimesis
Tags: generation
Website_url: https://mimesis.name/
Source_url: https://github.com/lk-geimfari/mimesis
Documentation_url: https://mimesis.name/api.html
Sheet_creation: 2019-12-04
Redactors: André B.
Updated: 2020-02-20
Licenses: MIT



Mimesis est un module rapide et facile d'utilisation qui aide à générer de grands volumes de données fictives dans de nombreuses langues.

Ces données fictives peuvent être très utiles lors du développement et pour des tests. Par exemple, elle peuvent servir à remplir une base de données de tests, créer des documents JSON et XML réalistes et anonymiser des données de production.

## Fonctionnalités

 Mimesis propose entre autres :

* Des générateurs personnalisables
* Un générateur générique
* Plus de 33 langues
* Une génération de données par modèle
* La romanisation du Cyrillique
* 20 providers (type de donnée générée), et les types associés :
  * Aléatoire (se basant sur `random`)
  * Adresse
  * Entreprise
  * Date et heure
  * Nourriture (et boisson)
  * Personne
  * Données scientifiques (séquence adn, masse molaire, ...)
  * Texte
  * Vêtement (taille)
  * Codes (ISBN, EAN, PIN)
  * Choix (par rapport à une séquence)
  * Cryptographie (clefs, uuid)
  * Développement (OS, langage de programmation...)
  * Nom de fichier, chemin
  * Composant hardware et spécifications
  * Données relatives à internet
  * Nombres
  * Documents structurés (html, css)
  * Moyens de transports
  * Système métrique
* Des générateurs de données spécifiques à un pays (numéro de téléphone, code communal,...)

L'utilisation de Mimesis est simple et efficace :
```Python
>>> from mimesis import Person
>>> person = Person('en')

>>> person.full_name()
'Antonetta Garrison'

>>> person.occupation()
'Backend Developer'

>>> person.telephone()
'1-408-855-5063'
```
