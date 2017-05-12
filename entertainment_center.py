import media
import fresh_tomatoes

# create 6 Movie instances all movie titles have been included with the rating
toy_story = media.Movie("Toy Story [" + media.Movie.VALID_RATING[0] + "]",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/Y53GeP",
                        "https://goo.gl/MuLPSm")

avatar = media.Movie("Avatar [" + media.Movie.VALID_RATING[2] + "]",
                     "A marine on an alien planet",
                     "https://goo.gl/175IoT",
                     "https://goo.gl/5WUckU")

inception = media.Movie("Inception [" + media.Movie.VALID_RATING[2] + "]",
                        "A story about dream",
                        "https://goo.gl/yjjvvm",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

pulp_fiction = media.Movie("Pulp Fiction[" + media.Movie.VALID_RATING[3] + "]",
                           "Consists of three interrelated stories",
                           "https://goo.gl/IkSLOu",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

fight_club = media.Movie("Fight Club [" + media.Movie.VALID_RATING[3] + "]",
                         "A depressed man try to destroy the world",
                         "https://goo.gl/02bxfw",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

interstellar = media.Movie("Interstellar[" + media.Movie.VALID_RATING[1] + "]",
                           "A story about exploring the universe",
                           "https://goo.gl/dnUCK7",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Add the 6 Movie instances into movies list and pass into fresh_tomatoes
# open_movies_page method
movies = [toy_story, avatar, inception, pulp_fiction, fight_club, interstellar]
fresh_tomatoes.open_movies_page(movies)
