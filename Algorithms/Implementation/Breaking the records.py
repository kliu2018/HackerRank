#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    ma=0
    mi=0
    score_max = scores[0]
    score_min = scores[0]
    for i in range(1, n):
        if scores[i] > scores[i-1] and scores[i]> score_max:
            ma+=1
            score_max = scores[i]
        if scores[i] < scores[i-1] and scores[i] < score_min:
            mi+=1
            score_min = scores[i]
        else:
            None
    return ma, mi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
