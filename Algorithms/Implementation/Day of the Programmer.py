#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap_date='12.09.'
    other_date='13.09.'
    if year == 1918:
        date = '26.09.1918'
    elif year<=1917 and year%4==0:
        date = leap_date +str(year)
    elif year>=1919 and (year%4==0 and (year%100!=0 or year%400==0)):
        date = leap_date +str(year)
    else:
        date = other_date + str(year)
    return date
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
