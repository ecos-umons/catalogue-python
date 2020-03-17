Title: Schematics
Created: 2012-09-02
Pip: schematics
Tags: manipulation, autre outil
Source_url: https://github.com/schematics/schematics
Documentation_url: https://schematics.readthedocs.io/en/latest/
Sheet_creation: 2020-02-07
Redactors: André B.
Updated: 2020-03-04
Licenses: BSD



Schematics propose des solutions pour décrire des données grâce à l'utilisation d'un modèle. Ce modèle permet de définir les types et certains paramètres de validation (longueur, valeur, ...).

Une fois le modèle créé et les données rentrées (dynamiquement ou via un import), celles-ci peuvent être validée et exportée. L'export est prévu vers un dictionnaire de type primitif ou natifs de Python, pouvant être facilement transformé en json.

Contrairement à la plupart des outils proposant ces services (ORM, Object Relational Mapper), Schematics ne propose pas de couche de communication avec une base de données.

Finalement, Schematics est très bien couvert par les tests et propose des tests sur les modèles avec des données fictives (générées en fonction du modèle).
