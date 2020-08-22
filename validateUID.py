# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:27:25 2020

@author: Varad Srivastava

ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
"""

import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        U = input()
        if all([re.search(r,U) for r in [r"[\w]{10}",r"([A-Z].*){2}",r"([0-9].*){3}"]]) and not re.search(r"(.).*\1",U):
            print("Valid")
        else:
            print("Invalid")