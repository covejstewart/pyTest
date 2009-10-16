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
#import scipy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def main():

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # the histogram of the data
    n, bins, patches = ax.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

    # hist uses np.histogram under the hood to create 'n' and 'bins'.
    # np.histogram returns the bin edges, so there will be 50 probability
    # density values in n, 51 bin edges in bins and 50 patches.  To get
    # everything lined up, we'll compute the bin centers
    bincenters = 0.5*(bins[1:]+bins[:-1])
    # add a 'best fit' line for the normal PDF
    y = mlab.normpdf( bincenters, mu, sigma)
    l = ax.plot(bincenters, y, 'r--', linewidth=1)

    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability')
    #ax.set_title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
    ax.set_xlim(40, 160)
    ax.set_ylim(0, 0.03)
    ax.grid(True)

    plt.show()

##    y=[]
##    for i in range(1000):
##        y.append(random.random());
##    mean = calcMean(y)
##    stdev = calcStdDev(y, mean)
##    print mean
##    print stdev
##    print numpy.max(y)
#    scipy.test()



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