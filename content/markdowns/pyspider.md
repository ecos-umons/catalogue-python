Title: pyspider
Created: 2014-11-24
Pip: pyspider
Tags: acquisition
Source_url: https://github.com/binux/pyspider
Documentation_url: http://docs.pyspider.org/en/latest/
Sheet_creation: 2020-02-06
Redactors: André B.
Updated: 2020-03-04
Licenses: Apache 2.0



pyspider est une librairie proposant un robot d'indexation paramétrable en Python. Une fois le script rédigé, une interface web permet d'explorer les résultats et processus en cours. L'architecture de pyspider permet une utilisation distribuée.

![Alt Text]({static}/res/pyspider.png)


Les différentes informations des pages webs sont disponibles sous le format pyquery, semblable au format j-Query.

La fréquence d'indexation ainsi que la durée de vie des informations sont complètement paramétrables (ici, avec une durée de vie de 10 jours) :

```Python
from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://scrapy.org/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
```
