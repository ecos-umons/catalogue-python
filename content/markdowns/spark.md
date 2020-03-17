Title: Spark
Created: 2010-10-04
Pip: pyspark
Tags: acquisition, data mining, machine learning, statistique
Website_url: https://spark.apache.org/
Source_url: https://github.com/apache/spark/tree/master/python
Documentation_url:http://spark.apache.org/docs/latest/api/python/index.html
Sheet_creation: 2020-03-06
Redactors: André B.
Updated: 2020-03-06
Licenses: Apache Software License


Spark est un système de calcul distribué efficace et généraliste, visant le domaine du Big Data. Le cœur de Spark contient des routines de calcul optimisées pour l'analyse de données, avec des API, ici en Python.

Le principal apport est l'objet Resilient Distributed Dataset (RDD) qui fourni une abstraction sur les données. Le fait que celles-ci soient distribuées est ainsi caché au développeur.

Spark s'intégre avec quatres outils principalement :

* Spark SQL pour SQL et les DataFrames
* MLlib pour le machine learning (classification, clustering, éveluation, régression, ...)
* GraphX pour la manipulation de graphes
* Spark Streaming pour les données en streaming (kafka, kinesis, flume, ...)


Attention : le paquet Python permet d’interagir avec un cluster Spark existant, pas d'en déployer un.
