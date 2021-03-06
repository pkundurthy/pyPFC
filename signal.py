import numpy as np
from universal import const

def fn_Qs(tp, wv, uq):
    
    return ((tp.rtel*const['m2cm'])**2.0e0)*tp.eps*(wv.lnu/(4.0e0*\
           (uq.dist*const['pc2cm'])**2.0e0))*(tp.dlnlbd)*\
           (uq.texp*const['hour2sec'])*1.509188961e26

def fn_Qp(tp, wv, uq):
    """                 """
    
    return fn_Qs(tp,wv,uq)*wv.plbd*(((uq.rp*const['km2cm'])/\
           (uq.r*const['au2cm']))**2.0e0)*(np.cos(uq.alf/2.0e0))**4.0e0
           

def fn_Qz(tp, wv, uq):
    """                 """
    
    return ((tp.rtel*const['m2cm'])**2.0e0)*tp.eps*wv.lnusol*tp.dlnlbd*\
    (uq.texp*const['hour2sec'])*uq.tauz*tp.sfac*(((wv.lbd*const['A2cm'])/\
    (2.0e0*(tp.rtel*const['m2cm'])))**2.0e0)*(0.1685855867e0)

def fn_Qez(tp, wv, uq):
    
    return ((tp.rtel*const['m2cm'])**2.0e0)*tp.eps*wv.lnu*tp.dlnlbd*\
    (uq.texp*const['hour2sec'])*uq.tauez*tp.sfac*(((wv.lbd*const['A2cm'])/\
    (2.0e0*(tp.rtel*const['m2cm'])))**2.0e0)*(3.772972403e25/(((uq.r*\
    const['au2cm'])*np.sin(uq.alf))**2.0e0))

def fn_Qpsf(tp, wv, uq):
    
    return fn_Qs(tp,wv,uq)*tp.sfac*tp.c0*(tp.lbd0/wv.lbd)**2.0e0

def fn_qrd(tp, wv, uq):
    
    return tp.xrd*tp.gain*uq.npix

def fn_SN(tp, wv, uq, list_noise):
    """                 """
    
    Qp = fn_Qp(tp,wv,uq)
    Qz = 0e0
    Qez = 0e0
    Qpsf = 0e0
    Qrd = 0e0
    
    if 'Z' in list_noise: 
        Qz = fn_Qz(tp,wv,uq)
    if 'EZ' in list_noise:
        Qez = fn_Qez(tp,wv,uq)
    if 'PSF' in list_noise:
        Qpsf = fn_Qpsf(tp,wv,uq)
    if 'RD'  in list_noise:
        Qrd = fn_Qrd(tp,wv,uq)
        
    SN = Qp/np.sqrt(Qz + Qez + Qpsf + Qrd)

    return SN
    