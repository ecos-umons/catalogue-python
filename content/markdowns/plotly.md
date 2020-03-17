Title: plotly.py
Created: 2013-06-13
Pip: plotly
Tags: visualisation, exploration
Website_url: https://plot.ly/python/
Source_url: https://github.com/plotly/plotly.py
Documentation_url: https://plot.ly/python-api-reference/
Sheet_creation: 2020-02-05
Redactors: André B.
Updated: 2020-03-03
Licenses: MIT



plotly.py est une librairie proposant des graphes interactifs sur des pages web. `plotly.py` est construit sur base de `plotly.js` qui propose une quarantaine de graphes différents. Ces représentations sont disponibles dans des notebooks jupyter.

Parmi les représentations, il y a :

* Des graphiques classiques (camembert, barres, lignes, ...)
* Des graphiques statistiques (histogrammes, boîtes à moustaches, zones d'erreur, ...)
* Des graphiques scientifiques (heatmap, graphe logarithmiques, dendogrammes, champs de vecteurs, graphes de réseaux, graphes polaires, ...)
* Des graphiques financiers (graphique en entonnoir, suite temporelle, indicateur, jauges, ...)
* Des cartes interactives (choloroplèthe, densité, bulles, lignes,...)
* Des graphiques 3D
* Des subdivisions en sous-graphiques


Les données sont utilisables via des structures de données natives à python (liste), tableaux numpy, avec des séries pandas, des chaînes de caractères ou des dates.

Un graphique peut être obtenu soit en utilisant un constructeur, une "factory" ou le module express (qui permet une définition de très haut niveau). Toutes autres modifications visuelles, telle que l'ajout d'informations supplémentaire en surimpression ou la division en sous-graphes, sont possibles par la suite.

![Alt Text]({static}/res/plotly.png)

En plus de cela, plotly.py est incorporé dans le projet Dash qui est un framework permettant de créer des applications web pour la visualisation de données. Dash étant une solution professionnelle proposant une utilisation open-source.
