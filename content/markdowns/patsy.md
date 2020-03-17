Title: Patsy
Created: 2012-07-10
Pip: patsy
Tags: statistique, autre outil
Source_url: https://github.com/pydata/patsy
Documentation_url: https://patsy.readthedocs.io/en/latest/
Sheet_creation: 2020-01-14
Redactors: André B.
Updated: 2020-03-03
Licenses: BSD



Patsy est une librairie permettant la description de modèles statistiques (comportant un facteur linéaire) et permettant de construire des matrices de design. Celles-ci peuvent définir une régression ou une appartenance à des groupes.

La syntaxe utilisée est inspirée et compatible avec celle du mini-langage `formula` rencontré en R et en S. Les matrices ainsi créées, définissant des modèles, peuvent être utilisées par des librairies de statistiques.

Par exemple, pour faire une régression de y en fonction de x,a,b ainsi que l'interaction entre a et b, on écrit :

```python
desc = ModelDesc.from_formula("y ~ (a + b + c + d) ** 2")
desc.describe()
```

De plus, Patsy permet :

* D'utiliser du code Python de façon arbitraire (utilisation de log(x) dans une formule)
* Des options pour les catégories, permettant la détection et la suppression automatique de doublons
* D'effectuer une même transformation à différents ensembles de données, même pour la normalisation
* De gérer des jeux de données conséquents ne tenant pas en mémoire
* De construire des matrices de contraintes linéaires dans un langage intelligible
* D'utiliser une API simple pour l'intégration dans d'autres modules Python
