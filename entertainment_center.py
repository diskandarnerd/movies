#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:22:57 2017

@author: dannyiskandar
"""
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
grease = media.Movie("Grease the movie",
                     "A movie about singing, dancing and romance in the high school setting",
                     "https://upload.wikimedia.org/wikipedia/en/e/e2/Grease_ver2.jpg",
                     "https://www.youtube.com/watch?v=f2CCEixOVVU")
#print(grease.storyline)
#grease.show_trailer()

arrival = media.Movie("Arrival",
                     "A movie about alien visiting earth and teaching human how to life",
                     "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

threeidiots = media.Movie("3idiots",
                     "3 idiots is having fun discovering what life is about, a very poetic and fun movie",
                     "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w")

lifeofpie = media.Movie("Lifeofpie",
                     "The life of a brave young boy, discovering himself about his own limitations and the importance of letting go",
                     "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                     "https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

movies = [toy_story, avatar, grease, arrival, threeidiots, lifeofpie]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
