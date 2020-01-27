# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:04:47 2020

@author: Varad Srivastava

You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Constraints





Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .
"""

from itertools import product

def smax(x,k,m):
    slis = []
    for j in x:
        sum = 0
        for y in range(k):
            sum = sum + pow(j[y],2)
        slis.append(sum%m)

    return (max(slis))

if __name__ == "__main__":
    K,M = map(int,input().split())
    N = []
    Z = []
    for i in range(K):
        N = list(map(int,input().split()))
        N.pop(0)
        Z.append(N)

    cartesian = list(product(*Z))
    print(smax(cartesian,K,M))