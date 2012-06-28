

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

    
