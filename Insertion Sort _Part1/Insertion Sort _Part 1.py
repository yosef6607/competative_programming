#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        if arr[i-1]>temp and i>0:
            arr[i]=arr[i-1]
            for j in range(0,len(arr)):
                print(arr[j],end=" ")
            print("")
        else:
            arr[i]=temp
            for j in range(0,len(arr)):
                print(arr[j],end=" ")
            print("")
            break
       
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
