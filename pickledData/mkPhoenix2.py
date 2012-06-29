
import os
import sys
import numpy as num
import scipy.interpolate
import cPickle as pickle
import pylab as plt

def find_nearest(array,value):
    idx=(num.abs(array-value)).argmin()
    return idx

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

set1 = num.arange(26,40,1)
set2 = num.arange(40,102,2)
tempList = num.concatenate((set1,set2),1)
lg = [3.5,4.0,4.5,5.0,5.5]

#OutArraryFF = np.zeros( len(lg),len(tempList) )
#OutArraryBB = np.zeros( len(lg),len(tempList) )

MassDict = {}
for i in range(len(tempList)):
    ttStr = str(tempList[i])
    MassDict[ttStr] = {}
    for j in range(len(lg)):
        lgStr = str(lg[j])
        ColFile = 'Col-'+ttStr+'-'+lgStr+'.spec'
        #print ColFile
        wv, fl, bb = readFlux(ColFile)
        MassDict[ttStr][lgStr] = {'wv':wv,'fl':fl,'bb':bb}
        print ColFile, len(wv), len(fl), len(bb)

FLArray = num.zeros( (21312,len(lg),len(tempList)) )
BBArray = num.zeros( (21312,len(lg),len(tempList)) )

ColFile0 = 'Col-38-4.5.spec'
wv0, fl0, bb0 = readFlux(ColFile0)
indx = []
#print MassDict.keys()
wv1 = []
for k in range(len(wv0)):
    if wv0[k] in MassDict['100']['4.5']['wv'] and not wv0[k] in wv1:
        ids = find_nearest(num.array(MassDict['100']['4.5']['wv']),wv0[k])
        indx.append(ids)
        diff = wv0[k]-MassDict['100']['4.5']['wv'][ids] 
        if diff != 0e0: print diff, wv0[k], MassDict['100']['4.5']['wv'][ids]
        if k == 5000: print '1/4', indx[-1]
        if k == 10000: print '2/4', indx[-1]
        if k == 15000: print '3/4', indx[-1]
        if k == 20000: print '4/4', indx[-1]
        wv1.append(wv0[k])
#print len(wv0), len(wv1)

for i in range(len(tempList)):
    ttStr = str(tempList[i])
    for j in range(len(lg)):
        lgStr = str(lg[j])
        print ttStr,' ',lgStr
        if len(MassDict[ttStr][lgStr]['wv']) == 21312:
            FLArray[:,j,i] = num.array(MassDict[ttStr][lgStr]['fl'])
            BBArray[:,j,i] = num.array(MassDict[ttStr][lgStr]['bb'])
        else:
            wv = num.array(MassDict[ttStr][lgStr]['wv'])[indx]
            wv.tolist()
            fl = num.array(MassDict[ttStr][lgStr]['fl'])[indx]
            bb = num.array(MassDict[ttStr][lgStr]['bb'])[indx]
            print len(fl), len(bb), len(indx), wv - num.array(wv0)
            FLArray[:,j,i] = fl
            BBArray[:,j,i] = bb


OutDict = {'wv':num.array(wv0),'logg':num.array(lg),\
           'temp':num.array(tempList),'FL':FLArray,'BB':BBArray}

fileOut = open('Phoenix.pickle','wb')
pickle.dump(OutDict,fileOut,-1)
fileOut.close()

