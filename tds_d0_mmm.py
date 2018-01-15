"""
10 Dyans of Statistics
Day 0 Mean Median Mode
"""
from __future__ import division

n = int(raw_input())
vals = map(int,raw_input().split())


def mean(array):
    mu = sum(array)/len(array)
    return mu

def median(array):
    array = sorted(array)
    half,odd = divmod(len(array),2)
    if odd:
        return array[half]
    return (array[half-1] + array[half]) / 2.0

def mode(array):
    most = max(list(map(array.count,array)))
    return min(list(set(filter(lambda x: array.count(x) == most,array))))

print mean(vals)
print median(vals)
print mode(vals)
