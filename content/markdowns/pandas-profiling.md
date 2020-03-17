Title: Pandas Profiling
Created: 2016-01-24
Pip: pandas-profiling
Tags: exploration, statistique
Source_url: https://github.com/pandas-profiling/pandas-profiling
Documentation_url: https://pandas-profiling.github.io/pandas-profiling/docs/
Sheet_creation: 2019-12-02
Redactors: André B.
Updated: 2020-03-03
Licenses: MIT



Pandas profiling permet de produire un rapport HTML interactif à partir d'un DataFrame produit par pandas. Pandas propose df.describe(); cette librairie ajoute df.profile_report() pour une analyse rapide. Des exemples sont proposé dans la documentation, tel que https://pandas-profiling.github.io/pandas-profiling/examples/russian_vocabulary/russian_vocabulary.html .

Voici ce qui peut être trouvé dans ce rapport :

* Les essentiels : type, valeurs uniques, valeurs manquantes
* Les quartiles (min, Q1, médiane, Q3, max, écart interquartile)
* Des statistiques descriptives (moyenne, valeur dominante, déviation, somme, médiane, déviation absolue, coefficient de variation, coefficient d'acuité, asymétrie)
* Les valeurs les plus courantes
* Des histogrammes
* Une mise en évidence de variables corrélées, des matrices de Spearman, Pearson et Kendall
* Des valeurs manquantes (matrices, comptage, heatmap, dendogramme)

Ce projet est indépendant de Pandas.
