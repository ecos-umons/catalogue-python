Title: Pattern
Created: 2011-03-15
Pip: pattern
Tags: visualisation, nlp, machine learning, acquisition
Website_url: https://www.clips.uantwerpen.be/pages/pattern
Source_url: https://github.com/clips/pattern
Documentation_url: https://www.clips.uantwerpen.be/pages/pattern-dev
Sheet_creation: 2019-12-03
Redactors: André B.
Updated: 2020-03-03
Licenses: BSD




Pattern est un module de de data mining sur le web. Il comporte des outils pour Google, Twitter, l'API Wikipedia, le web et l'HTML. Il y a également des outils pour le traitement de la langue, pour l'apprentissage automatique, l'analyse de dépendances et certaines graphiques en HTML Canvas.

Plus de 50 exemples sont proposés et le tout est couvert par plus de 350 tests unitaires.

Pattern est découpé en 6 modules :

* pattern.web : Outils accédant aux différentes APIs, permettant le traitement de l'HTML et proposant un robot d'indexation.
* pattern.en : Outils de NLP (Natural Language Processing) pour l'anglais. Ils utilisent des modèles statistiques donnant un résultat rapide mais parfois incorrect.
* pattern.search : Algorithme cherchant une séquence de mots (n-grams) dans un texte étiquetté
* pattern.vector : Outils d'apprentissage automatique
* pattern.graph : Graphiques représentant les relations entre différents nœuds (mots, concepts, ...). Ces graphiques sont exportables en animations HTML Canvas. En voici un exemple tiré du site de Pattern :


![Alt Text]({static}/res/pattern_graph5.jpg)


Attention : le site web de pattern n'est pas à jour (mentionnant la version 2.6).
