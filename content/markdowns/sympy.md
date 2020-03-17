Title: Sympy
Created: 2008-04-01
Pip: sympy
Tags: calcul numérique
Website_url: https://www.sympy.org/en/index.html
Source_url: https://github.com/sympy/sympy
Documentation_url: https://docs.sympy.org/latest/index.html
Sheet_creation: 2019-12-03
Redactors: André B.
Updated: 2020-03-04
Licenses: BSD



Sympy est une librairie pour les mathématiques, utilisant des symboles. Son but est d'être un système algébrique (computer algebra system, CAS en anglais) complet, tout en gardant le code le plus simple possible. Sympy se base sur mpmath. D'autres librairies peuvent être utilisées pour la représentation graphique.

Voici un exemple d'utilisation tiré de la documentation :
```python
>>> from sympy.solvers import solve
>>> from sympy import Symbol
>>> x = Symbol('x')
>>> solve(x**2 - 1, x)
[-1, 1]
```
