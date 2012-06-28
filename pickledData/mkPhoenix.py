
import os
import sys
import numpy as num


lg = ['3.5','4.0','4.5','5.0','5.5']
set1 = num.arange(26,40,1)
set2 = num.arange(40,102,2)
tempList = num.concatenate((set1,set2),1)

IDLscr = open('MakeColumnFiles.scr','w')
for t in tempList:
    for l in lg:
        fileName = 'lte'+str(t)+'-'+str(l)+'-0.0.NextGen.spec.gz'
        ColFile = 'Col-'+str(t)+'-'+str(l)+'.spec'
        print >> IDLscr, 'rdNextGen, "%s", w, f, b, teff, logg, mh' % (fileName)
        print >> IDLscr, 'openw,1, "%s"' % (ColFile)
        print >> IDLscr, 'print, "%s"' % (ColFile)
        print >> IDLscr, 'for i=0L,N_ELEMENTS(w)-1 do printf,1, w[i],"|",f[i],"|",b[i]'
        print >> IDLscr, 'close,1\n'
        #print fileName, ColFile
IDLscr.close()

os.system('idl < MakeColumnFiles.scr')
