Title: igraph
Created: 2008-02-15
Pip: python-igraph
Tags: exploration, autre outil
Website_url: https://igraph.org/python/
Source_url: https://github.com/igraph/python-igraph
Documentation_url: https://igraph.org/python/doc/igraph-module.html
Sheet_creation: 2020-02-06
Redactors: André B.
Updated: 2020-03-04
Licenses: GPL



igraph est une librairie efficace pour la recherche et l'analyse de réseaux. Le paquet logiciel python-igraph propose une interface pour accéder à ses différentes fonctionnalités.

La librairie de base, en C, est à installer et compiler indépendemment du module Python.

Parmi les-dites fonctionnalités, il y a la possibilité de construire un graphe manuellement :

```Python
g = Graph()
g.add_edges([(2, 0)])
g.add_vertices(3)
g.add_edges([(2, 3), (3, 4), (4, 5), (5, 3)])
```

A des fins de recherche, il est aussi possible de créer des graphes avec des générateurs (déterministes ou non).

Une fois le graphe généré, les différentes propriétés (telles que le degré, étiquettes,  ...) sont accessibles.

Finalement, igraph propose des représentations paramétrables et un export vers un fichier pour une réutilisation ultérieure.

![Alt Text]({static}/res/igraph.png)
