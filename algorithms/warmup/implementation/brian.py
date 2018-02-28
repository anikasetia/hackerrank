#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    i = 0
    b_act_twice = 0
    for each in ar:
        
        if(i != k):
            b_act_twice = b_act_twice + each
            
    if((b_act_twice/2) == b):
        return "Bon Appetit"
    else:
        return (b - (b_act_twice/2))
            

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
