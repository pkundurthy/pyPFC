
import cPickle as pickle

FileRead = open('vanleeuwen07.tsv')
FileLines = FileRead.readlines()

HippDict = {}

index = {0:'HR_RA',1:'DEG_DEC',2:'HIP',\
         3:'n_HIP',4:'RA',5:'DEC',6:'plx',\
         7:'err_plx',8:'Hpmag',9:'bv',10:'err_bv'}

for line in FileLines:
    if not line.startswith('#'):
        lSplit = map(str,line.split('|'))
        if len(lSplit) == 11 and lSplit[3].strip() == '':
            HippDict[lSplit[2].strip()] = {}
            for i in xrange(0,11):
                if i != 2:
                    if i != 3:
                        HippDict[lSplit[2].strip()][index[i]] = float(lSplit[i].strip())
                    else:
                        HippDict[lSplit[2].strip()][index[i]] = lSplit[i].strip()

print len(HippDict.keys()), ' objects written'
fileOut = open('hipp07.pickle','wb')
pickle.dump(HippDict,fileOut,-1)
fileOut.close()

