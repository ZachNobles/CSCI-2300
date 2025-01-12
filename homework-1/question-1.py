# -*- coding: utf-8 -*-
"""
Homework 1, problem 1
@author: Zach Nobles
"""


### change stuff here ###

INPUT = 4 #n, or how many times the function should run

#########################



from sys import exit
stars = 0;

def foo(n):
    global stars
    if n == 0:
        return
    
    #0 to n-1, including n-1 but not n
    for i in range(n): 
        print("*", end="")
        stars += 1
    
    foo(n-1)
    
    
if __name__ == "__main__":
    
    if INPUT < 0:
        print("input should not be negative")
        exit()
    
    foo(INPUT)
    print(f"\nn = {INPUT}, {stars} stars printed")