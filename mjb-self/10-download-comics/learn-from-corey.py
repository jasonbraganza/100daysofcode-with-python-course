""" follow along with Corey at https://www.youtube.com/watch?v=ng2o98k983k"""


import csv

# Import Stuff we need to process the file
import requests
from bs4 import BeautifulSoup

# Now create a file to save all this data to.


source = requests.get("https://coreyms.com").text
soup = BeautifulSoup(source, "lxml")
csv_file = open("Corey’s Posts.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video_link"])
for article in soup.find_all("article"):
    headline = article.h2.a.text

    summary = article.find("div", class_="entry-content").p.text

    try:
        video_source = article.find("iframe")["src"]
        video_id = video_source.split("/")[-1]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"

    except TypeError:
        youtube_link = f"No video found."

    csv_writer.writerow([headline, summary, youtube_link])
csv_file.close()
