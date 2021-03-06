import math
import os
import random
import re
import sys
from collections import Counter
# Complete the countTriplets function below.
def countTriplets(arr, r):
    left_map = Counter()
    right_map = Counter(arr)
    count = 0
    for j in arr:
        right_map[j] -= 1
        i = left_map[j/r]
        k = right_map[j*r]
        count += i * k
        left_map[j] += 1
    return count

    
    
