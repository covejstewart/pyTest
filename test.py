#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeffrey
#
# Created:     14/08/2009
# Copyright:   (c) jeffrey 2009
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import math
import random

def main():

    y=[]
    for i in range(1000):
        y.append(random.random());
    mean = calcMean(y)
    stdev = calcStdDev(y, mean)
    print mean
    print stdev

def calcMean(data):
    mean = 0
    count = 0
    for val in data:
        if val == '':
            continue
        count += 1
        mean = mean + float(val)
    if count > 0:
        mean = mean / count
    else:
        mean = 0
    return mean

def calcStdDev(data, mean):
    stdev = 0
    count = 0
    for val in data:
        if val == '':
            continue
        count += 1

        stdev = stdev + (float(val) - mean)**2

    if count > 1:
        stdev = math.sqrt(stdev/(count - 1))
    else:
        stdev = 0

    return stdev

if __name__ == "__main__":
    main()