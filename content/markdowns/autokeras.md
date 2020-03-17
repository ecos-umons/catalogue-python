Title: AutoKeras
Created: 2017-11-30
Pip: autokeras
Tags: machine learning
Website_url: https://autokeras.com/
Source_url: https://github.com/keras-team/autokeras
Documentation_url: https://autokeras.com/tutorial/overview/
Sheet_creation: 2020-01-07
Redactors: André B.
Updated: 2020-02-18
Licenses: MIT



AutoKeras est une librairie de machine learning automatisé (AutoML). L'AutoML a pour but de rendre les outils de deep learning accessibles à des experts dans diverses disciplines ayant une compétence en machine learning limitée. AutoKeras propose des fonctions cherchant une architecture et des paramètres pour le modèle de deep learning.

Chaque type de modèle, défini par la tâche censée être accomplie, propose une interface simplissime :

```Python
import autokeras as ak

clf = ak.ImageClassifier()
clf.fit(x_train, y_train)
results = clf.predict(x_test)
```

Les tâches supportées sont :

* La classification d'images
* La régression sur des images
* La classification textuelle
* La régression sur du textuelle
* La classification de données structurées
* La régression sur des données structurées

Pour des besoins légèrement plus spécifiques, il est possible de définir une architecture à haut niveau, alors qu'AutoKeras se charge de définir plus précisémment celui-ci.

Cette définition se fait à partir de briques de base :

* **Nodes** : ImageInput, Input, StructuredDataInput, TextInput.
* **Preprocessors** : ImageAugmentation, Normalization, TextToIntSequence, TextToNgramVector, CategoricalToNumerical.
* **Blocks** : ConvBlock, DenseBlock, Embedding, Merge, ResNetBlock, RNNBlock, SpatialReduction, TemporalReduction, XceptionBlock, ImageBlock, StructuredDataBlock, TextBlock.
* **Heads** : ClassificationHead, RegressionHead.


Le modèle final peut être exporté pour être rechargé ultérieurement.
