# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:36:08 2019

@author: Varad Srivastava
"""
"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""
def takeSecond(elem):
    return elem[1]

if __name__ == '__main__':
    name_list = []
    score_list = []
    n = int(input())
    for i in range(0,n):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score) 
        i = i+1 
    fin = (list(zip(name_list,score_list)))
    fin.sort(key=takeSecond)

    min = fin[0][1]
    #print(min)

    #Finding min2
    for i in range(1,n):
        if fin[i][1]==min:
            i = i+1
        else:
            index = i
            min2 = fin[i][1]
            min2name = []
            min2name.append(fin[i][0])
            for j in range(index+1,n):
                if fin[j][1]==min2:
                    min2name.append(fin[j][0])    
            break
            
    #print(min2)
    #print(index)
    min2name.sort()
    for k in range(0,len(min2name)):
        print(min2name[k])
