#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    countSwap=0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                countSwap+=1
    print("Array is sorted in "+str(countSwap)+" swaps. ")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[len(a)-1]))
                
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
