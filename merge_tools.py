# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 01:25:42 2020

@author: Varad Srivastava
"""
"""
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting .
The second line contains an integer, , denoting the length of each subsegment.

Constraints

, where  is the length of 
It is guaranteed that  is a multiple of .
Output Format

Print  lines where each line  contains string .

Sample Input

AABCAAADA
3   
Sample Output

AB
CA
AD
Explanation

String  is split into  equal parts of length . We convert each  to  by removing any subsequent occurrences non-distinct characters in :

We then print each  on a new line.
"""
def merge_the_tools(string, k):
    lis = [[m for m in string[i:i+k]] for i in range(0,len(string),k)]
    leng = len(lis)
    llist=[[] for z in range(k)]
    
    
    for w in range(0,leng):
        for l in range(0,k): 
            #print(lis[w][l])
            if k==1:
                print(lis[w][l])
            elif (lis[w][l] not in llist[w]):
                llist[w].append(lis[w][l])
            else:
                l+=1
            
    if k!=1:        
        for j in range(0,leng):
            for x in range(len(llist[j])):
                print(llist[j][x],end="")
            print("")
        
    #print(lis)
    #print(lis[2][2])
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)