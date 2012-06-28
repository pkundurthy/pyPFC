import cPickle as pickle

TelDict = {\
'ECLIPSE':{'IWA':4.0,'Dtel':1.8 ,'C0':5.00E-010,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'trauger07'},\
'EPIC'   :{'IWA':2.0,'Dtel':1.5 ,'C0':1.00E-009,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'clampin06'},\
'ESPI'   :{'IWA':4.0,'Dtel':1.5 ,'C0':3.00E-007,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'lyon03'},\
'ExPO'   :{'IWA':2.9,'Dtel':3.0 ,'C0':1.00E-009,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'gezari03'},\
'TPF-C'  :{'IWA':3.9,'Dtel':4.0 ,'C0':5.00E-011,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'crepp09'},\
'UMBRAS' :{'IWA':3.5,'Dtel':1.0 ,'C0':1.00E-008,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'schultz03'},\
'HST'    :{'IWA':3.0,'Dtel':2.4 ,'C0':1.00E-006,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'HST*'   :{'IWA':3.0,'Dtel':2.4 ,'C0':5.00E-010,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'TOPS'   :{'IWA':1.5,'Dtel':1.2 ,'C0':1.00E-010,'eps':0.20,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'guyon07'},\
'DREAM'  :{'IWA':1.5,'Dtel':8.0 ,'C0':5.00E-011,'eps':0.20,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'TPF-C*' :{'IWA':3.9,'Dtel':8.0 ,'C0':5.00E-011,'eps':0.03,'Sfac':2.1,'lbd0':5500,'dlnlbd':0.2 ,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'PECO'   :{'IWA':2.0,'Dtel':1.4 ,'C0':1.00E-010,'eps':0.90,'Sfac':2.1,'lbd0':4000,'dlnlbd':0.3 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'guyon09'},\
'TPF(K)' :{'IWA':3.5,'Dtel':4.0 ,'C0':7.00E-011,'eps':0.44,'Sfac':2.1,'lbd0':6830,'dlnlbd':0.3 ,'XRD': 1.0,'Gain': 1.0,'Refs': 'krist'},\
'TPF(T)' :{'IWA':4.0,'Dtel':8.0 ,'C0':1.00E-010,'eps':0.90,'Sfac':2.1,'lbd0':5000,'dlnlbd':0.75,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'EPIC-N' :{'IWA':2.0,'Dtel':1.65,'C0':1.00E-009,'eps':0.25,'Sfac':2.1,'lbd0':4400,'dlnlbd':0.3 ,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'DAVINC' :{'IWA':0.5,'Dtel':3.3 ,'C0':1.00E-009,'eps':0.25,'Sfac':2.1,'lbd0':6500,'dlnlbd':0.20,'XRD': 1.0,'Gain': 1.0,'Refs': 'shao08'},\
'ATLAST' :{'IWA':2.0,'Dtel':16.0,'C0':1.00E-010,'eps':0.85,'Sfac':2.1,'lbd0':5000,'dlnlbd':0.86,'XRD': 1.0,'Gain': 1.0,'Refs': '         '},\
'ACCESS' :{'IWA':2.3,'Dtel':1.5 ,'C0':2.00E-009,'eps':0.40,'Sfac':2.1,'lbd0':3000,'dlnlbd':0.10,'XRD': 1.0,'Gain': 1.0,'Refs': '         '}\
          }

fileOut = open('telescope.pickle','wb')
pickle.dump(TelDict,fileOut,-1)
fileOut.close()




