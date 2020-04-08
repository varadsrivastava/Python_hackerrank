# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:58:30 2020

@author: Varad Srivastava

You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""

def gsort(x):
    y = []
    z = []
    for i in x:
        if i.islower():
            y.append(i)

    for j in x:
        if j.isupper():
            y.append(j)
    
    for k in x:
        if k.isnumeric():
            if (int(k)%2)!=0:
                y.append(k)
            else:
                z.append(k)
    
    lis = y+z
    print(*lis,sep="")

"""
print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
"""
    

if __name__ == "__main__":
    S = input()
    s = list(sorted(S))
    gsort(s)

