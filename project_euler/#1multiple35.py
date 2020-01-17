# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 03:23:08 2020

@author: Varad Srivastava

This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

For each test case, print an integer that denotes the sum of all the multiples of  or  below .

Sample Input 0

2
10
100
Sample Output 0

23
2318
Explanation 0

For , if we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Similarly for , we get .
"""

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumf=0
    sumt=0
    sumft=0
    m = n//3
    o = n//5
    p = n//15
    if n%5==0:
        sumf = int((o*(o-1)//2*5))
    else:
        sumf = int((o*(o+1)//2*5))
    if n%3==0:
        sumt = int((m*(m-1)//2*3))
    else:
        sumt = int((m*(m+1)//2*3))
    if n%15==0:
        sumft = int((p*(p-1)//2*15))
    else:
        sumft = int((p*(p+1)//2*15))
        
    
    print(sumt+sumf-sumft)