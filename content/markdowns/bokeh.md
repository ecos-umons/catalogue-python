Title: Bokeh
Created: 2013-04-01
Pip: bokeh
Tags: visualisation, dashboard
Website_url: https://bokeh.org/
Source_url: https://github.com/bokeh/bokeh
Documentation_url: https://docs.bokeh.org/en/latest/
Sheet_creation: 2019-11-12
Redactors: André B.
Updated: 2020-02-18
Licenses: BSD-3





Bokeh est une librairie open-source Python interactive se concentrant sur la visualisation de données en créant des présentations web dynamiques (utilisant JavaScript). Les présentations peuvent être des applications, dashboard, une exploration via les notebooks Jupyter, une visualisation de flux de données, ou un module à intégrer dans un site web.

Les graphiques sont modulaires et peuvent être construits sur mesure en fonction des guides, annotations, axes et glyphes utilisés. Dans le cas où les fonctionnalités ne sont pas suffisantes, il reste possible d'ajouter du code JavaScript spécifique.

Ici, un exemple de donut :
![Alt text]({static}/res/bokeh.png)

Cependant, il existe le module `bokeh.charts` qui propose une API à haut niveau pour la création des graphiques. Pour le moment, ce module propose les graphiques :

* Area (superposé et surimprimé)
* Bar (groupé et empilé)
* BoxPlot
* Donut
* Dot
* HeatMap
* Histogram
* Horizon
* Line
* Scatter
* Step
* Timeseries

Bokeh fonctionne avec la plupart des librairies d'analyse et de traitement de données en Python.
