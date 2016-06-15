import feedparser

FEED_URL = 'http://rss.weather.yahoo.co.jp/rss/days/4410.xml'

class Feed:
    def fetch(self):
        feed = feedparser.parse(FEED_URL)
        return feed.entries[0].description
