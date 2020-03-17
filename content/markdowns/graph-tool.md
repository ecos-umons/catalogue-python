Title: graph-tool
Created: 2006-07-10
Latest: 2015-10-27
Version: 2.11
Pip: graph-tool
Tags: autre outil, generation, manipulation, statistique, visualisation
Website_url: https://graph-tool.skewed.de/
Source_url: https://git.skewed.de/count0/graph-tool
Documentation_url: https://graph-tool.skewed.de/static/doc/index.html
Sheet_creation: 2020-03-06
Redactors: André B.
Updated: 2020-03-06
Licenses: GPLv3


graph-tool est un module permettant la manipulation et l'analyse statistique de graphes. Pour ce faire, de nombreuses opérations sont proposées, mais aussi des générateurs, ...

Malgré son apparence de module Python, les opérations critiques sont écrites en C++ et utilisant la librairie Boost Graph. De cette façon, la rapidité d'exécution est garantie. De plus, le module supporte OpenMP qui permet les exécutions parrallèles et distribuées.

Pour complèter les fonctionnalités précises, des visualisations sont disponibles. La documentation encourage cependant à utiliser graphviz à cet effet.

![Alt text]({static}/res/graph-tool.png)


En particulier, graph-tool supporte :

* La création manuelle de graphes
* Des propriétés arbitraire sur les nœuds, graphes ou arcs
* Des filtres efficaces sur les arcs et nœuds
* Des opération I/O (chargement et sauvegarde), avec GraphML, GML, dot et la sérialisation
* L'accès aux propriétés statistiques (histogramme de degrés, corrélations de nœuds, distance minimale moyenne,...)
* Des algorithmes topologiques (isomorphismes, minimum spanning tree, maximum flow, composantes connexes, ...)
* La génération de graphes aléatoires (tout en pouvant spécifier des listes de degrés ou de corrélation)
* La détection de communautés
* Le clustering
* ...

Contrairement à ce qui est disponible via PyPI, le version la plus récente sur le site est la 2.29 datant de juillet 2019. Des nouveaux commits apparaissent également sur la branche master du projet, sur GitLab.
