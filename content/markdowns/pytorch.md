Title: PyTorch
Created: 2016-09-01
Pip: torch
Tags: manipulation, machine learning, calcul numérique
Website_url: https://pytorch.org/
Source_url: https://github.com/pytorch/pytorch/
Documentation_url: https://pytorch.org/docs/stable/index.html
Sheet_creation: 2020-02-07
Redactors: André B.
Updated: 2020-03-04
Licenses: BSD-3



PyTorch est une librairie proposant des tenseurs et des réseaux de neurones dynamiques rapides grâce à l'accélération graphique (GPU).

La librairie est principalement utilisée pour soit:

* Remplacer NumPy et profiter de la dite accélération graphique
* Faire de la recherche en deep learning, grâce à sa flexibilité et sa rapidité

Les réseaux de neurones dynamiques sont possibles grâce à la technique de dérivation automatique inverse et au ruban utilisé pour accélérer les calculs. Concrètement, il est possible de modifier la structure d'un réseau avec une surcharge de calcul minimale.

L'interface de PyTorch, pensée directement pour le Python, permet de l'étendre facilement via numpy, scipy,... De plus, grâce à l'exécution synchrone (permise pas les réseaux dynamiques), le débuggage est simplifié.

Plus précisémment, PyTorch est subdivisé en 6 modules :

* torch : Fonctions sur les tenseurs (comme NumPy), avec l'accélération graphique
* torch.autograd : Dérivation automatique supportant les opérations sur tenseur qui sont dérivables
* torch.jit : Ensemble d'outils de compilation (TorchScript) permettant de sérialiser et d'optimiser des modèles
* torch.nn : Réseaux de neurones, reposant principalement sur torch.autograd
* torch.multiprocessing : Partage des tâches et de la mémoire entre plusieurs processus
* torch.utils : Chargement de données et autres fonctions utilitaires
