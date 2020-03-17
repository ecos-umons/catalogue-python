Title: toolz
Created: 2015-01-11
Pip: toolz
Tags: autre outil, manipulation
Source_url: https://github.com/pytoolz/toolz/
Documentation_url: http://toolz.readthedocs.org/
Sheet_creation: 2020-03-06
Redactors: André B.
Updated: 2020-03-06
Licenses: New BSD


toolz est une ensemble de fonctions d'utilité générale pour les itérateurs, les fonctions et les dictionnaires.

Toutes ces nouvelles fonctions sont :

* Composables (sont interopérables)
* Sans effet de bord
* Efficientes : ne calculent que le necéssaire
* Low Tech : Pas d'artifice ou de syntaxe complexe à apprendre
* Optimisées
* Sérialisables ; elles supportent les solutions courantes de calcul parrallélisé



toolz est divisé en trois sous-modules :

* `itertoolz` pour les interactions avec les itérateurs (par exemple, groupby, unique, interpose, ...)
* `functoolz` pour les fonctions d'ordre supérieur (par exemple, memoize, curry, compose, ...)
* `dicttoolz` pour les opérations sur les dictionnaires (par exemple, assoc, update-in, merge)


Toutes ces fonctions sont inspirées des langages fonctionnels travaillant sur des listes. Des tâches assez complexes peuvent être effectuées en couplant plusieurs de ces fonctions.
