# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 01:12:41 2020

@author: Varad Srivastava

The Fibonacci sequence is defined by the recurrence relation:

.
Hence the first 12 terms will be:
The  term, , is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain  digits?

Input Format

The first line contains an integer  , i.e., number of test cases.
Next  lines will contain an integer .

Constraints



Output Format

Print the values corresponding to each test case.

Sample Input

2
3
4
Sample Output

12
17
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

#import timeit
#import sys
#sys.setrecursionlimit(30001)

"""
def countDigit(N): 
    if N == 0: 
        return 0
    return int(1 + countDigit(N // 10))


def fib(n):
    N=24000
    arr = [1,1] + [0]*N
    for i in range(2,N):
        if(countDigit(arr[i-1])<n):
            arr[i] = arr[i-1] + arr[i-2]
        else:
            print(i)
            break

def fibonac(X,Y,n,counter):
    
    if(countDigit(Y)<n):
        Z1=X+Y
        Z2=Y
        counter+=1
        fibonac(Z2,Z1,n,counter)
        
    else:
        print(counter)

    
"""
if __name__=="__main__":
    #start = timeit.default_timer()
    T = int(input())

    N=24000
    arr = [1,1] + [0]*N
    for i in range(2,N):
        arr[i] = arr[i-1] + arr[i-2]

    vals = {}
    for j in range(len(arr)):
        if len(str(arr[j])) not in vals.keys():
            vals[len(str(arr[j]))] = j+1    

    for k in range(0,T):
        k = int(input())
        print(vals[k])


    #m.sort()
    #for j in range(T):
        #fib(int(m[j]))

    

    




    #stop = timeit.default_timer()

    #print('Time: ', stop - start) 


