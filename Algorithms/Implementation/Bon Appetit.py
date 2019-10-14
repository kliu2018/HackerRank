#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = sum(bill)
    no_anna = total - bill[k]
    true_b = no_anna/2
    wrong_b = total/2
    if true_b ==b:
        print('Bon Appetit') 
    else:
        owe = wrong_b - true_b
        print(int(owe))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
