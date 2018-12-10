import scrapy
from bs4 import BeautifulSoup

class Spotify(scrapy.Spider):
    name = "Spotify"
    start_urls = ["https://open.spotify.com/playlist/4hOKQuZbraPDIfaGbM3lKI"]

    def parse(self, response):
        print("start printing results...\n\n\n")
        trackSelector = "li.tracklist-row"
        # pretty = BeautifulSoup(response.css(trackSelector).extract(), 'html.parser')
        # print(pretty.prettify())
        for track in response.css(trackSelector):
            BeautifulSoup(track.extract()).prettify()
            yield {
                "Name": track.css("span.track-name ::text").extract(),
                # intential cutting last element because it is a repeating
                # track name
                "Artist": track.css("span a ::text").extract()[:-1]
            }

