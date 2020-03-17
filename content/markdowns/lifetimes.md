Title: Lifetimes
Created: 2015-02-16
Pip: Lifetimes
Tags: temporel, statistique, visualisation
Source_url: https://github.com/CamDavidsonPilon/lifetimes
Documentation_url: https://lifetimes.readthedocs.io/en/latest/
Sheet_creation: 2019-12-03
Redactors: André B.
Updated: 2020-02-20
Licenses: MIT




Lifetimes est une librairie permettant d'évaluer et de prédire la valeur totale d'un client, jusqu'à sa dernière interaction.

Cela se fait sous deux hypothèses :

* Un utilisateur qui interagi est "vivant"
* Un utilisateur peut "périr" après un certain temps.

L'estimation porte donc sur la fréquence des interactions, la valeur de chacune de celle-ci et sur la date de la dernière interaction.
Techniquement :
* Les données peuvent être lues au format CSV, Pandas ou NumPy (en plus des types Python).
* Des représentations spécialisées et préconfigurées sont proposées
* L'intervalle de confiance peut être configuré

L'analyse de fréquence la plus simple utilise le modèle BG/NBD (BetaGeo). Ici avec des données de test :
![Alt text]({static}/res/lifetimes.png)

Des matrices donnant la probabilité de survie d'un client et des graphiques permettant de comparer le modèle à la réalité sont proposés.

D'autres modèles que BG/NBD sont proposés :

* Le modèle Gamma-Gamma (prenant en compte la valeur marchande des transactions, supposées indépendantes)
* Le modèle Pareto NBD
