#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:20:35 2017

@author: dannyiskandar
"""

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        
        
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of toys -"+str(self.number_of_toys))
        
        
#creatiing an instance from a class child, this line below will be executed first, which
#means it will execute __init__ function that basically initialise variable and create space
#for that instance!

#billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()


miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()

#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)