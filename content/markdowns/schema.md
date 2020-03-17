Title: Schema
Created: 2012-08-19
Pip: schema
Tags: validation
Source_url: https://github.com/keleshev/schema
Documentation_url: https://github.com/keleshev/schema
Sheet_creation: 2019-12-04
Redactors: André B.
Updated: 2020-03-04
Licenses: MIT




Schema est une librairie de data validation. Elle permet de valider des structures provenant de fichiers de configuration, formulaires, services en lignes, commandes dans le terminal, JSON/YAML, le tout sous forme de types Python.

Schema valide :

* Le type
* Les fonctions (ou objets avec une méthode __call__) : est-ce que ça retourne True ?
* Les objets avec une méthode `validate` (exemple : Regex, faisant partie du module)
* Les listes, tableaux, dictionnaires
* Des Hooks : une paire clé:valeur, une fois trouvée, celle-ci peut déclencher une fonction. Utilisé pour détecter des valeur interdites
* Et d'autres encore
