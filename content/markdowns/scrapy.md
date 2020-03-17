Title: Scrapy
Created: 2009-09-17
Pip: Scrapy
Tags: acquisition, data mining
Website_url: https://scrapy.org/
Source_url: https://github.com/scrapy/scrapy
Documentation_url: https://docs.scrapy.org/en/latest/
Sheet_creation: 2020-02-07
Redactors: André B.
Updated: 2020-03-04
Licenses: BSD



Scrapy est un robot d'indexation et de récupération de données structurées.

Scrapy peut être utilisé de la sorte pour du data mining, de la surveillance de site ou pour des tests automatisés.

Pour lancer une activité, il faut créer un processus (nommé spider), paramétrable en quelques lignes :

```Python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

```

Les processus lancent des requêtes web et effectuent le traitement décrit dans la spider de façon asynchrone. Différent paramètres permettant de limiter les ressources consommées par la spider sont proposés. Parmi ceux-ci, une limite au nombre de requêtes par adresse IP, un délai temporel entre deux requêtes, ...

Les données structurées ainsi récupérées sont disponibles dans des fichiers textes (JSON, XML ou CSV par exemple), ou sur différents supports (disque dur, FTP, Amazon S3,...).

De plus, des outils de débuggage sont fournis avec, tels une console Telnet, des outils pour certains processus (compression HTML, robots.txt), ou un terminal interactif.
