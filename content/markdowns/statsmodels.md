Title: statsmodels
Created: 2011-06-14
Pip: statsmodels
Tags: statistique
Website_url: http://www.statsmodels.org/devel/
Source_url: https://github.com/statsmodels/statsmodels
Documentation_url: https://spacy.io/api
Sheet_creation: 2020-02-10
Redactors: André B.
Updated: 2020-03-04
Licenses: BSD



statsmodels est un module Python visant à complèter SciPy, en terme de statistique descriptive, d'économétrie, d'estimation ou d'inférence (se basant à chaque fois sur un modèle pertinent).

```python
import numpy as np
import statsmodels.api as sm

# Génération de données fictives (2 régresseurs + constante)
nobs = 100
X = np.random.random((nobs, 2))
X = sm.add_constant(X)
beta = [1, .1, .5]
e = np.random.random(nobs)
y = np.dot(X, beta) + e

# Apprentissage
results = sm.OLS(y, X).fit()

# Inspection des résultats
print(results.summary())
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.298
Model:                            OLS   Adj. R-squared:                  0.283
Method:                 Least Squares   F-statistic:                     20.57
Date:                Wed, 22 Jan 2020   Prob (F-statistic):           3.58e-08
Time:                        18:54:03   Log-Likelihood:                -18.273
No. Observations:                 100   AIC:                             42.55
Df Residuals:                      97   BIC:                             50.36
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.4687      0.070     20.862      0.000       1.329       1.608
x1             0.0507      0.096      0.528      0.599      -0.140       0.241
x2             0.6083      0.097      6.269      0.000       0.416       0.801
==============================================================================
Omnibus:                       57.347   Durbin-Watson:                   2.386
Prob(Omnibus):                  0.000   Jarque-Bera (JB):                7.214
Skew:                           0.072   Prob(JB):                       0.0271
Kurtosis:                       1.692   Cond. No.                         4.71
==============================================================================
```





## Fonctionnalités

* Des modèles de régression linéaire supplémentaires
* Un modèle linéaire mixte (sur les effets et la variance)
* Des modèles linéaires généralisés (GLM) avec un support pour les distributions de type exponentiel à un facteur
* Un GLM Baysésien Mixte pour la distributions polynomiales et de Poisson
* Une estimations d'équations généralisées (GEE) pour les données longitudinales
* Des modèles discrets (logit, probit, Poisson, Régression Binomiale Négative)
* Modèles Linéaires Robustes (RLM)
* Analyse des séries temporelles (modèles StateSpace, chaînes de Markov, ARIMA, VAR, VECM, ...)
* Analyse de survie (Vox, Kaplan-Meier)
* Outils supplémentaires d'analyse multivariée
* Statistiques sans paramètre
* Tests statistiques additionnels
* Jeux de données pour exemples et tests
* MICE
* Graphiques supplémentaires
* Outils pour les flux (lecture de .dta, bien qu'en retard sur pandas, export vers ascii, latex et html)
* Modèles divers
* Des exemples dans différents stades de développement pour un découverte de la librairie
