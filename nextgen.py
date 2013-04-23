
import cPickle as cP
import numpy as np
from universal import *
Phoenix = cP.load(open(picklePath+'Phoenix.pickle','rb'))
import pylab as plt
from sets import const

def find_nearest(array,value):
    idx=(np.abs(array-value)).argmin()
    return array[idx], idx

def TempLoggGrid(lbd_index, specType):
    
    Grid = Phoenix[specType][lbd_index,:,:]
    return Grid
    
def fn_lnu_nextgen(lbd, temp, logg, stelrad):
    
    
    lbd_used, lbd_index = find_nearest(Phoenix['wv'],lbd)

    FluxGrid = TempLoggGrid(lbd_index,'FL')
    #BB_TLG = TempLoggGrid(lbd_index,'BB')
    
    FluxVlogg = []
    print np.shape(Phoenix['logg']), np.shape(Phoenix['temp']), np.shape(FluxGrid) 
    for i in range(len(Phoenix['logg'])):
        #plt.plot(Phoenix['temp'],FluxGrid[i,:],'b.')
        #xtemp = np.arange(min(Phoenix['temp']),max(Phoenix['temp']),1000)
        #ytemp = np.interp(xtemp,Phoenix['temp'],FluxGrid[i,:])
        #plt.plot(xtemp,ytemp,'r-')
        #plt.title(str(Phoenix['logg'][i]))
        #plt.show()
        FVlogg = np.interp(temp, Phoenix['temp']*100,FluxGrid[i,:])
        FluxVlogg.append(FVlogg)
    
    ff = np.interp(logg, Phoenix['logg'],np.array(FluxVlogg))

    #InterpFunc = scipy.interpolate.interp2d(Phoenix['logg'],Phoenix['temp']*100e0,FluxGrid,kind='linear')
    #InterpFunc = scipy.interpolate.(Phoenix['logg'],Phoenix['temp']*100e0,BB_TLG)

    #ff = InterpFunc(logg,temp)
    #print FluxGrid
    Lnu = (4.0*np.pi*(const['radsun']*stelrad)**2)*ff*((lbd_used*const['A2cm'])**2)/(const['clight'])
    # LL = specific luminosity in erg/sec/Hz
    return Lnu
