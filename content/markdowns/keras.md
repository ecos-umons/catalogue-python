Title: Keras
Created: 2015-10-11
Pip: Keras
Tags: machine learning
Source_url: https://github.com/keras-team/keras
Documentation_url: https://keras.io/
Sheet_creation: 2020-01-12
Redactors: André B.
Updated: 2020-02-20
Licenses: MIT



Keras est une librairie permettant la création de réseaux de neurones à haut-niveau. Keras utilise Tensorflow, CNTK ou Theano en interne. Le but est de permettre un prototypage rapide. Keras supporte les réseaux convolutifs, récursifs et tourne aussi bien sur le CPU que la GPU.

Principes fondamentaux de Keras :

* Facilité d'utilisation : l'API est réfléchie pour des humains en réduisant l'effort mental pour retenir les concepts qui y sont liés. En cas de problème, une erreur explicite et utile est proposée.
* Modularité : Les couches de neurones, fonctions de coût, d'activation, optimisations sont vues comme des modèles qui peuvent être assemblés pour créer un nouveau modèle.
* 100% Python : Le code est compact et Keras ne nécéssite pas de fichier de configuration dans un autre langage.


La totalité du prototypage peut se faire en quelques lignes :
```python
# Imports
from keras.models import Sequential
from keras.layers import Dense

# Création du modèle
model = Sequential()

# Ajout de couches
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# Configuration du mode d'apprentissage
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Entrainement
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluation
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# Prédictions
classes = model.predict(x_test, batch_size=128)
```

En plus de modèle séquentiel, présenté ci-dessus, il existe une API fonctionnelle, permettant de créer un réseau de neurone plus complexe (couches partagées, graphique acycliques dirigés, sorties multiples, ...).

Keras propose les fonctions d'activation courantes, ou plus avancée, tant qu'elles se trouvent dans TensorFlow/Theano/CNTK.

Les couches quand à elles sont par dizaines et, dans le cas ou un besoin spécifique n'est pas rencontré, il reste possible de définir une couche avec une expression lambda ou par héritage de la classe `keras.layers.Layer`.
