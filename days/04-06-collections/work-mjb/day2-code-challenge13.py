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


# make a movie placeholder namedtuple template to hold movie date
Movie = collections.namedtuple("Movie", "title year score")

# also lets make variables to hold the constraints that we want (minimum year and the number of movies)
min_movies = 4
min_year = 1960
movie_directors = collections.defaultdict(list)

# ok, now the first thing to do is probably read in the file?
def process_movie_file():
    # next up, get rid of the pieces we don’t want and create a dict of the pieces we do (key is the director, while values are the movie name, year, and the imdb score)
    # creating a default dict, to hold all our values.
    with open("movie_metadata.csv") as read_in:
        read_in_object = csv.DictReader(read_in)
        for each_line in read_in_object:
            try:
                director = each_line["director_name"]
                movie_name = each_line["movie_title"].replace(
                    "\xa0", ""
                )  # the replace thingie replaces the weird non-breaking spaces at the end of the titles with nothing
                movie_year = int(each_line["title_year"])  # make sure it is a number
                movie_score = float(
                    each_line["imdb_score"]
                )  # make sure it is a decimal number
            except ValueError:  # some years are empty
                continue
            if (
                movie_year < min_year
            ):  # if a year is older than my mininimum year, discard line and continue looping
                continue

            # next assemble the movie related variables into a tuple
            m = Movie(title=movie_name, year=movie_year, score=movie_score)
            movie_directors[director].append(m)
    return movie_directors


def calculate_avg_movie_score(movies):
    """Calculate average scores for each director"""
    ratings = [
        m.score for m in movies
    ]  # make a list of all the movie scores of the specific director
    average = sum(ratings) / max(
        1, len(ratings)
    )  # add the list and divide by the number of items in the list. the max is to avoid divide by zeros
    return round(average, 1)  # round to the nearest number


def best_director(movie_directors):
    """run through the list and then average the movie scores and then rank them"""
    the_list = {
        director: calculate_avg_movie_score(movies)
        for director, movies in movie_directors.items()
        if len(movies) >= min_movies
    }
    print(sorted(the_list.items(), key=lambda x: x[1], reverse=True))


if __name__ == "__main__":
    """ get the best director based on their imdb ratings"""
    process_movie_file()
    best_director(movie_directors)
