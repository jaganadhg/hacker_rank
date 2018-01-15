"""
10 Days of Statistics
IQR
"""
from __future__ import division 

def median(array):
    array = sorted(array)
    half,odd = divmod(len(array),2)
    if odd:
        return array[half]
    return (array[half-1] + array[half]) / 2.0

def iqr(array):
    
    sorted_array = sorted(array)
    mid = int(len(array)/2)
    
    if len(array)%2 == 0:
        lower = median(sorted_array[:mid])
        upper = median(sorted_array[mid:])
    else:
        lower = median(sorted_array[:mid])
        upper = median(sorted_array[mid + 1:])
    iqr_ = upper - lower
    
    return iqr_


def create_vector(base_vector,freq_vector):
    final_vector = list()
    
    for element in range(len(base_vector)):
        tmp_vec = map(int,((base_vector[element] + " ") * freq_vector[element]).split())
        final_vector.extend(tmp_vec)
    return final_vector

n = int(raw_input())
base_vector = raw_input().strip().split()
freq_vector = list(map(int, raw_input().strip().split()))

final_vec = create_vector(base_vector,freq_vector)
print float(iqr(final_vec))
