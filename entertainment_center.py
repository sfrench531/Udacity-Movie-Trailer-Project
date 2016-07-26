# Entertainment Center

# This code will generate an HTML webpage containing information from the
# movies provided.

# importing relevant modules, both self-generated media and instructor-provided
# fresh_tomatoes (which has been tweaked, but not significantly altered)

import media
import fresh_tomatoes


# constructing/initializing all six Movie objects with title, plot
# description, poster URL, and trailer URL

fox = media.Movie("Fantastic Mr. Fox", "Woodland animals strike back against "
                  "their human oppressors",
                  "http://0f1b361a5a35d46c59b38689aef7623c.fslcdn.net/media/spotlight/page/poster-0f39d152-d30c-455f-a94e-ee9596b9cc5b.jpg",  # noqa
                  "https://www.youtube.com/watch?v=n2igjYFojUo")

sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                       "A couple uses a new medical procedure to erase"
                       " all memories of each other after a painful breakup",
                       "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",  # noqa
                       "https://www.youtube.com/watch?v=quuMv7cGUn0")

bernie = media.Movie("Bernie", "The true story of a small Texas town rocked by"
                     " a terrible crime",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/Bernie_film_poster.jpg",  #noqa
                     "https://www.youtube.com/watch?v=YJuhWKcY_6U")


nightcrawler = media.Movie("Nightcrawler", "Jake Gyllenhaal stars as a wannabe"
                            " local news videographer who gets a little too "
                            "close to the action",
                          "http://ia.media-imdb.com/images/M/MV5BMjM5NjkzMjE5MV5BMl5BanBnXkFtZTgwNTMzNTk4MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=X8kYDQan8bw")

short = media.Movie("Short Term 12", "A social worker at a group home helps "
                    "troubled children while struggling to come to terms "
                    "with her own difficult childhood",
                    "https://upload.wikimedia.org/wikipedia/en/b/b8/Short_Term_12.jpg",  # noqa
                    "https://www.youtube.com/watch?v=qhS6tvSb0UQ")

welcome = media.Movie("Welcome To Me", "After she wins the lottery, an "
                      "eccentric woman uses her prize money to make a TV"
                      " show about her life",
                      "http://blogs-images.forbes.com/markhughes/files/2015/05/Welcome-to-Me-1.jpg",  # noqa
                      "https://www.youtube.com/watch?v=r0KEe-hMsLg")

# using fresh_tomatoes method to create and open HTML webpage
# note: required list of Movies is created within function call

fresh_tomatoes.open_movies_page(
    [fox, sunshine, bernie, nightcrawler, short, welcome])
