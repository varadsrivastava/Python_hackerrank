# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:50:16 2020

@author: Varad Srivastava

You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since  is zero-indexed.

Python 3


20213233343528222729313025262319243637181617111213141534567891012
    sorted_arr.append(lis[0])
    for i in range(1,len(lis)):
        for j in range(0,len(sorted_arr)):
            if lis[i][k] > sorted_arr[j][k]:
                if j==(len(sorted_arr)-1):
                    sorted_arr.append(lis[i])
                    break
                else:
                    continue


Line: 15 Col: 28
Submit CodeRun Code
Upload Code as File
Test against custom input
100 10
64 79 18 94 46 81 74 97 71 92
46 24 23 20 68 15 53 93 24 91
17 66 34 64 28 5 55 25 44 96
16 71 80 84 5 79 63 77 69 77
33 77 24 13 58 81 41 36 73 62
93 26 16 55 61 51 39 69 29 45
44 85 1 48 23 59 52 82 50 37
77 74 9 21 35 54 81 57 32 76
82 21 72 49 98 21 77 64 6 63
68 17 93 83 12 43 84 28 96 86
9 16 3 89 38 11 70 25 41 38
49 99 31 19 85 97 80 63 16 69
50 85 80 75 36 48 56 69 63 94
78 80 83 86 92 60 56 90 22 73
69 81 45 9 67 25 82 46 68 82
98 38 23 31 38 83 37 76 69 82
95 48 21 64 25 6 38 96 69 23
44 97 46 54 21 56 65 51 66 34
87 22 27 24 55 48 90 10 8 51
21 6 74 78 8 88 26 63 72 43
64 4 42 20 54 91 2 51 79 40
93 76 52 58 40 78 98 27 53 48
85 23 86 30 91 49 81 4 59 9
88 96 77 95 36 71 7 52 14 20
69 98 21 94 14 35 28 97 3 9
60 47 56 34 35 61 9 44 80 92
4 76 57 28 60 3 46 4 6 17
59 44 88 7 71 60 84 12 91 38
76 57 5 2 25 12 46 62 32 68
14 15 11 1 34 20 54 58 45 38
89 49 16 43 74 51 80 22 88 31
8 98 51 73 32 13 59 12 56 92
36 82 9 63 77 79 77 25 52 91
63 82 58 75 13 20 79 89 55 89
58 37 93 1 29 72 78 95 47 35
90 82 58 60 55 86 82 22 44 94
55 17 51 99 29 92 1 79 96 34
32 78 41 1 24 52 11 80 3 25
30 32 32 71 85 80 63 23 80 97
35 22 11 71 10 48 43 58 31 33
30 98 60 58 28 71 95 28 21 29
74 4 13 99 90 64 28 27 73 4
52 21 52 31 35 82 35 64 21 71
92 85 13 48 5 32 92 70 15 85
47 55 25 80 24 22 19 78 17 43
3 91 71 53 49 39 96 88 59 61
79 26 98 2 95 95 70 38 82 85
69 67 41 11 95 39 20 19 96 36
11 74 48 23 84 49 47 43 27 90
4 28 35 14 70 62 52 94 46 91
72 11 14 82 59 51 93 98 55 79
90 84 84 24 21 81 11 57 27 78
98 97 59 51 89 40 96 35 25 59
73 85 64 17 46 9 79 54 27 15
48 91 7 56 41 6 4 26 96 39
43 22 34 89 52 59 55 52 38 42
10 31 9 8 21 46 29 4 97 4
44 49 78 31 53 29 11 35 46 14
44 39 57 35 9 63 85 5 97 24
9 72 49 50 41 47 23 71 15 45
51 6 98 64 75 35 39 48 2 50
92 22 72 60 96 15 17 4 79 27
90 30 98 28 92 8 83 71 24 62
5 54 86 14 71 96 87 2 58 78
37 61 60 30 46 96 49 58 27 48
14 59 22 35 75 60 55 28 91 85
21 1 85 85 78 67 24 69 22 17
76 61 84 64 33 76 61 10 33 95
71 9 1 32 31 80 69 7 25 59
69 64 78 85 21 88 56 70 92 74
79 12 8 9 54 56 37 44 1 84
6 66 54 5 82 17 41 25 3 71
8 44 63 17 75 43 87 15 85 3
15 42 15 59 38 22 46 27 19 13
54 71 76 93 67 39 46 12 78 46
23 82 71 34 31 61 94 58 10 62
30 8 43 38 7 23 77 38 93 32
32 72 46 59 64 45 14 73 62 72
76 26 47 89 25 73 79 28 60 48
41 58 85 55 29 64 39 84 20 87
24 8 70 16 69 32 17 26 58 16
40 53 40 63 22 37 11 74 7 8
23 4 56 39 27 94 91 72 14 61
41 86 3 29 41 15 99 50 82 84
33 5 22 93 73 86 99 87 26 66
73 25 55 46 69 38 99 14 43 55
43 21 82 30 90 66 6 67 49 25
81 38 65 40 80 7 90 82 33 13
18 45 1 90 53 51 51 96 32 90
32 69 51 22 71 85 80 61 99 23
88 8 41 92 4 25 64 89 30 75
93 85 99 87 67 3 54 16 98 57
33 54 31 83 64 93 3 24 65 81
74 19 15 66 17 14 34 50 57 16
10 30 20 97 32 85 83 89 68 18
46 82 9 14 54 50 55 28 26 96
29 96 3 33 12 52 11 26 19 22
50 81 95 59 76 53 10 9 72 87
25 85 54 43 53 13 52 70 38 76
20 14 30 80 23 43 27 67 42 11
5
Python
You have earned 30.00 points!
70/115 challenges solved.
61%
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Next Challenge
Test case 0
Test case 1
Compiler Message
Success
Input (stdin)
Download
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Expected Output
Download
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def athelete_sort(lis,k):
    sorted_arr = []
    sorted_arr.append(lis[0])
    for i in range(1,len(lis)):
        for j in range(0,len(sorted_arr)):
            if lis[i][k] > sorted_arr[j][k]:
                if j==(len(sorted_arr)-1):
                    sorted_arr.append(lis[i])
                    break
                else:
                    continue

            elif lis[i][k] == sorted_arr[j][k]:
                if j==(len(sorted_arr)-1):
                    sorted_arr.append(lis[i])
                    break                 
                
                elif lis[i][k] < sorted_arr[j+1][k]:
                    sorted_arr.insert(j+1,lis[i])
                    break
                else:
                    continue


            else:
                sorted_arr.insert(j,lis[i])
                break
    
    for m in sorted_arr:
        print(*m)
    

if __name__ == '__main__':
    nm = input().split()
    
    N = int(nm[0])
       
    M = int(nm[1])
      
    arr = []
     
    for _ in range(N):
        arr.append(list(map(int, input().rstrip().split())))
    
    K = int(input())
    athelete_sort(arr,K)
