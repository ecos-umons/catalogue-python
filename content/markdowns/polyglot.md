Title: Polyglot
Created: 2014-07-08
Pip: polyglot
Tags: nlp
Website_url: http://polyglot-nlp.com
Source_url: https://github.com/aboSamoor/polyglot
Documentation_url: https://polyglot.readthedocs.io/en/latest/
Sheet_creation: 2020-02-06
Redactors: André B.
Updated: 2020-03-04
Licenses: GPLv3+



Polyglot est une librairie de compréhension du texte, supportant de très nombreuses langues.

En particulier, Polyglot offre les fonctions suivantes, toujours accessibles avec des appels de très haut niveau (typiquement en une commande) :

* Tokenisation (165 langues)
* Reconnaissance de la langue  (196 langues)
* Reconnaissance d'entités nommées (lieux, personnes, ...) (40 langues)
* Étiquettage de la parole (reconnaissance des fonctions grammaticales) (16 langues)
* Analyse de sentiments (connotation positive ou négative) (136 langues)
* Proposition de mots semblables (synonymes) (137 langues)
* Analyse morphologique (décomposition en morphèmes)(135 langues)
* Traduction (69 langues)

L'utilisation se fait à très haut niveau, comme mis en avant dans cet exemple tiré de la documentation :

```python
text = Text(u"In Großbritannien war Gandhi mit dem westlichen Lebensstil vertraut geworden")
print(text.entities)
[I-LOC([u'Gro\xdfbritannien']), I-PER([u'Gandhi'])]
```
