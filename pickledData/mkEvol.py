
import cPickle as pickle
import numpy as np


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

    return {'mass':mass,'logL':logL,'teff':10**(np.array(logTeff)),'logg':np.array(logg),'mbol':mbol,'bv':np.array(bmag)-np.array(vmag),'vmag_abs':np.array(vmag)}

DataFile = open('output.MarigoETAL2008.data','r')
File = DataFile.readlines()

L6 = []
L7 = []
L8 = []
L9 = []
L10 = []
OutDict = {}
for line in File:
    if not line.startswith('#'):
        lSplit = map(str, line.split())
        print lSplit[0]
        if lSplit[0].strip() == '6.00':
            L6.append(line)
        if lSplit[0].strip() == '7.00':
            L7.append(line)
        if lSplit[0].strip() == '8.00':
            L8.append(line)
        if lSplit[0].strip() == '9.00':
            L9.append(line)
        if lSplit[0].strip() == '10.00':
            L10.append(line)


OutDict['6.0'] = EvolTrack(L6)
OutDict['7.0'] = EvolTrack(L7)
OutDict['8.0'] = EvolTrack(L8)
OutDict['9.0'] = EvolTrack(L9)
OutDict['10.0'] = EvolTrack(L10)

fileOut = open('marigoETAL2008.pickle','wb')
pickle.dump(OutDict,fileOut,-1)
fileOut.close()




