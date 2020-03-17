Title: HoloViews
Created: 2015-03-17
Pip: holoviews
Tags: visualisation
Website_url: https://www.holoviews.org/
Source_url: https://github.com/holoviz/holoviews
Documentation_url: https://www.holoviews.org/getting_started/index.html
Sheet_creation: 2020-01-10
Redactors: André B.
Updated: 2020-02-19
Licenses: BSD



HoloViews est une librairie travaillant sur la visualisation et l'analyse de données. Les représentations sont dérivées d'annotations qu'il faut ajouter aux données.

HoloViews peut utiliser Bokeh, Matplotlib ou Plotly pour la représentation, ce qui permet une grande diversité de graphiques, éventuellement interactifs.

Pour une découverte interactive, HoloViews propose des jauges en fonction des dimensions à explorer.

Voici un aperçu de code (sorti du contexte de la création des données qui n'est pas couverte par HoloViews) :

```python
choropleth = hv.Polygons(counties, ['lons', 'lats'], [('detailed name', 'County'), 'Unemployment'])

# Options graphiques
choropleth.opts(
    opts.Polygons(logz=True, tools=['hover'], xaxis=None, yaxis=None,
                   show_grid=False, show_frame=False, width=500, height=500,
                   color_index='Unemployment', colorbar=True, toolbar='above', line_color='white'))
```

Et ainsi le résultat associé :

![Alt Text]({static}/res/holoviews.png)
