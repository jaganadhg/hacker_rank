"""
10 Days of Statistics 
Standard Deviation
"""
from __future__ import division
import math 

n = int(raw_input())
vals = map(int,raw_input().split())

def mean(array):
    mu = sum(array)/len(array)
    return mu

def __sum_square(array):
    med = mean(array)
    sumsq = sum((item - med)**2 for item in array)
    
    return sumsq

def stdev(array):
    ssq = __sum_square(array)
    return math.sqrt(ssq/len(array))

print stdev(vals)
