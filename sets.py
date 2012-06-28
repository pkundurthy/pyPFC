
import cPickle as cP
from universal import *

telData =cP.load(open(picklePath+'telescope.pickle','rb'))

class const:
    """
        PURPOSE:
        Initializes a data structure with a list of user specified
        constants from the file 'constants.txt'
        
        DATA:
        #constants in cgs
        #['CLIGHT','GRAVC','MSUN','RADSUN','HPLANCK','BOLTZMANNK',
        #'A2CM','PC2CM','AU2CM','KM2CM','M2CM','HOUR2SEC','MIN2SEC',
        #'DAY2SEC','YEAR2SEC','DEG2RAD','RAD2ASEC']
        #
        clight          |   2.99792458d10          |    cm/sec
        msun            |   1.99d33                |    g
        gravc           |   6.67259d-8             |    cm^3 g^-1 sec^-2
        radsun          |   6.96d10                |    cm
        hplanck         |   6.6260755d-27          |    erg sec
        boltzmannk      |   1.380658d-16           |    erg/K
        A2cm            |   1.0d-8                 |    cm
        pc2cm           |   3.086d18               |    cm
        au2cm           |   1.496d13               |    cm
        km2cm           |   1.0d5                  |    cm
        m2cm            |   1.0d2                  |    cm
        hour2sec        |   3600.d0                |    sec
        min2sec         |   60.0d0                 |    sec
        day2sec         |   8.64d4                 |    sec
        year2sec        |   3.1536d7               |    sec
        deg2rad         |   1.74532925d-2          |    radians
        rad2asec        |   206264.806247          |    arcsec
        lowangle        |   5d-12                  |    radians (1 micro-arcsec) 
        """
    
    def __init__(self):
        self.clight    = 2.99792458e10
        self.msun      = 1.99e33
        self.gravc     = 6.67259e-8
        self.radsun    = 6.96e10
        self.hplanck   = 6.6260755e-27
        self.boltzmann = 1.380658e-16
        self.A2cm      = 1.0e-8
        self.pc2cm     = 3.086e18
        self.au2cm     = 1.496e13
        self.km2cm     = 1.0e5
        self.m2cm      = 1.0e2
        self.hour2sec  = 3600e0
        self.min2sec   = 60e0
        self.day2sec   = 8.64e4
        self.year2sec  = 3.1536e7
        self.deg2rad   = 1.74532925e-2
        self.rad2asec  = 206264.806247e0
        
class telescope:
    """

   PURPOSE:
       Reads telescope data from a file

   out - <data structure>
       .iwa    - the inner working angle in lambda/Diameter units
       .rtel   - the radius of the telescope's primary mirror in meters
       .c0     - the contrast ratio of the detection zone <dimensionless>
       .eps    - the dimensionless throughput (multiply by 100 to get %)
       .sfac   - the sharpness of the PSF in  lambda/Diameter units
       .lbd0   - the fiducial wavelength of the contrast measurement in Angstroms
       .dlnlbd - the dimensionless bandpass (multiply by 100 to get %)
       .xrd    - the read-noise in photons/electron
       .gain   - the gain of the detector electron/readout
       .telname- the string containing the telescope's name

    """

    def __init__(self, telname):

        self.iwa    = telData[telname]['IWA']
        self.rtel   = telData[telname]['Dtel']/2e0
        self.c0     = telData[telname]['C0']
        self.eps    = telData[telname]['eps']
        self.sfac   = telData[telname]['Sfac']
        self.ldb0   = telData[telname]['lbd0']
        self.dlnlbd = telData[telname]['dlnlbd']
        self.xrd    = telData[telname]['XRD']
        self.gain   = telData[telname]['Gain']
        self.telname= telname
        self.refs   = telData[telname]['Refs']

class observation:
    
    def __init__(self, lbd, texp, sndet):
        """
            lbd - Angstrom
            texp - hours
            sndet - 
        """
        
        self.lbd = lbd
        self.texp = texp
        self.sndet = sndet

class planet:
    
    def __init__(self, rp, r, alf, plbd):
        """
            rp - Earth radii
            r - AU
            alg - degrees
            plbd -
        """

        self.rp = rp
        self.r = r
        self.alf = alf
        self.plbd = plbd

class stellar:

    def __init__(self, mass):
        """
            mass - solar masses
            age - years
            const - (python object)
        """

        self.mass = mass

        self.rad =
        self.teff =
        self.logg =
        self.lbol =
        self.vmag =
        self.bmag =
        self.mbol =

    def wvparams(self, lbd):
        """ lbd - Angstrom """
        
        self.lnu =

    def setdist(self, dist):
        """ dist - parsecs """

        self.dist= dist

class system:

    def __init__(self, planet, stellar):

        self.planet = planet
        self.stellar = stellar