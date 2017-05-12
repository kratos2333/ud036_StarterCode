import media
import fresh_tomatoes

# create 6 Movie instances all the movie title has been included with the rating
toy_story = media.Movie("Toy Story [" + media.Movie.VALID_RATING[0] + "]",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&list=PLFAlnWe4T8GvZ8sUgKhWv2Tq--FCieOTP")

avatar = media.Movie("Avatar [" + media.Movie.VALID_RATING[2] + "]",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&list=PLXZoqTfS5CfaoQ_j24jCrOWSszIOkn6qx")

inception = media.Movie("Inception [" + media.Movie.VALID_RATING[2] + "]",
                        "A story about dream",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

pulp_fiction = media.Movie("Pulp Fiction [" + media.Movie.VALID_RATING[3] + "]",
                           "Consists of three interrelated stories",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

fight_club = media.Movie("Fight Club [" + media.Movie.VALID_RATING[3] + "]",
                         "A depressed man with split personality try to destroy the world",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

interstellar = media.Movie("Interstellar [" + media.Movie.VALID_RATING[1] + "]",
                           "A story about exploring the universe",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")
                           
# Add the 6 Movie instances into movies list and pass into fresh_tomatoes open_movies_page method
movies = [toy_story,avatar,inception,pulp_fiction,fight_club,interstellar]
fresh_tomatoes.open_movies_page(movies)

