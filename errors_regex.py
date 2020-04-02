# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:16:52 2020

@author: Varad Srivastava

You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
"""
import re

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        try:
            print(bool(re.compile(input())))
        except:
            print("False")
