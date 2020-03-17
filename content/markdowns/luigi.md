Title: Luigi
Created: 2012-10-21
Pip: luigi
Tags: pipeline, dashboard
Source_url: https://github.com/spotify/luigi
Documentation_url: https://luigi.readthedocs.io/en/stable/
Sheet_creation: 2020-01-12
Redactors: André B.
Updated: 2020-02-20
Licenses: Apache 2.0



Luigi est une librairie aidant à la création de pipelines complexes. Elle prend en charge la résolution des dépendances, la gestion du workflow, la visualisation, la gestion des erreurs, l'intégration au terminal et d'autres tâches associées.

Le serveur Luigi propose une interface graphique pour superviser les différentes tâches :
![Alt Text]({static}/res/luigi_web.png)


En terme de concept, Luigi est semblable à GNU Make ou certaines tâches peuvent avoir des dépendances. En fonction de ces dépendances, Luigi génère un graphe d'exécution et permet de le visualiser pour consulter l'avancement général. Luigi, contrairement à Make, est configuré en Python. Toutes sortes de tâches sont supportées, en particulier l'entraînement de réseaux de neurones, les tâches Hadoop, Spark, des manipulations de bases de données,...

Luigi est assez robuste, supporte des milliers de tâches, organisés en graphes complexes. Les tâches récurrentes sont supportées.

Cependant, quelques limites sont énoncées :

* Le fonctionnement par batch en fait un outil moins efficace pour les processus continus
* Ne supporte pas plus de dizaines de milliers de tâches
* Luigi ne supporte pas l'exécution distribuée (une tâche, un nœud). Des contre-mesures existent mais ne sont pas idéales
* Luigi n'a pas de lancement automatique, il faut utiliser un autre outil pour déclencher les workflow (par exemple, contrab)
