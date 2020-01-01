# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:01:07 2020

@author: Varad Srivastava
"""

vowel=('A','E','I','O','U')
    
def minion_game(string):

    kevin_count = 0
    le = len(string)
    
    for i in range(0,le):
        if string[i] in vowel :
            kevin_count+=le-i 
        else:
            i+=1


    total_score = le*(le+1)/2
    st = total_score-kevin_count
    if kevin_count>st:
        print("Kevin",int(kevin_count))
    elif kevin_count<st:
        print("Stuart",int(st))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)