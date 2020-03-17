Title: Joblib
Created: 2009-09-01
Pip: joblib
Tags: pipeline
Source_url: https://github.com/joblib/joblib
Documentation_url: https://joblib.readthedocs.io/en/latest/
Sheet_creation: 2020-01-12
Redactors: André B.
Updated: 2020-02-19
Licenses: BSD



Joblib est un ensemble d'outils légers pour le pipelining en Python. En particulier, Joblib offre un service de mise en cache de fonctions, de mémoization, et du parralélisme simple.

De cette façon, Joblib promet d'éviter de calculer la même chose deux fois, sans avoir à préparer une solution sur mesure. Joblib assure aussi une persistance grâce à un cache. De cette façon, relancer une application après un crash est facilité. Le tout est proposé sans devoir adapter son workflow (pas de framework ni de paradigme spécifique).

Même si Joblib n'a pas de dépendance, les fonctions ont été pensées et optimisées pour une utilisation de NumPy. De plus, même si le flux est à définir de bout en bout, il est possible d'intercepter et d'analyser les résultats intermédiaires ainsi que le coût de chaque étape de calcul.

Voici un exemple de gain de temps de calcul grâce à Joblib (repris de la documentation) :

```python
>>> from joblib import Memory
>>> cachedir = 'your_cache_dir_goes_here'
>>> mem = Memory(cachedir)
>>> import numpy as np
>>> a = np.vander(np.arange(3)).astype(np.float)
>>> square = mem.cache(np.square)
>>> b = square(a)                                   
________________________________________________________________________________
[Memory] Calling square...
square(array([[0., 0., 1.],
       [1., 1., 1.],
       [4., 2., 1.]]))
___________________________________________________________square - 0...s, 0.0min

>>> c = square(a)
>>> # L'appel ci-dessus n'a pas necéssité de calcul
```
