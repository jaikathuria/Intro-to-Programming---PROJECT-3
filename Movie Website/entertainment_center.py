import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                        "8.3/10",
                       "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "7.9/10",
                    "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
threeidiots = media.Movie("3 Idiots","story of 3 friends in an engineering college",
                          "8.4/10",
                          "http://www.indicine.com/movies/img/2009/10/threeidiots2.jpg",
                         "https://www.youtube.com/watch?v=K0eDlFX9GMc")
twostates = media.Movie("2 States",
                        "Coming from two very different cultural backgrounds, Krish and Ananya decide that they won't get married until they convince their parents",
                        "7/10",
                        "http://www.filmapia.com/sites/default/files/filmapia/pub/movie/posters/1401170120_12fe3cbe_2-states-poster-612x884.jpg",
                       "https://www.youtube.com/watch?v=CGyAaR2aWcA")
batman_begins = media.Movie("Batman Begins",
                           "Bruce Wayne returns as Batman to eliminate crime from Gotham.",
                            "8.3/10",
                           "http://www.impawards.com/2005/posters/batman_begins_ver3.jpg",
                           "https://www.youtube.com/watch?v=neY2xVmOfUM")
yaar_annmulle = media.Movie("Yaar Annmulle",
                 "Guri, Deep and Sher Singh are three university friends living in a hostel. They experience all aspects of friendship like bunking classes, dealing with rival groups and matters of the heart.",
                            "7.4/10",
                 "http://www.toptenscentral.com/wp-content/uploads/2015/04/Yaar-Anmulle-punjabi-film.jpg",
                 "https://www.youtube.com/watch?v=6RE_q4bqxS0")

movies = [toy_story, avatar, threeidiots, twostates, batman_begins, yaar_annmulle]
fresh_tomatoes.open_movies_page(movies)
