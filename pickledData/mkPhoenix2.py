
import os
import sys
import numpy as num
import scipy.interpolate
import cPickle as pickle

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
        if len(wv) == 21312:
            wv0 = wv

FLArray = num.zeros( (21312,len(lg),len(tempList)) )
BBArray = num.zeros( (21312,len(lg),len(tempList)) )

for i in range(len(tempList)):
    ttStr = str(tempList[i])
    for j in range(len(lg)):
        lgStr = str(lg[j])
        print ttStr,' ',lgStr
        if len(MassDict[ttStr][lgStr]['wv']) == 21312:
            FLArray[:,j,i] = MassDict[ttStr][lgStr]['fl']
            BBArray[:,j,i] = MassDict[ttStr][lgStr]['bb']
        else:
            wv = MassDict[ttStr][lgStr]['wv']
            fl = MassDict[ttStr][lgStr]['fl']
            bb = MassDict[ttStr][lgStr]['bb']
            DFL = scipy.interpolate.UnivariateSpline(wv,fl,k=3,s=0)
            FLArray[:,j,i] = DFL(wv0)
            DBB = scipy.interpolate.UnivariateSpline(wv,bb,k=3,s=0)
            BBArray[:,j,i] = DBB(wv0)


OutDict = {'wv':num.array(wv0),'logg':num.array(lg),\
           'temp':num.array(tempList),'FL':FLArray,'BB':BBArray}

fileOut = open('Phoenix.pickle','wb')
pickle.dump(OutDict,fileOut,-1)
fileOut.close()

