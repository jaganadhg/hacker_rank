"""
10 Days of Statistics
Day 1 : Quartiles
"""
from __future__ import division

n = int(raw_input())
vals = map(int,raw_input().split())


def median(array):
    array = sorted(array)
    half,odd = divmod(len(array),2)
    if odd:
        return array[half]
    return (array[half-1] + array[half]) / 2.0

def quartiles(array):
    
    sorted_array = sorted(array)
    mid = int(len(array)/2)
    
    if len(array)%2 == 0:
        lower = median(sorted_array[:mid])
        upper = median(sorted_array[mid:])
    else:
        lower = median(sorted_array[:mid])
        upper = median(sorted_array[mid + 1:])
    print int(lower)
    print int(median(array))
    print int(upper)

quartiles(vals)
