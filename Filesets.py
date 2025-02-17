#!/usr/bin/env python
# coding: utf-8

# 
# # ---- All Datasets used for analysis and dasgoclient searches (Need to Finish Filling in!!) ---- #
'''
===========================================================================================================
/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       8.6 GB,   11 files,    9726665 events
/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       152.2 GB, 74 files,  133752091 events
/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,            57.9 GB,  45 files,   46495988 events
/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,            89.8 GB,  65 files,   73330042 events
/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,            87.1 GB,  49 files,   69219288 events
/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD,                 53.1 GB,  52 files,   41564915 events
/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD,                 154.2 GB, 70 files,  120688407 events
/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD,                 156.1 GB, 72 files,  124050331 events
-----------------------------------------------------------------------------------------------------------
                                                                                            625441538 events total
===========================================================================================================
/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,                 67.8 GB,  33 files,   63043590 events
/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,                 107.8 GB, 66 files,   96264601 events
/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,                 52.5 GB,  37 files,   46145204 events
/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,                 110.6 GB, 58 files,   89630771 events
/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,                 147.8 GB, 66 files,  115429972 events
-----------------------------------------------------------------------------------------------------------
                                                                                            410514138 events total
===========================================================================================================
/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD,                 227.6 GB, 146 files, 171484635 events
/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD,                 105.4 GB, 45 files,   78255208 events
/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD,                 96.1 GB,  57 files,   70027804 events
/JetHT/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD,                 493.1 GB, 232 files, 356976276 events
-----------------------------------------------------------------------------------------------------------
                                                                                            676743923 events total
===========================================================================================================
/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,  2.0 GB,   2 files,     2789243 events
/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,  121.5 GB, 70 files,  158145722 events
/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       54.1 GB,  28 files,   67441308 events
/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       76.5 GB,  40 files,   98017996 events
/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       73.3 GB,  47 files,   90984718 events
/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD,       48.6 GB,  43 files,   57465359 events
-----------------------------------------------------------------------------------------------------------
                                                                                                      events total
===========================================================================================================
/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,            102.1 GB, 79 files,  136300266 events
/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,            133.0 GB, 117 files, 165652756 events
/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD,       56.4 GB,  40 files,   70274947 events
/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,            134.3 GB, 78 files,  154618774 events
/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD,            219.2 GB, 115 files, 242140980 events
-----------------------------------------------------------------------------------------------------------
                                                                                            768987723 events total
===========================================================================================================
'''
#
# Weighted JetHT files are for the data driven background (pre-tag region)

import os



def CollectDatasets(redirector_str):
    """
        redirector_str --> string for either running over lpc of coffea-casa
            Two acceptable inputs: 'root://xcache/' Only works in Coffea-Casa Environment
                                   'root://cmsxrootd.fnal.gov/'
            UBWinterFell tests:    '/mnt/data/cms'
    """
    
    
    # uploadDir = 'srv/' for lpcjobqueue shell or TTbarAllHadUproot/ for coffea casa and WinterFell
    
    if 'cmsxrootd' in redirector_str:
        uploadDir = 'srv'
    else:
        uploadDir = 'TTbarAllHadUproot'
    
    filedir = uploadDir+'/nanoAODv9Files/'
    Years = ['UL16', 'UL17', 'UL18']
    VFP = ['preVFP', 'postVFP'] # preVFP unavailable in Winterfell for the moment
    # VFP = ['postVFP'] # Only for simple test in WinterFell
    filesets = {} # To be filled and returned by this function
 
    # ---- Before concatenation with +=, lists should be declard ---- # 
    
    for y in Years:
        if '16' in y:
            for v in VFP:
                filesets[y+v+'_QCD'] = []
                filesets[y+v+'_TTbar_700_1000'] = []
                filesets[y+v+'_TTbar_1000_Inf'] = []
            # ---- JetHT and SingleMu ---- #
            for l in ['', 'B', 'C', 'D', 'E', 'F']:
                filesets[y+'preVFP_JetHT'+l+'_Data'] = []
                filesets[y+'preVFP_SingleMu'+l+'_Data'] = []
            for l in ['', 'F', 'G', 'H']:
                filesets[y+'postVFP_JetHT'+l+'_Data'] = []
                filesets[y+'postVFP_SingleMu'+l+'_Data'] = []
            
            
        elif '17' in y:
            filesets[y+'postVFP_QCD'] = []
            filesets[y+'postVFP_TTbar'] = []
            for l in ['', 'B', 'C', 'D', 'E', 'F']:
                filesets[y+'postVFP_JetHT'+l+'_Data'] = []
                filesets[y+'postVFP_SingleMu'+l+'_Data'] = []
                
        else:
            filesets[y+'postVFP_QCD'] = []
            filesets[y+'postVFP_TTbar'] = []
            for l in ['', 'A', 'B', 'C', 'D']:
                filesets[y+'postVFP_JetHT'+l+'_Data'] = []
                filesets[y+'postVFP_SingleMu'+l+'_Data'] = []
    
    # ---- Loop through years and VFP status, filling the filesets dictionary with the MC file locations from corresponding txt files ---- #
    
    for y in Years:
        if '16' in y:
            for v in VFP:
                # ---- QCD ---- #
                ulqcdfilename = filedir + 'QCD/QCD_NanoAODv9_' + y + '_' + v + '.txt'
                with open(ulqcdfilename) as f:
                    ulqcdfiles = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
                filesets[y+v+'_QCD'] += ulqcdfiles
                
                # ---- TTbar ---- #
                ulttbar700to1000filename = filedir + 'TT/TT_Mtt-700to1000_NanoAODv9_' + y + '_' + v + '.txt'
                with open(ulttbar700to1000filename) as f:
                    ulttbar700to1000files = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
                ulttbar1000toInffilename = filedir + 'TT/TT_Mtt-1000toInf_NanoAODv9_' + y + '_' + v + '.txt'
                with open(ulttbar1000toInffilename) as f:
                    ulttbar1000toInffiles = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
                filesets[y+v+'_TTbar_700_1000'] += ulttbar700to1000files
                filesets[y+v+'_TTbar_1000_Inf'] += ulttbar1000toInffiles
                                
                # ---- JetHT ---- #
                datafilelist = os.listdir(filedir + 'JetHT/')
                for filename in datafilelist:
                    if 'pre' in v:
                        if 'Run2016' in filename: #preVFP
                            with open(filedir + 'JetHT/' + filename) as f:
                                jetdatafiles2016 = [redirector_str + s.strip() for s in f.readlines() if ('HIPM' in s and not s.startswith('#'))] 
                            filesets[y+v+'_JetHT_Data'] += jetdatafiles2016 
                    elif 'post' in v:
                        if 'Run2016' in filename: #postVFP
                            with open(filedir + 'JetHT/' + filename) as f:
                                jetdatafiles2016 = [redirector_str + s.strip() for s in f.readlines() if ('HIPM' not in s and not s.startswith('#'))] 
                            filesets[y+v+'_JetHT_Data'] += jetdatafiles2016
                    
                # ---- Z' Dark Matter Mediator ---- #
                ulZprimeDMfilename = filedir + 'ZprimeDMToTTbar/ZprimeDMToTTbar_NanoAODv9_' + y + '_' + v + '.txt'
                ulDMfiles=[]
                k=0
                for i in range(1000, 5500, 500):
                    with open(ulZprimeDMfilename) as f:
                        ulDMfiles.append([redirector_str + s.strip() for s in f.readlines() if ("ResoIncl_MZp"+str(i) in s and not s.startswith('#'))])
                    filesets[y+v+'_DM'+str(i)] = ulDMfiles[k]
                    k += 1
                    
#                 # ---- RS KK Gluon ---- #
#                 ulRSGluonfilename = filedir + 'RSGluonToTT/RSGluonToTT_NanoAODv9_' + y + '_' + v + '.txt'
#                 ulRSGluonfiles=[]
#                 l=0
#                 for i in range(1000, 5500, 500):
#                     with open(ulRSGluonfilename) as f:
#                         ulRSGluonfiles.append([redirector_str + s.strip() for s in f.readlines() if ("RSGluonToTT_M-"+str(i) in s and not s.startswith('#'))])
#                     filesets[y+v+'_RSGluon'+str(i)] += ulRSGluonfiles[l]
#                     l += 1
                    
        else: # UL17 and UL18
            v = VFP[1] # No preVFP after 2016 Run vertex problem was fixed
            
            # ---- QCD ---- #
            ulqcdfilename = filedir + 'QCD/QCD_NanoAODv9_' + y + '_' + v + '.txt'
            with open(ulqcdfilename) as f:
                ulqcdfiles = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
            filesets[y+v+'_QCD'] += ulqcdfiles

#             # ---- TTbar ---- #
#             ulttbar700to1000filename = filedir + 'TT/TT_Mtt-700to1000_NanoAODv9_' + y + '_' + v + '.txt'
#             with open(ulttbar700to1000filename) as f:
#                 ulttbar700to1000files = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
#             ulttbar1000toInffilename = filedir + 'TT/TT_Mtt-1000toInf_NanoAODv9_' + y + '_' + v + '.txt'
#             with open(ulttbar1000toInffilename) as f:
#                 ulttbar1000toInffiles = [redirector_str + s.strip() for s in f.readlines() if not s.startswith('#')]
#             filesets[y+v+'_TTbar_700_1000'] += ulttbar700to1000files
#             filesets[y+v+'_TTbar_1000_Inf'] += ulttbar1000toInffiles
            
            # ---- JetHT ---- #
            datafilelist = os.listdir(filedir + 'JetHT/')
            for filename in datafilelist: 
                if 'Run2017' in filename: #postVFP
                    with open(filedir + 'JetHT/' + filename) as f:
                        jetdatafiles2017 = [redirector_str + s.strip() for s in f.readlines() if (not s.startswith('#'))] 
                    filesets[y+v+'_JetHT_Data'] += jetdatafiles2017
                elif 'Run2018' in filename: #postVFP
                    with open(filedir + 'JetHT/' + filename) as f:
                        jetdatafiles2018 = [redirector_str + s.strip() for s in f.readlines() if (not s.startswith('#'))] 
                    filesets[y+v+'_JetHT_Data'] += jetdatafiles2018

            # ---- Z' Dark Matter Mediator ---- #
            ulZprimeDMfilename = filedir + 'ZprimeDMToTTbar/ZprimeDMToTTbar_NanoAODv9_' + y + '_' + v + '.txt'
            ulDMfiles=[]
            k=0
            for i in range(1000, 5500, 500):
                with open(ulZprimeDMfilename) as f:
                    ulDMfiles.append([redirector_str + s.strip() for s in f.readlines() if ("ResoIncl_MZp"+str(i) in s and not s.startswith('#'))])
                filesets[y+v+'_DM'+str(i)] = ulDMfiles[k]
                k += 1
                
            # ---- RS KK Gluon ---- #
            ulRSGluonfilename = filedir + 'RSGluonToTT/RSGluonToTT_NanoAODv9_' + y + '_' + v + '.txt'
            ulRSGluonfiles=[]
            l=0
            for i in range(1000, 5500, 500):
                with open(ulRSGluonfilename) as f:
                    ulRSGluonfiles.append([redirector_str + s.strip() for s in f.readlines() if ("RSGluonToTT_M-"+str(i) in s and not s.startswith('#'))])
                filesets[y+v+'_RSGluon'+str(i)] = ulRSGluonfiles[l]
                l += 1
            
    
    # ---- JetHT Eras---- #
    
    datafilelist = os.listdir(filedir + 'JetHT/')
    for filename in datafilelist:
        
        if 'Run2016B' in filename:
            with open(filedir + 'JetHT/' + filename) as b:
                jetdatafiles2016b = [redirector_str + s.strip() for s in b.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_JetHTB_Data'] += jetdatafiles2016b
        elif 'Run2016C' in filename:
            with open(filedir + 'JetHT/' + filename) as c:
                jetdatafiles2016c = [redirector_str + s.strip() for s in c.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_JetHTC_Data'] += jetdatafiles2016c
        elif 'Run2016D' in filename:
            with open(filedir + 'JetHT/' + filename) as d:
                jetdatafiles2016d = [redirector_str + s.strip() for s in d.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_JetHTD_Data'] += jetdatafiles2016d
        elif 'Run2016E' in filename:
            with open(filedir + 'JetHT/' + filename) as e:
                jetdatafiles2016e = [redirector_str + s.strip() for s in e.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_JetHTE_Data'] += jetdatafiles2016e
        elif 'Run2016F' in filename:
            with open(filedir + 'JetHT/' + filename) as fold:
                jetdatafiles2016fold = [redirector_str + s.strip() for s in fold.readlines() if ('HIPM' in s and not s.startswith('#'))]
            with open(filedir + 'JetHT/' + filename) as fnew:
                jetdatafiles2016fnew = [redirector_str + s.strip() for s in fnew.readlines() if ('HIPM' not in s and not s.startswith('#'))]
            filesets['UL16preVFP_JetHTF_Data'] += jetdatafiles2016fold
            filesets['UL16postVFP_JetHTF_Data'] += jetdatafiles2016fnew
        elif 'Run2016G' in filename:
            with open(filedir + 'JetHT/' + filename) as g:
                jetdatafiles2016g = [redirector_str + s.strip() for s in g.readlines() if not s.startswith('#')] 
            filesets['UL16postVFP_JetHTG_Data'] += jetdatafiles2016g
        elif 'Run2016H' in filename:
            with open(filedir + 'JetHT/' + filename) as h:
                jetdatafiles2016h = [redirector_str + s.strip() for s in h.readlines() if not s.startswith('#')] 
            filesets['UL16postVFP_JetHTH_Data'] += jetdatafiles2016h
                
        if 'Run2017B' in filename:
            with open(filedir + 'JetHT/' + filename) as b:
                jetdatafiles2017b = [redirector_str + s.strip() for s in b.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_JetHTB_Data'] += jetdatafiles2017b
        elif 'Run2017C' in filename:
            with open(filedir + 'JetHT/' + filename) as c:
                jetdatafiles2017c = [redirector_str + s.strip() for s in c.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_JetHTC_Data'] += jetdatafiles2017c
        elif 'Run2017D' in filename:
            with open(filedir + 'JetHT/' + filename) as d:
                jetdatafiles2017d = [redirector_str + s.strip() for s in d.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_JetHTD_Data'] += jetdatafiles2017d
        elif 'Run2017E' in filename:
            with open(filedir + 'JetHT/' + filename) as e:
                jetdatafiles2017e = [redirector_str + s.strip() for s in e.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_JetHTE_Data'] += jetdatafiles2017e
        elif 'Run2017F' in filename:
            with open(filedir + 'JetHT/' + filename) as f:
                jetdatafiles2017f = [redirector_str + s.strip() for s in f.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_JetHTF_Data'] += jetdatafiles2017f
                
        if 'Run2018A' in filename:
            with open(filedir + 'JetHT/' + filename) as a:
                jetdatafiles2018a = [redirector_str + s.strip() for s in a.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_JetHTA_Data'] += jetdatafiles2018a
        elif 'Run2018B' in filename:
            with open(filedir + 'JetHT/' + filename) as b:
                jetdatafiles2018b = [redirector_str + s.strip() for s in b.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_JetHTB_Data'] += jetdatafiles2018b
        elif 'Run2018C' in filename:
            with open(filedir + 'JetHT/' + filename) as c:
                jetdatafiles2018c = [redirector_str + s.strip() for s in c.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_JetHTC_Data'] += jetdatafiles2018c
        elif 'Run2018D' in filename:
            with open(filedir + 'JetHT/' + filename) as d:
                jetdatafiles2018d = [redirector_str + s.strip() for s in d.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_JetHTD_Data'] += jetdatafiles2018d
                

    
    # ---- Single Muon ---- #
    datafilelist = os.listdir(filedir + 'SingleMu/')
    for filename in datafilelist:
        
        if 'Run2016B' in filename:
            with open(filedir + 'SingleMu/' + filename) as b:
                jetdatafiles2016b = [redirector_str + s.strip() for s in b.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_SingleMuB_Data'] += jetdatafiles2016b
        elif 'Run2016C' in filename:
            with open(filedir + 'SingleMu/' + filename) as c:
                jetdatafiles2016c = [redirector_str + s.strip() for s in c.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_SingleMuC_Data'] += jetdatafiles2016c
        elif 'Run2016D' in filename:
            with open(filedir + 'SingleMu/' + filename) as d:
                jetdatafiles2016d = [redirector_str + s.strip() for s in d.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_SingleMuD_Data'] += jetdatafiles2016d
        elif 'Run2016E' in filename:
            with open(filedir + 'SingleMu/' + filename) as e:
                jetdatafiles2016e = [redirector_str + s.strip() for s in e.readlines() if not s.startswith('#')] 
            filesets['UL16preVFP_SingleMuE_Data'] += jetdatafiles2016e
        elif 'Run2016F' in filename:
            with open(filedir + 'SingleMu/' + filename) as fold:
                jetdatafiles2016fold = [redirector_str + s.strip() for s in fold.readlines() if ('HIPM' in s and not s.startswith('#'))]
            with open(filedir + 'SingleMu/' + filename) as fnew:
                jetdatafiles2016fnew = [redirector_str + s.strip() for s in fnew.readlines() if ('HIPM' not in s and not s.startswith('#'))]
            filesets['UL16preVFP_SingleMuF_Data'] += jetdatafiles2016fold
            filesets['UL16postVFP_SingleMuF_Data'] += jetdatafiles2016fnew
        elif 'Run2016G' in filename:
            with open(filedir + 'SingleMu/' + filename) as g:
                jetdatafiles2016g = [redirector_str + s.strip() for s in g.readlines() if not s.startswith('#')] 
            filesets['UL16postVFP_SingleMuG_Data'] += jetdatafiles2016g
        elif 'Run2016H' in filename:
            with open(filedir + 'SingleMu/' + filename) as h:
                jetdatafiles2016h = [redirector_str + s.strip() for s in h.readlines() if not s.startswith('#')] 
            filesets['UL16postVFP_SingleMuH_Data'] += jetdatafiles2016h
            
        if 'Run2017B' in filename:
            with open(filedir + 'SingleMu/' + filename) as b:
                jetdatafiles2017b = [redirector_str + s.strip() for s in b.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_SingleMuB_Data'] += jetdatafiles2017b
        elif 'Run2017C' in filename:
            with open(filedir + 'SingleMu/' + filename) as c:
                jetdatafiles2017c = [redirector_str + s.strip() for s in c.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_SingleMuC_Data'] += jetdatafiles2017c
        elif 'Run2017D' in filename:
            with open(filedir + 'SingleMu/' + filename) as d:
                jetdatafiles2017d = [redirector_str + s.strip() for s in d.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_SingleMuD_Data'] += jetdatafiles2017d
        elif 'Run2017E' in filename:
            with open(filedir + 'SingleMu/' + filename) as e:
                jetdatafiles2017e = [redirector_str + s.strip() for s in e.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_SingleMuE_Data'] += jetdatafiles2017e
        elif 'Run2017F' in filename:
            with open(filedir + 'SingleMu/' + filename) as f:
                jetdatafiles2017f = [redirector_str + s.strip() for s in f.readlines()[::3] if not s.startswith('#')] 
            filesets['UL17postVFP_SingleMuF_Data'] += jetdatafiles2017f
                
        if 'Run2018A' in filename:
            with open(filedir + 'SingleMu/' + filename) as a:
                jetdatafiles2018a = [redirector_str + s.strip() for s in a.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_SingleMuA_Data'] += jetdatafiles2018a
        elif 'Run2018B' in filename:
            with open(filedir + 'SingleMu/' + filename) as b:
                jetdatafiles2018b = [redirector_str + s.strip() for s in b.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_SingleMuB_Data'] += jetdatafiles2018b
        elif 'Run2018C' in filename:
            with open(filedir + 'SingleMu/' + filename) as c:
                jetdatafiles2018c = [redirector_str + s.strip() for s in c.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_SingleMuC_Data'] += jetdatafiles2018c
        elif 'Run2018D' in filename:
            with open(filedir + 'SingleMu/' + filename) as d:
                jetdatafiles2018d = [redirector_str + s.strip() for s in d.readlines()[::3] if not s.startswith('#')] 
            filesets['UL18postVFP_SingleMuD_Data'] += jetdatafiles2018d
        
                
    # print(filesets['UL16postVFP_JetHT_Data'])
    # print('==========================================================================================================')
    # print(filesets['UL16postVFP_TTbar'])
                    
    return filesets

# CollectDatasets('root://xcache/')
# xrootdstr1 = 'root://cmseos.fnal.gov//eos/uscms'
# xrootdstr2 = 'root://xcache/' # Only works in Coffea-Casa Environment
# xrootdstr3 = 'root://cmsxrootd-site.fnal.gov/' #If 2nd redirector fails, file is probably here
# xrootdstr4 = 'root://cmsxrootd.fnal.gov/'
