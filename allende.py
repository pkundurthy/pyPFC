

import cPickle as cP
import numpy as np
from universal import *

allende = cP.load(open(picklePath+'allende99.pickle','rb'))

def colormag():
    
    bv = []
    v = []
    
    for hid in allende.keys():
        bv.append(allende[hid]['bv'])
        v.append(allende[hid]['vmag_abs'])

    return bv, v
    
def coordinates():
    
    ra = []
    dec = []
    
    for hid in allende.keys():
        ra.append(allende[hid]['RA'])
        dec.append(allende[hid]['DEC'])

    return ra, dec
    
def getdist():
    
    dist = []
    for hid in allende.keys():
        dist.append(1e0/allende[hid]['plx'])

    return dist

def getParams(hip):

    OutDict = {'teff':10**(allende[hip]['logTeff']),\
               'logg':allende[hip]['logg'],\
               'dist':1e0/allende[hip]['plx'],\
               'mass':allende[hip]['mass'],\
               'rad':10**(allende[hip]['logRad']),\
               'bv':allende[hip]['bv'],\
               'bc':allende[hip]['bc'],\
               'vmag_abs':allende[hip]['vmag_abs'],\
               'vmag_app':allende[hip]['vmag_app']
               }
               #,'RA':allende[hip]['RA'],'DEC':allende[hip]['DEC']
               #}

    return OutDict

def getPairList(par1name,par2name):
    
    par1 = []
    par2 = []
    for hid in allende.keys():
        par1.append(allende[hid][par1name])
        par2.append(allende[hid][par2name])
    
    return np.array(par1), np.array(par2)