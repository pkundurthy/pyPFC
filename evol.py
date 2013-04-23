

import cPickle as cP
import numpy as np
from universal import *
#import pylab as plt

evol, AgeMatch, RangeMass = cP.load(open(picklePath+'marigoETAL2008.pickle','rb'))

def checkMassRange(mass):
    RangeDict = {}
    for YY in evol.keys():
        if (mass > RangeMass[YY][0]) and (mass < RangeMass[YY][1]):
            RangeDict[YY] = True
        else:
            RangeDict[YY] = True
    
    return RangeDict
    
def CheckInRange(RangeDict):
    
    InRange = False
    YYOut = None
    #print AgeMatch
    for YY in AgeMatch:
        InRange = RangeDict[YY]
        if InRange:
            YYOut = YY
            break
    
    return InRange, YYOut

def getPar(mass,parname):

    RangeDict = checkMassRange(mass)
    InRange, YY = CheckInRange(RangeDict)
    ParVal = None
    
    mass = float(mass)
    mass_arr = np.array(evol[YY]['mass'])
    parr_arr = np.array(evol[YY][parname])
    
    if InRange:
        ParVal = np.interp(mass,mass_arr,parr_arr)
    else:
        raise NameError('mass not in range')
    
    return ParVal

def getAllPars(mass):
    
    RangeDict = checkMassRange(mass)
    InRange, YY = CheckInRange(RangeDict)
    OutDict = {}
    
    for par in evol[YY].keys():
        ParVal = getPar(mass,par)
        #if par == 'teff':
            #print mass, InRange, YY, ParVal
        #print par, ParVal
        OutDict[par] = ParVal

    return OutDict
