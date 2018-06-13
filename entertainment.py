import fresh_tomatoes
import media


black_panther = media.Movie("Black Panther",
                            "A new king must defend his nation from outside"
                            " threats.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

get_out = media.Movie("Get Out",
                      "A thriller about a black man meeting his white"
                      " girlfriend's family.",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/Teaser_poster_for_2017_film_Get_Out.png",  # NOQA
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

creed = media.Movie("Creed",
                    "The son of Apollo Creed has a lot to prove when he wants"
                    " to be a professional boxer.",
                    "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Uv554B7YHk4")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "A ragtag group must work together to"
                                      " save the galaxy.",
                                      "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",  # NOQA
                                      "https://www.youtube.com/watch?v=2LIQ2-PZBC8")  # NOQA

dark_knight = media.Movie("The Dark Knight",
                          "When the Joker incites chaos in Gotham, Batman"
                          " must stop him.",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

forrest_gump = media.Movie("Forrest Gump",
                           "Several historical events are retold through the"
                           " life of one man.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

lion_king = media.Movie("The Lion King",
                        "A lion returns from self-exile to assume his late"
                        " father's throne.",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=V6jOvVf05aQ")

mulan = media.Movie("Mulan",
                    "A woman disguised as a male warrior fills in for her"
                    " father and saves China.",
                    "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",  # NOQA
                    "https://www.youtube.com/watch?v=MsAniqGowKE")


movies = [black_panther, get_out, creed, guardians_of_the_galaxy, dark_knight,
          forrest_gump, lion_king, mulan]
fresh_tomatoes.open_movies_page(movies)
