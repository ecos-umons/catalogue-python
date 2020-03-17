Title: Lifelines
Created: 2013-12-10
Pip: lifelines
Tags: temporel, statistique, visualisation
Source_url: https://github.com/CamDavidsonPilon/lifelines
Documentation_url: https://lifelines.readthedocs.io/en/latest/
Sheet_creation: 2019-12-03
Redactors: André B.
Updated: 2020-02-20
Licenses: MIT





Lifelines est une implémentation d'analyse de survie : quelle est la probabilité qu'un évènement mettant fin aux interactions ("mort") se produise, en fonction du temps ? Et quelle sera notre population après un temps donné ?

Ses spécificités sont :

* De s'intégrer avec Pandas et ses structures de données
* De proposer des représentations préconfigurées pour l'analyse de survie (dont une superposition avec une population de référence)
* Une API simple et intuitive
* De ne faire que l'analyse de survie
* De supporter la censure à gauche, à droite et par intervalle.

Par défaut, le modèle utilisé est celui de Kaplan-Meier.
Cependant, il est possible de définir un modèle de taux de mortalité avec d'autres modèles paramétriques tels que Weibull, Log-Normal, Log-Logistique, Piewewise Exponential, Gamma Généralisé ou exponentiel. Il est également possible de créer une fonction sur mesure.

Dans le cas où la survie a été modélisée avec Kaplan-Meier, l'estimation de ce taux de mortalité peut-être proposée par Nelson-Aalen.

Lifelines utilise la formule de Cox pour ses régressions.
