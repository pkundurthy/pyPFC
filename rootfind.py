
import numpy as np

def rootSecant(Func, x1, x2):
    
    eps = np.abs(Func(x1)/ (Func(x1) - Func(x2)))
    while eps > 1e-12:
        x0 = x1 - Func(x1)*((x1-x2)/(Func(x1) - Func(x2)))
        x2 = x2
        x1 = x0
        eps = np.abs(Func(x1)/ (Func(x1) - Func(x2)))

    return x1
    
