


import os
import sys
import numpy as num
import scipy.interpolate
import cPickle as pickle
import pylab as plt

def readFlux(fileName):
    
    File = open(fileName,'r')
    wv = []
    fl = []
    bb = []
    i = 0
    while True:
        line = File.readline()
        if len(line) == 0:
            break
        else:
            i += 1
            lSplit = map(float, line.split('|'))
            wv.append(lSplit[0])
            fl.append(lSplit[1])
            bb.append(lSplit[2])

    return wv, fl, bb

ColFile1 = 'Col-100-4.5.spec'
ColFile2 = 'Col-34-4.5.spec'

wv1, fl1, bb2 = readFlux(ColFile1)
wv2, fl2, bb2 = readFlux(ColFile2)

print set(wv2) <= set(wv1)

print len(wv1), len(wv2)
print len(list(set(wv1))), len(list(set(wv2)))

