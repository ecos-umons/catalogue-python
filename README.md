# Catalogue de solutions d’analyse et de traitement des données en Python

![master build](https://github.com/ecos-umons/catalogue-python/workflows/CI/badge.svg)

Ce catalogue a pour but de présenter, de façon succincte, les principales librairies liées à l'analyse et au traitement de données en Python. De la sorte, un acteur avec des connaissances de base dans le domaine pourra naviguer le-dit catalogue afin de repérer des librairies interéssantes pour son projet. Chaque fiche a pour vocation de donner un avant-goût et de permettre de décider rapidement si oui ou non la librairie concernée mérite une étude plus approfondie, via le site et la documentation.

Ce catalogue est un projet opensource et les contributions à la forme et au contenu sont les bienvenus.

## Informations disponibles

### Métadonnées

Afin de complèter la mise en forme d'une fiche sur le site, et ainsi de donner un complément d'information, des métadonnées sont disponibles dans chaque fiche. Celles-ci peuvent être simples ou multiples, necéssaires ou facultatives.

Voici un exemple complet de métadonnées :

* Title: Bokeh <!-- Nom de la librairie -->
* Created: 2013-10-25 <!-- Première publication de la librairie -->
* Latest: 2019-11-04 <!-- Dernière mise à jour de la librairie -->
* Version: 1.4.0 <!-- Version a la date latest -->
* Pip: bokeh <!-- Adresse PyPI -->
* Tags: visualization <!-- Categories (1+) -->
* Website_url: https://bokeh.org/ <!-- Site web (présentation) -->
* Source_url: https://github.com/bokeh/bokeh <!-- Sources (code) -->
* Documentation_url: https://docs.bokeh.org/en/latest/ <!-- Documentation (api, fonctionnement) -->
* Sheet_creation: 2019-11-01 <!-- Première version de la fiche -->
* Redactors: André, Benjamin <!-- Rédacteurs de la fiche -->
* Updated: 2019-11-12 <!-- Date de dernière modification de la fiche -->
* Licenses : BSD-3 <!-- License(s) -->
* Stars: 12556
* Forks: 3173
* Issues: 473
* PullRequests : 13

Un champ vide ne sera pas publié sur le site. Dans le cas ou un dépôt github est mentionné, les 4 derniers champs sont automatiquement ajoutés. Dans certains cas, comme pour graph-tool, il y a une entrée sur PyPI mais pas de package pip. Dans ce cas-là, il sera impossible pour le script de récupérer la dernière version ainsi que la date de celle-ci.

Pour tous les autres cas, voici un exemple minimal pour lequel tous les champs seront visibles sur les site (éventuellement remplis via le script) :

* Title: Bokeh <!-- Nom de la librairie -->
* Created: 2013-10-25 <!-- Première publication de la librairie -->
* Pip: bokeh <!-- Adresse PyPI -->
* Tags: visualization <!-- Categories (1+) -->
* Website_url: https://bokeh.org/ <!-- Site web (présentation) -->
* Source_url: https://github.com/bokeh/bokeh <!-- Sources (code) -->
* Documentation_url: https://docs.bokeh.org/en/latest/ <!-- Documentation (api, fonctionnement) -->
* Sheet_creation: 2019-11-01 <!-- Première version de la fiche -->
* Redactors: André, B<!-- Rédacteurs de la fiche -->
* Updated: 2019-11-12 <!-- Date de dernière modification de la fiche -->
* Licenses : BSD-3 <!-- License(s) -->


### Catégories utilisées

Chaque librairie peut être associée a une ou plusieurs catégories via ses métadonnées. Celles-ci peuvent être ajoutées de façon dynamique. Dans un soucis de cohérence et de simplicité de navigation, les catégories utilisées se limitent actuellement à :

* acquisition
* autre outil
* calcul numérique
* dashboard
* data mining
* environnement scientifique
* exploration
* generation
* machine learning
* manipulation
* nlp
* pipeline
* statistique
* temporel
* validation
* visualisation

### Remarques

Contrairement à ce que laisse entendre la documentation de Pelican, il faut impérativement utiliser ; au lieu de , pour délimiter une liste pour un champ de métadonnées additionnel.

Certains projets ne sont pas hébergés sur GitHub mais launchpad.net.

Les images doivent se trouver dans le dossier `content\res`. Le code pour pouvoir en utiliser une dans une fiche suis la syntaxe suivante : `![Alt text]({static}/res/<nom de l'image>)`

## Librairies rejetées

Certaines librairies ont déjà été considérées puis rejetées pour des raisons diverses. Principalement : indisponibilité sur PyPI, vetusté du projet, hors-sujet ou librairie trop spécifique.

* alvi
* Anaconda
* AWS
* Caffe
* Celery
* chemlab
* data_hacks
* Datacleaner
* datashader
* datasploit
* deap
* DVC
* hadojae/DATA
* Hadoop
* Kaggle
* Kivy
* linkedin/wherehows
* mlpack
* model-describer
* netron
* Numba
* opencv-python
* pillow
* portia
* pybrain
* pydgraph
* pyqt
* python mapper
* scvelo
* sympy
* theano


## Construit avec

* [Pelican](https://github.com/getpelican/pelican) - Moteur de templates
* [DandyDev](https://github.com/DandyDev) - Thème Bootstrap pour Pelican

## Contribuer

Les contributions se font par pull requests. Pour les contributions concernant le contenu des fiches, un bouton est disponible sur le site. Celui-ci mène directement à la page d'édition. Une fois une modification effectuée, celle-ci est passée en revue par un administrateur qui peut demander des ajustements, refuser la modification ou accepter celle-ci.

Il est aussi possible de [créer une nouvelle fiche](https://github.com/ecos-umons/catalogue-python/new/master/content/markdowns). Pour ce faire, il peut être interéssant de s'inspirer d'une fiche existante ou d'avoir ce README.md disponible.

N'oubliez pas d'ajouter votre nom à la liste des rédacteurs lors d'une première proposition.

## Licence

Licence WTFPL

## Remerciements

* Decan 1.
