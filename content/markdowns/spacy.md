Title: spaCy
Created: 2015-01-25
Pip: spacy
Tags: nlp
Website_url: https://spacy.io
Source_url: https://github.com/explosion/spaCy
Documentation_url: https://spacy.io/api
Sheet_creation: 2020-02-10
Redactors: André B.
Updated: 2020-03-04
Licenses: MIT



spaCy est une librairie du traitement du langage (NLP), fonctionnant en Python et Cython. L'intention est de, sur base de l'état actuel de la recherche, proposer un outil de NLP permettant de créer des produits d'une qualité industrielle.

spaCy, contrairement à NLTK ou CoreNLP, n'est pas destiné à la recherche. C'est pour cette raison que la configuration (choix entre différents algorithmes aux résultats très similaires) est simplifiée. De plus, des modèles (pour différentes langues) pré-entraînés sont proposés à l'installation.

## Fonctionnalités

* Tokenisation (non destructive) : Division d'un texte en mot, éléments de ponctuation, etc.
* Reconnaissance d'entités nommés : Identification de lieux, personnes, sociétés, etc, connus.
* Support de plus de 50 langues.
* Modèles pré-entraînés disponibles.
* Efficacité (rapidité) optimisée : Utilisation des réçentes découvertes dans le domaine.
* Intégration facilitée avec le deep learning
* Étiquetage : Découverte du rôle grammaticale des différents mots du texte.
* Interprétation des mots en fonction du contexte syntaxique
* Découpage de phrases par la syntaxe
* Représentations graphiques de la syntaxe et des entités reconnues.
* Fonctions de hachage
* Export vers les tableaux numpy
* Sérialisation binaire efficace (conversion en fichiers)
* Export et utilisation de modèles facilités
* Précision (controlée)
