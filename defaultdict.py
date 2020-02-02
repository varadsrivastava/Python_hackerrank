# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:34:36 2020

@author: Varad Srivastava

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
For example:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])
In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. Print the indices of each occurrence of  in group . If it does not appear, print .

Constraints



Input Format

The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .

Output Format

Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared  times in positions ,  and .
'b' appeared  times in positions  and .
In the sample problem, if 'c' also appeared in word group , you would print .

Python 3


123456789101112131415161718

 
    for item in B:
        if item in A:
            print(*A[item])
        else:
            print("-1")


Line: 18 Col: 1
Submit CodeRun Code
Upload Code as File
Test against custom input
Python
You have earned 20.00 points!
55/115 challenges solved.
48%
Congratulations
You solved this challenge. Would you like to challenge your friends?

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
5 2
a
a
b
a
b
a
b
Expected Output
Download
1 2 4
3 5
Contest Calendar
"""

from collections import defaultdict

if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    A = defaultdict(list)
    B = []
    for i in range(n):
        A[input()].append(i+1)
    for j in range(m):
        B.append(input())

 
    for item in B:
        if item in A:
            print(*A[item])
        else:
            print("-1")
