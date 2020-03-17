Title: NumExpr
Created: 2009-01-23
Pip: numexpr
Tags: calcul numérique
Source_url: https://github.com/pydata/numexpr
Documentation_url: http://numexpr.readthedocs.io/en/latest/
Sheet_creation: 2020-01-14
Redactors: André B.
Updated: 2020-02-20
Licenses: MIT



NumExpr est un évaluateur à haute performance pour les expressions numériques. De cette façon, l'expression ```3*a+4*b``` est accélérée et utilise moins de mémoire lors de l'utilisation de tableau. De plus, le multithread (paramétrable via des variables d'environnement) et la répartitions sur plusieurs processeurs sont prévus, ce qui permet d'être plus performant que NumPy. Typiquement, de 2 à 4x plus rapide.

En évitant de stocker les résultats intermédiaires, la gestion du cache est améliorée et les performances le sont avec. L'utilisation est simple (ici avec des tableaux de numpy) : ``` numexpr.evaluate('a*b-4.1*a > 2.5*b') ```.

NumExpr supporte le travail avec des tableaux NumPy, ainsi que les opérations logiques, arithmétiques et de comparaisons.

Les fonctions supportées sont :

* Le test conditionnel
* Les fonctions trigonométrique (inverses), trigonométriques hyperboliques (inverses)
* arctan2
* Logarithmes
* Exponentielles
* Racine carrée
* Valeur absolue
* Créations, décomposition et conjugué de nombres complexes
* Appartenance à une chaîne de caractère

Les sommes et produits peuvent être utilisés pour une réduction accélérée.
