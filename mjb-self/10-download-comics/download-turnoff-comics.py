"""
The problem
Write a command line tool to download the latest comics from https://turnoff.us/
"""

import feedparser
import requests

# get the rss feed from Turn off
# for the whole feed - key values - dict_keys(['feed', 'entries', 'bozo', 'headers', 'updated', 'updated_parsed', 'href', 'status', 'encoding', 'version', 'namespaces'])
# for each entry - key values - dict_keys(['title', 'title_detail', 'summary', 'summary_detail', 'published', 'published_parsed', 'links', 'link', 'id', 'guidislink', 'tags'])

turnoff_feed = feedparser.parse("https://turnoff.us/feed.xml")

# print(f"Last entry on the blog is {(turnoff_feed["entries"][0])}")

# we’re parsing the feed, getting the list of entries and then getting the first item (the lastest post), then looking for the summaryr in article’s meta data dictionary and that has the link to the comic, so splitting the thing and getting the url
comic = turnoff_feed["entries"][0]["summary"].split('"')[1]
comic_title = turnoff_feed["entries"][0]["title"].title()


# split the url, and get the file name, so I can name the file identically.
comic_file_name = comic.split("/")
comic_file_name = comic_file_name[-1]


# now ask requests to get the comic
get_comic = requests.get(comic)

print(f"Thel latest comic is, “{comic_title}”")
with open(comic_file_name, "wb") as f:
    f.write(get_comic.content)
print("Done saving comic")
