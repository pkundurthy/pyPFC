
import numpy as np
from universal import *
from regions import *

def fn_xi1_alf(tp,wv,uq,list_noise):
 
    def xi1(alf):
        uq.alf = alf
        r1 = fn_r1(tp,wv,uq)
        rmax = fn_rmax(tp,wv,uq,list_noise)
        return r1/rmax

    return xi1
    
def fn_xi2_alf(tp,wv,uq,list_noise):

    def xi2(alf):
        uq.alf = alf
        r2 = fn_r2(tp,wv,uq)
        rmax = fn_rmax(tp,wv,uq,list_noise)
        return r2/rmax

    return xi2

def fn_xihzin_alf(stel,list_noise):

    def xihzin(alf):
        uq.alf = alf
        rhz1 = fn_rhzin(stel)
        rmax = fn_rmax(tp,wv,uq,list_noise)
        return rhz1/rmax

    return xihzin

def fn_xihzout_alf(stel,list_noise):

    def xihzout(alf):
        uq.alf = alf
        rhz2 = fn_rhzout(stel)
        rmax = fn_rmax(tp,wv,uq,list_noise)
        return rhz2/rmax

    return xihzout

def fn_xi_intersection_alf(func1,func2,tp,wv,uq,stel,list_noise):
    
    if func1 == func2:
        raise NameError("Same Function %s %s" % func1, func2)
    
    if (func1 == 'fn_xihzin_alf' and func2 == 'fn_xihzout_alf')\
        or (func2 == 'fn_xihzin_alf' and func1 == 'fn_xihzout_alf'):
        raise NameError("cannot have both HZ functions")
    
    def fn_xi_intersection(alf):

        xiTOP = 
        xiBOT =
        
        
    
    
