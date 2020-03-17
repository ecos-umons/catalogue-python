Title: Dask
Created: 2015-01-29
Pip: dask
Tags: dashboard, pipeline, manipulation
Website_url: https://dask.org/
Source_url: https://github.com/dask/dask
Documentation_url: https://docs.dask.org/en/latest/
Sheet_creation: 2020-01-08
Redactors: André B.
Updated: 2020-02-18
Licenses: New BSD



Dask est une librairie pour la parallélisation. En s'appuyant sur des librairies communes, NumPy et Pandas, et en proposant une interface semblable, Dask se veut facile d'utilisation. Les collections ainsi crées (Array, DataFrame, Bag, Delayed, Future) peuvent ainsi être utilisées dans des tâches diverses.

Ces tâches sont interconnectées et forment un graphe implicite aboutissant au résultat final attendu par l'utilisateur. La seconde principale contribution de Dask, après les collections, est un ordonnanceur dynamique permettant une exécution distribuée utilisant le graphe.

De plus, un dashboard est proposé pour suivre l'ordre des tâches et leur statut.

Dask met plusieurs valeurs en avant :
* La familiarité (réutilisation des tableaux NumPy et DataFrames de Pandas)
* La flexibilité (l'interface de l'ordonnanceur permet des workflows spécialisés)
* Le code natif (tout sera écrit en python)
* La rapidité (légereté de Dask)
* La montée en charge (fonctionne sur des ensembles de milliers de processeurs)
* La simplicité (installation et utilisation triviale sur une seule machine)
* La communication (retours et outils de diagnostiques pour les humains)
