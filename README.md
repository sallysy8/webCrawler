# webCrawler
## Summary
This is a web crawler using Python3 scrapy framework.  The first functionality of this crawler is to research the music popularity among different media.  Currently, we support crawling Spotify's top list.

## How to use it
### Dependencies
1. [scrapy](https://github.com/scrapy/scrapy/blob/master/README.rst)
2. Python3 (for sure)
3. [beautifulsoup](https://pypi.org/project/beautifulsoup4/)

You need to install Python3 and scrapy framework.
### To list the crawlers
Go to musicList directory, run the following command:
```scrapy list```

### To crawl
```scrapy crawl Spotify```

## Future work
In order to have concrete results, we need input from different music platforms, such as Spotify, MTV, Amazon Music, NPR and etc.  So more crawlers need to be implemented.

## Enjoy!
