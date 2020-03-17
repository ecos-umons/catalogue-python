Title: TensorFlow
Created: 2015-11-09
Pip: tensorflow
Tags: machine learning
Website_url: https://www.tensorflow.org/
Source_url: https://github.com/tensorflow/tensorflow
Documentation_url: https://www.tensorflow.org/api_docs/python/tf
Sheet_creation: 2020-02-11
Redactors: André B.
Updated: 2020-03-05
Licenses: Apache 2.0



TensorFlow est un ensemble d'outils et de librairies visant à supporter la recherche en machine learning et facilitant le développement d'applications concrètes.

TensorFlow était un projet de l'équipe Google Brain. Les APIs sont en Python et C++. La création de modèles est simplifiée et de nombreuses ressources en ligne existent.

En pratique, TensorFlow est principalement utilisé en conjonction avec Keras qui fournit une interface de plus haut niveau.

En voici un exemple :
```python
def get_compiled_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
  ])

  model.compile(optimizer='adam',
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model
```


TensorFlow est utilisé par airbnb, Coca-Cola, intel, Google, Twitter, LindekIn, Snapchat, Uber,...

TensorFlow permet entre autres :

* De construire facilement un modèle (pour la classification, la régression)
* De surveiller le surentraînement ou le sousentraînement
* L'export de modèles
* D'importer et préparer les données dans de nombreux formats (CSV, NumPy, pandas, images, texte, ...)
* De personnaliser les tenseurs, modèles, opérations
* D'entraîner le modèle de façon distribuée
* De créer des générateurs (par exemple, Deep Dream)
* De traîter des données numériques, du texte, des images, des fichiers sonores
