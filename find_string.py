# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 02:10:42 2019

@author: Varad Srivastava
"""

def count_substring(string, sub_string):
    counter=0
    
    for i in range(0, len(string)-len(sub_string)+1):
            if (string[i:i+len(sub_string)]==sub_string):
                    counter=counter+1

            else:
                i+=1

    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)