
import inspect, os

#print inspect.getfile(inspect.currentframe()) # script filename (usually with path)
modulePath = os.path.dirname( os.path.abspath(__file__ ) )
picklePath = modulePath+'/pickledData/'

const = {\
        'clight'    : 2.99792458e10,\
        'msun'      : 1.99e33,\
        'gravc'     : 6.67259e-8,\
        'radsun'    : 6.96e10,\
        'hplanck'   : 6.6260755e-27,\
        'boltzmann' : 1.380658e-16,\
        'A2cm'      : 1.0e-8,\
        'pc2cm'     : 3.086e18,\
        'au2cm'     : 1.496e13,\
        'km2cm'     : 1.0e5,\
        'm2cm'      : 1.0e2,\
        'hour2sec'  : 3600e0,\
        'min2sec'   : 60e0,\
        'day2sec'   : 8.64e4,\
        'year2sec'  : 3.1536e7,\
        'deg2rad'   : 1.74532925e-2,\
        'rad2asec'  : 206264.806247e0\
        }
