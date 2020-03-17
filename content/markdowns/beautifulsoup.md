Title: Beautiful Soup
Created: 2017-11-30
Pip: beautifulsoup4
Tags: acquisition
Website_url: https://www.crummy.com/software/BeautifulSoup/
Source_url: https://code.launchpad.net/beautifulsoup
Documentation_url: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Sheet_creation: 2020-01-08
Redactors: André B.
Updated: 2020-02-18
Licenses: MIT
Stars: 80
Forks: 26
Issues: 9



Beautiful Soup est une librairie proposant une façon aisée de récupérer du contenu depuis des pages web. Reposant sur un parser XML ou HTML (lxml et html5lib), cette librairie  décompose le code source en un arbre syntaxique, rendant l'itération et la manipulation plus aisée. Beautiful Soup permet aussi de négliger l'encodage, convertissant tout en UTF-8, que ce soit lors de l'import ou de l'export.

Cependant, BeautifulSoup demande un surcoût et pour une tâche critique, l'utilisation directe du parser, tel lxml, est recommandée (par la documentation).

BeautifulSoup offre :

* Un affichage structuré dans le terminal
* L'accès aux éléments (et leur contenu, attributs) via la structure de donnée (soup)
* Récuperer tous les éléments d'un certains type (éventuellement via une regex ou une fonction spécialisée)
* Extraire le texte
* La recherche par classe CSS
* Un outil de diagnostique (sur les différentes versions de beautifulsoup et des parsers utilisés)
