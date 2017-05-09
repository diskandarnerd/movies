#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:24:12 2017

@author: dannyiskandar
"""
import webbrowser



class Movie():
    #""" this class provides a way to store movie related information"""
    
    #define class variable , avariables that could be used for this class movie not just one of the instance of the class
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    