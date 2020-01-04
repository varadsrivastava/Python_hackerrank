# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 03:16:46 2020

@author: Varad Srivastava
"""

def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    if(size==1):
        print("a")
    else:

        print("-"*(size*2-2) + alpha[size-1]  + "-"*(size*2-2),end='\n')
        for i in range(size-1,0,-1):
            print("-"*(i*2-2)+ "-".join(reversed(alpha[(i):(size-1+1)])) + "-" + alpha[i-1]  + "-" + "-".join(alpha[(i):(size-1+1)]) + "-"*(i*2-2),end='\n')
        
        for i in range(2,size,1):
            print("-"*(i*2-2)+ "-".join(reversed(alpha[(i):(size-1+1)])) + "-" + alpha[i-1]  + "-" + "-".join(alpha[(i):(size-1+1)]) + "-"*(i*2-2),end='\n')
        print("-"*(size*2-2) + alpha[size-1]  + "-"*(size*2-2),end='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)