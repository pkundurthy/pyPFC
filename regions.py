
import numpy as np
from sets import const
from signal import *
const = const()

def fn_dmax(tp,wv,uq, list_noise):
    """;+
    ; AUTHOR:
    ;   P. Kundurthy & E. Agol, University of Washington, Seattle
    ;
    ; PURPOSE:
    ;   Computes Dmax from various parameters
    ;
    ; CALLING SEQUENCE:
    ;   dmax = FN_DMAX(tp,wv,uq,list_noise)
    ;
    ; INPUTS:
    ;   tp - telescope parameters [data structure]
    ;   wv - telescope parameters [data structure]
    ;   uq - telescope parameters [data structure]
    ;
    ; OUTPUTS:
    ;   tel = {IWA:<value>,Rtel:<value>...}
    ;-"""
    
    alf_max = 60.0e0*const.deg2rad

    # See derivations on pages 
    Phialfmax = (np.cos(alf_max/2.0e0))**4.0
    Falfmax = (Phialfmax**2.0e0)*( (np.sin(alf_max))**4.0e0)

    NCASE=['Z','EZ','PSF','RD','A3','A4']
    match = where(NCASE EQ strupcase(strn(uq.noise)))
    # uq.r = 1.0d0
    # uq.dist = 1.0d0
    # uq.alf = !dpi/2.0d0
    Phialf = (np.cos(uq.alf/2.0e0))**4.0
    
    Qp = fn_Qp(tp,wv,uq)
    Kp = (((uq.dist*const.pc2cm*uq.r*const.au2cm)**2.0e0)/Phialf)*Qp
    K1 = (tp.IWA*wv.lbd*const.A2cm/(2.0e0*tp.Rtel*const.m2cm))
    if 'Z' in list_noise:
        Qz = fn_Qz(tp,wv,uq)
        DZ = ((Kp**2.0e0)/(Qz*(uq.SNdet**(2.0e0))*(K1**4.0e0))*Falfmax)**(1.0e0/8.0e0)
    if 'EZ' in list_noise:
        Qez = fn_Qez(tp,wv,uq)
        Kez = ((uq.r*const.au2cm)**2.0e0)*((np.sin(uq.alf))**2.0e0)*Qez
        DEZ = ((Kp**2.0e0)/(Kez*(uq.SNdet**(2.0e0))*(K1**2.0e0))*Falfmax)**(1.0e0/6.0e0)
        
    if 'PSF' in list_noise:
        Qpsf = fn_Qpsf(tp,wv,uq)
        Kpsf = ((uq.dist*const.pc2cm)**2.0e0)*Qpsf
        DPSF = ((Kp**2.0e0)/(Kpsf*(uq.SNdet**(2.0e0))*(K1**4.0e0))*Falfmax)**(1.0e0/6.0e0)

    if 'RD' in list_noise:
        Qrd = fn_Qrd(tp,wv,uq)
        DRD = ((Kp**2.0e0)/(Qrd*(uq.SNdet**(2.0e0))*(K1**4.0e0))*Falfmax)**(1.0e0/8.0e0)

    MultiCondition == False
    if ('Z' in list_noise) and ('EZ' in list_noise) and ('PSF' in list_noise):
        DZprime = DZ
        MultiCondition = True
    if ('Z' in list_noise) and ('EZ' in list_noise) and ('PSF' in list_noise) and ('RD' in list_noise):
        DZprime = (DZ*DRD)/((DZ**8.0e0+DRD**8.0e0)**(1.0e0/8.0e0))
        MultiCondition = True

    if MultiCondition:
        V = (DZprime**6.0e0)*(DEZ**6.0e0+DPSF**6.0e0)/((DEZ**6.0e0)*(DPSF**6.0e0))
        S = (3.0e0/(2.0e0**(1.0e0/3.0e0)))*(np.sqrt(V**4.0e0 + (256.0e0/27.0e0))-V**2.0e0)**(1.0e0/3.0e0)
        G = ( (V**2.0e0)/4.0e0 - (4.0e0/S) + S/3.0e0)**(0.5e0)
        Dmax = DZprime*((-G/2.0e0)-(V/4.0e0)+0.5*np.sqrt((3.0e0*(V**2.0e0)/4.0e0)+( (V**3.0e0)/(4.0e0*G))-G**2.0e0))**(0.5e0)
    else:
        if 'Z' in list_noise:
            Dmax = DZ
        if 'EZ' in list_noise:
            Dmax = DEZ
        if 'PSF' in list_noise:
            Dmax = DPSF
        if 'RD' in list_noise:
            Dmax = DRD

    return Dmax/const.pc2cm
        
def fn_r1(tp,wv,uq):
    # Input units are in standard initial units (see p_initialize)
    # Output is in AU

    cm2au = 1.0e0/const.au2cm
    r1 = cm2au*((tp.IWA/np.sin(uq.alf))*((wv.lbd*const.A2cm)/(2.0e0*(tp.Rtel*const.m2cm)))*(uq.dist*const.pc2cm))
    return r1

def fn_r2(tp, wv, uq):
    # Input units are in standard initial units (see p_initialize)
    # Output is in AU
    
    cm2au = 1.0e0/const.au2cm
    # uq.r = 1.0d0

    fnQp = fn_Qp(tp,wv,uq)
    Cp = ((uq.r*const.au2cm)**2.0e0)*fnQp
    if 'Z' in list_noise:
        fnQz = fn_Qz(tp,wv,uq)
        r2 = (((Cp**2.0e0)/(fnQz))*(uq.sndet**(-2.0e0)))**(0.25e0)
    if 'EZ' in list_noise:
        fnQez = fn_Qez(tp,wv,uq)
        Cez = ((uq.r*const.au2cm)**2.0e0)*fnQez
        r2 = (((Cp**2.0e0)/(Cez))*(uq.sndet**(-2.0e0)))**(0.5e0)
    if 'PSF' in list_noise:
        fnQpsf = fn_Qpsf(tp,wv,uq)
        r2 = (((Cp**2.0e0)/(fnQpsf))*(uq.sndet**(-2.0e0)))**(0.25e0)
    if 'RD' in list_noise:
        fnQrd = fn_Qrd(tp,wv,uq)
        r2 = (((Cp**2.0e0)/(fnQrd))*(uq.sndet**(-2.0e0)))**(0.25e0)
    
    MultiCondition == False
    if ('Z' in list_noise) and ('EZ' in list_noise) and ('PSF' in list_noise):
        Qx = fnQz + fnQpsf
        MultiCondition = True
    if ('Z' in list_noise) and ('EZ' in list_noise) and ('PSF' in list_noise) and ('RD' in list_noise):
        Qx = fnQz + fnQpsf + fnQrd
        MultiCondition = True
    
    if MultiCondition:
        r2 = ((Cez/(2.0e0*Qx))*( (-1.0e0) + np.sqrt(1.0e0 + (4.0e0*Qx*Cpsn/Cez**2.0e0))))**(0.5e0)

    return r2*cm2au

def fn_rhzin(stel):
    # input stel.lbol must be in solar units
    # output is in AU
    return 0.95e0*np.sqrt(stel.lbol)

def fn_rhzout(stel):
    # input stel.lbol must be in solar units
    # output is in AU
    return 1.35e0*np.sqrt(stel.lbol)
    
def fn_rmax(tp, wv, uq):
    
    Dmax = const.pc2cm*fn_Dmax(tp,wv,uq)
    alfmax = 60.0e0*const.deg2rad
    rmax = (tp.iwa*(wv.lbd*const.A2cm)/(2.0e0*(tp.rtel*const.m2cm)))*Dmax/np.sin(alfmax)
    return rmax/const.au2cm

def fn_xi1(tp, wv, uq):
    r1 = fn_r1(tp,wv,uq)
    rmax = fn_rmax(tp,wv,uq)
    return r1/rmax

def fn_xi2(tp, wv, uq):
    r2 = fn_r2(tp,wv,uq)
    rmax = fn_rmax(tp,wv,uq)
    return r2/rmax

def fn_xihzin(tp,wv,uq,stel):
    rhz1 = fn_rhzin(stel)
    rmax = fn_rmax(tp,wv,uq)
    return rhz1/rmax

def fn_xihzout(tp,wv,uq,stel):
    rhz2 = fn_rhzout(stel)
    rmax = fn_rmax(tp,wv,uq)
    return rhz2/rmax






