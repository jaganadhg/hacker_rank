"""
10 Days of Statistics 
Day 0 Weighted Mean
"""
from __future__ import division

n = raw_input()
vector = map(int,raw_input().split())
weight = map(int,raw_input().split())

prod = lambda x: x[0] * x[1]

def weighted_mean(vector,weight):
    vector_weight = zip(vector,weight)
    
    return round(sum(map(prod,vector_weight))/sum(weight),1)

print weighted_mean(vector,weight)
