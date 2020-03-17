Title: NetworkX
Created: 2002-05-01
Pip: networkx
Tags: autre outil, generation, manipulation, statistique
Website_url: http://networkx.github.io/
Source_url: https://github.com/networkx/networkx
Documentation_url: https://networkx.github.io/documentation/stable/
Sheet_creation: 2020-03-06
Redactors: André B.
Updated: 2020-03-06
Licenses: BSD


NetworkX est un module ciblant la création, la manipulation et l'étude des structures, dynamiques et fonctions de graphes complexes. Le public visé est composé de mathématiciens, physiciens, biologistes, informaticiens ou sociologues.

En particulier, NetworkX propose :

* Des structures de données pour les graphes, digraphes et multigraphes
* De nombreux algorithmes standards
* Des mesures sur le graphe et sa structure
* Des générateurs de graphes classiques, aléatoire ou des réseaux synthétiques
* Les nœuds sont arbitraires (texte, image, XML, ...)
* Les arcs peuvent contenir des données arbitraires (poids, séries, ...)
* Des opérations et algorithmes internes écrits en C, C++ et FORTRAN, permettant de travailler avec des grands volumes de données
* Une interface Python simple permettant un prototypage rapide


Un exemple de cette simplicité est mis en avant ici avec une recherche du plus court chemin :

```python
>>> import networkx as nx
>>> G = nx.Graph()
>>> G.add_edge('A', 'B', weight=4)
>>> G.add_edge('B', 'D', weight=2)
>>> G.add_edge('A', 'C', weight=3)
>>> G.add_edge('C', 'D', weight=4)
>>> nx.shortest_path(G, 'A', 'D', weight='weight')
['A', 'B', 'D']
```
