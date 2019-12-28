# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 03:51:06 2019

@author: Varad Srivastava
"""
"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

def mat(height, width):
    height = int(height)
    width = int(width)

    
    for i in range(int((width-3)/2),0,-3):
        print("-"*i,end='')
        print("."+"|.."*int((width - 2*i - 3)/3)+"|.",end='')
        print(("-"*i).rjust(0))
        


    print("-"*int((width-7)/2)+"WELCOME"+"-"*int((width-7)/2))

    for i in range(3,int((width-3)/2)+3,3):
        print("-"*i,end='')
        print("."+"|.."*int((width - 2*i - 3)/3)+"|.",end='')
        print(("-"*i).rjust(0))



if __name__ == "__main__":
    N,M = input().split(" ")
    mat(N,M)
