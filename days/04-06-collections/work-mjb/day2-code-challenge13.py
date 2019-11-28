"""
There is this great ML article Predict Movie Rating. In this week's code challenge we use its data set to get the 20 highest rated directors based on their average movie IMDB ratings.

Steps:

    As mentioned in the article the dataset is here, but we provided a copy in the repo's 13/ subfolder.

    Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts from which you only need the following k,v pairs:

    OrderedDict([...
                ('director_name', 'Lawrence Kasdan'),   
                ...
                ('movie_title', 'Mumford\xa0'),
                ...
                ('title_year', '1999'),
                ...
                ('imdb_score', '6.9'),
                ...

    Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data. However going to min 5 movies we miss Sergio Leone :(

    Take movies of year >= 1960.

    Print the top 20 highest rated directors with their movies ordered desc on rating.
"""

import collections, csv

# ok, first thing to do is probably read in the file?
def process_movie_file():
    with open("movie_metadata.csv") as read_in:
        # uses orderedDict to get in and make a dictionary of all the objects, using the header as the key, such as director_name', 'Jon Gunn'
        read_in_object = csv.DictReader(read_in)
        # next up, take this object and strip it of most items
        for each_line in read_in_object:

            print(
                f'{each_line["director_name"]}, directed {each_line["movie_title"]}, in {each_line["title_year"]}, and it has a score of {each_line["imdb_score"]} on IMDB'
            )


if __name__ == "__main__":
    process_movie_file()
