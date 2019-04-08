import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = 0
    sum = 0
    z = Counter(ar)

    r = list(z.values())
    
    for i in range(len(r)):
        sum = sum +(r[i]//2)
    print(sum)
    return sum
    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()