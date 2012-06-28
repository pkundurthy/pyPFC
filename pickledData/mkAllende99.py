
import cPickle as pickle

FileRead = open('allende99.tsv')
FileLines = FileRead.readlines()

AllendeDict = {}

index = {0:'HIP',1:'vmag_app',2:'plx',3:'err_plx',4:'vmag_abs',5:'err_vmag_abs',\
         6:'bv',7:'logg',8:'err_logg',9:'mass',10:'err_mass',\
         11:'logRad',12:'err_logRad',13:'bc',14:'err_bc',\
         15:'logTeff',16:'err_logTeff',17:'RA',18:'DEC'}

for line in FileLines:
    if not line.startswith('#'):
        lSplit = map(str,line.split('|'))
        if len(lSplit) == 19:
            AllendeDict[lSplit[0].strip()] = {}
            for i in xrange(1,19):
                AllendeDict[lSplit[0].strip()][index[i]] = float(lSplit[i].strip())

print len(AllendeDict.keys()), ' objects written'
fileOut = open('allende99.pickle','wb')
pickle.dump(AllendeDict,fileOut,-1)
fileOut.close()

