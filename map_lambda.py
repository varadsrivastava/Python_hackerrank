# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:04:45 2020

@author: Varad Srivastava

Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Concept

The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
Note:

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

Input Format

One line of input: an integer .

Constraints


Output Format

A list on a single line containing the cubes of the first  fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation

The first  fibonacci numbers are , and their cubes are .

Python 3


12345678910111213141516171819
    else:
        lis=[0,1]
        for i in range(2,n):
            lis.append(lis[i-1]+lis[i-2])
    return(lis)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
Line: 19 Col: 41
Submit CodeRun Code
Upload Code as File
Test against custom input
Python
You have earned 20.00 points!
72/115 challenges solved.
63%
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Next Challenge
Test case 0
Test case 1
Test case 2
Test case 3
Test case 4
Test case 5
Test case 6
Test case 7
Test case 8
Test case 9
Compiler Message
Success
Input (stdin)
Download
5
Expected Output
Download
[0, 1, 1, 8, 27]
Contest Calendar
"""

cube = lambda x: pow(x,3)

def fibonacci(n):
    lis = []  
    if n==0:
        lis=[]
    elif n==1:
        lis=[0]
    elif n==2:
        lis=[0,1]
    else:
        lis=[0,1]
        for i in range(2,n):
            lis.append(lis[i-1]+lis[i-2])
    return(lis)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))