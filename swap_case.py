# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 01:29:03 2019

@author: Varad Srivastava
"""

"""
ou are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .
"""

def split(word): 
    charlist = []
    for char in word:
        charlist.append(char)
    return charlist    

def list_to_string(lis):
    string = ""
    for i in range(0,len(lis)):   
        string = string + str(lis[i])
    return string

def swap_case(s):
    m = []
    n = split(s)
    for letter in n:
        if letter.islower():
            lu = letter.upper()
            m.append(lu)
        elif letter.isupper():
            lo = letter.lower()
            m.append(lo)
        else:
            m.append(letter)

    return list_to_string(m)
    

    """
    stri = ""
    for letter in split(s):
        if letter.islower():
            stri= stri + (letter.upper())
        elif letter.isupper():
            stri= stri + (letter.lower())
        else:
            stri= stri + letter



    return stri   
    """

    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)