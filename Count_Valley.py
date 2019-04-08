import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c = 0
    counter = 0
    
    val = []
    for i in range(n):
        if (s[i] == 'U'):
            val.append(1)
        elif(s[i] == 'D'):
            val.append(-1)
            
    for i in range(len(val)):
        flag = 0
        if (c == -1):
            flag = 1
        c = c + val[i]
        if((flag == 1) & (c == 0)):
            counter = counter + 1
    return (counter)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()