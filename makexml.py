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
from xml.dom.minidom import Document
import csv
import math

def main():

    filereader = csv.reader(open('testSystemResults.csv'), delimiter=',');

    outfile = open('map.csv', 'w')

    for row in filereader:
        newrow = 0
        name = row[0]
        mean = calcMean(row[5::1])
        stdev = calcStdDev(row[5::1], mean)
        newrow = name+","
        for val in row[5::1]:
            if val == '' or stdev == 0:
                newrow += ","
            else:
                out = abs((float(val) - mean) / stdev)
                out = '%.2f,' %out
                newrow += out
        outfile.write(newrow+'\n')


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