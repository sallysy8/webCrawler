import scrapy
from bs4 import BeautifulSoup


class AmazonMusic(scrapy.Spider):
    name = "AmazonMusic"
    start_urls = ["https://music.amazon.com/playlists/B07WK6BSV1"]

    def parse(self, response):
        print("start printing results...\n\n\n")
        trackSelector = "tr.playlistDetailsListItem"
        #pretty = BeautifulSoup(response.css(trackSelector).extract(), 'html.parser')
        #print(pretty.prettify())
        for track in response.css(trackSelector):
            BeautifulSoup(track.extract()).prettify()
            yield {
                "Name": track.css("td.title ::text").extract()[0],
                # intential cutting last element because it is a repeating
                # track name
                "Artist": track.css("span.artist ::text").extract()[0]
            }
