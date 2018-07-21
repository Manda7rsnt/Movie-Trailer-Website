import fresh_tomatoes
import media


def main():
    """This creates Movie objects and initializes them with the data"""
    toy_story = media.Movie("Toy Story",
                            "1h 21min",
                            "A story of a boy and his toys that come to life",
                            "Animation, Adventure, Comedy",
                            "22 November 1995",
                            "Tom Hanks, Tim Allen, Don Rickles",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                            "http://www.youtube.com/watch?v=vwyZH85NQC4")

    oceans_eleven = media.Movie("Oceans 11",
                                "1h 56min",
                                "Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously",  # NOQA
                                "Crime, Thriller",
                                "7 December 2001 (USA)",
                                "George Clooney, Brad Pitt, Julia Roberts",
                                "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=imm6OR605UI")

    transformers = media.Movie("Transformers",
                               "2h 24min",
                               "An ancient struggle between two Cybertronian races",  # NOQA
                               "Adventure,Sci-Fi",
                               "3 July 2007 (USA)",
                               "Shia LaBeouf, Megan Fox, Josh Duhamel",
                               "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=HKi0xnV4ZjM")

    twelve_angry_men = media.Movie("12 Angry Men",
                                   "1h 36min",
                                   "A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence",  # NOQA
                                   "Crime, Drama",
                                   "April 1957 (USA)",
                                   "Henry Fonda, Lee J. Cobb, Martin Balsam",
                                   "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=Dosg0p7LAB4")  # NOQA

    madagascar = media.Movie("Madagascar",
                             "1h 26min",
                             "Spoiled by their upbringing and unaware of what wildlife really is, four animals from the New York Central Zoo escape to Madagascar",  # NOQA
                             "Animation, Adventure, Comedy",
                             "27 May 2005 (USA)",
                             "Chris Rock, Ben Stiller, David Schwimmer",
                             "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=_FvCgabQVjA")

    iceage = media.Movie("Ice Age",
                         "1h 21min",
                         "Set during the Ice Age, a sabertooth tiger, a sloth, and a wooly mammoth find a lost human infant, and they try to return him to his tribe",  # NOQA
                         "Animation, Adventure, Comedy",
                         "15 March 2002 (USA)",
                         "Denis Leary, John Leguizamo, Ray Romano",
                         "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=cMfeWyVBidk")

    # Create a list of movies
    movies = [toy_story, oceans_eleven, transformers, twelve_angry_men,
              madagascar, iceage]

    # Use the function to create html file to show the movie details in webpage
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
