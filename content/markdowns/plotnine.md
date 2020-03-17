Title: Plotnine
Created: 2017-04-22
Pip: plotnine
Tags: visualisation
Website_url: https://plotnine.readthedocs.io/en/stable/about-plotnine.html
Source_url: https://github.com/has2k1/plotnine
Documentation_url: https://plotnine.readthedocs.io/en/stable/
Sheet_creation: 2019-10-28
Redactors: André B.
Updated: 2020-03-04
Licenses: GPLv2



Plotnine est une librairie permettant de construire des graphiques selon la même grammaire que `ggplot2`, en R. Le fait d'avoir la même syntaxe de création aide au port ou à la transition de R à Python. De plus, cette grammaire a été réfléchie pour limiter l'effort mental nécessaire à la création de graphiques complexes, tout en restant simple pour des graphiques basiques.

Plotnine a été construit par-dessus matplotlib, une librairie largement éprouvée. De cette façon, le module profite de sa robustesse et permet d'utiliser l'API de matplotlib pour des cas qui ne seraient pas couverts par la grammaire proposée.

Voici un exemple tiré de la documentation, mettant en avant la grammaire de graphiques venant de `ggplot2` :

```Python
from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))
```

![Alt Text]({static}/res/plotnine.png)


La plupart des différentes ressources d'apprentissage externes proposées sur le site n'existent plus.

## Fonctionnalités

* Grammaire ggplot2
* Production rapide de graphiques
* Ajouts esthétiques
* Possibilité d'ajout de watermark (signature)
* Animations
* Sauvegarde dans un fichier pdf
* Différents thèmes
* De nombreux graphiques classiques
* Support de différents systèmes de coordonées
* Divers jeux de données pour tester les graphiques
