
import cPickle as pickle
import numpy as np
import sys


def EvolTrack(L):

    mass = []
    logL = []
    logTeff = []
    logg = []
    mbol = []
    bmag = []
    vmag = []

    for line in L:
        lsplit = map(str, line.split())
        mass.append(float(lsplit[1].strip()))
        logL.append(float(lsplit[3].strip()))
        logTeff.append(float(lsplit[4].strip()))
        logg.append(float(lsplit[5].strip()))
        mbol.append(float(lsplit[6].strip()))
        bmag.append(float(lsplit[8].strip()))
        vmag.append(float(lsplit[9].strip()))

    return {'mass':mass,'logL':logL,'logteff':np.array(logTeff),'logg':np.array(logg),'mbol':mbol,'bv':np.array(bmag)-np.array(vmag),'vmag_abs':np.array(vmag)}

DataFile = open('output.MarigoETAL2008.data','r')
File = DataFile.readlines()

ListAge = []
for line in File:
    if not line.startswith('#'):
        lSplit = map(str, line.split())
        ListAge.append(lSplit[0].strip())

AgeDict = {}
OutDict = {}
print set(ListAge)
for age in list(set(ListAge)):
    AgeDict[str(age)] = []
    
for line in File:
    if not line.startswith('#'):
        lSplit = map(str, line.split())
        AgeDict[lSplit[0]].append(line)

for age in AgeDict.keys():
    OutDict[age] = EvolTrack(AgeDict[age])
    

RangeMass = {} 
for YY in OutDict.keys():
    RangeMass[YY] = (np.min(OutDict[YY]['mass']),np.max(OutDict[YY]['mass']))
    
ageSort = []
keyList = []
for key in OutDict.keys():
    ageSort.append(float(key))
    keyList.append(key)
    
AgeMatch = []
dummy1 = np.abs(np.array(ageSort) - 9.65e0)
index_sort = np.argsort(dummy1)
for i in index_sort:
    AgeMatch.append(keyList[i])
prefferdAge = keyList[index_sort[0]]

OutTuple = OutDict, AgeMatch, RangeMass

fileOut = open('marigoETAL2008.pickle','wb')
pickle.dump(OutTuple,fileOut,-1)
fileOut.close()


