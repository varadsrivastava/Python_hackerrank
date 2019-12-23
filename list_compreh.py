# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 19:37:44 2019

@author: Varad Srivastava
"""
"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, 

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if ((i+j+k)!=n)])