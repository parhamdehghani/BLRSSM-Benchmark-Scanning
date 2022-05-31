#!/usr/bin/env python
# -*- coding: utf-8 -*-

######## Packages ###########
from math import *
import fnmatch
import numpy as np
import os
import sys
#sys.path.append("/lustre03/project/6005777/pdehghan/Research/pyslha")
#sys.path.append("/lustre03/project/6005777/pdehghan/Research/xslha")
import xslha
import pyslha
import pandas as pd
import signal
import time

from MyPySLHA import *


######## Writing LesHouches input files ###############
def write(blocks, file):
    with open(file, 'w+') as f:
        for b in blocks:
            write_block_head(b, f)
            write_block_entries(b, blocks[b], f)

def write_block_entries(block_name, values, file):
    for v in values.keys():
        if block_name == 'MODSEL':
            file.write(' %s %i # \n' % (v, int(values[v])))
        else:
            file.write(' %s %10.4e # \n' % (v, float(values[v])))

def write_block_head(name, file):
    file.write("Block " + name.upper() + " # \n")
######## Current LesHouches File Paths ###############
LHAFileFullPath    = os.path.abspath("LesHouches.in.BLRinvSeesaw")
LHAFiledirPath     = os.path.dirname(LHAFileFullPath)
LHAFileName        = os.path.basename(LHAFileFullPath)
newLHAFileFullPath = os.path.abspath("LesHouches.in.BLRinvSeesaw_new")
newLHAFileName     = os.path.basename(newLHAFileFullPath)
######## SLHA File Paths ################################
SLHAFileFullPath   = os.path.abspath("SPheno.spc.BLRinvSeesaw")
SLHAFiledirPath    = os.path.dirname(SLHAFileFullPath)
SLHAFileName       = os.path.basename(SLHAFileFullPath)
destPathforNewSLHA = os.path.dirname("SPhenoOutputs/SPheno.spc.BLRinvSeesaw.*")
######## Desired MicrOMEGAs Output File Paths ##########
PathforMicrOMEGAsResult = os.path.abspath("omg.out")
PathforChannelsOutput = os.path.abspath("channels.out")
PathforDecaysOutput = os.path.abspath("DECAYS.out")
########################################################
# maximum of the solutions that satisfy the LHC constraints
fileno = 0 
MaxNumberOfSolution = 200
chosen = pd.read_csv("chosen.csv")
relic_density = chosen["relic density"][0]
######## Lists for Sotring ###############
m0_list = []
m12_list = []
TanBeta_list = []
A0_list = []
TanBetaR_list = []
VR_list = []
SignumMu_list = []
MuR_list = []
#SignumMuR_list = []
YvDIG_list = []
YsDIG_list = []
relic_list = []
DD_SI_list = []
DD_SD_p_list = []
DD_SD_n_list = []
relic_boolean_list = []
neutralino_mass_list = []
sneutrino_mass_list = []

# Initiation and building the primary LesHouche
p = subprocess.call("rm -f SPhenoOutputs/* micrOMEGAS.csv Les*new *Seesaw",shell=True)
p = subprocess.call("rm -f "+SLHAFileName,shell=True)

SPheno_input = xslha.read("LesHouches.in.BLRinvSeesaw_init")
#SPheno_input.blocks['MINPAR']['1'] = chosen["m0"][0]
#SPheno_input.blocks['MINPAR']['2'] = chosen["m12"][0]
#SPheno_input.blocks['MINPAR']['4'] = chosen["SignumMu"][0]
#SPheno_input.blocks['MINPAR']['5'] = chosen["A0"][0]
#SPheno_input.blocks['MINPAR']['6'] = chosen["SignumMuR"][0]
#SPheno_input.blocks['MINPAR']['7'] = chosen["TanBeta"][0]
#SPheno_input.blocks['MINPAR']['9'] = chosen["TanBetaR"][0]
#SPheno_input.blocks['MINPAR']['11'] = chosen["VR"][0]
#SPheno_input.blocks['YSIN']['1,1'] = chosen["YsDIG"][0]
#SPheno_input.blocks['YSIN']['2,2'] = chosen["YsDIG"][0]
#SPheno_input.blocks['YSIN']['3,3'] = chosen["YsDIG"][0]
#SPheno_input.blocks['YVIN']['1,1'] = chosen["YvDIG"][0]
#SPheno_input.blocks['YVIN']['2,2'] = chosen["YvDIG"][0]
#SPheno_input.blocks['YVIN']['3,3'] = chosen["YvDIG"][0]
write(SPheno_input.blocks,LHAFileName)
######################################################
while fileno < MaxNumberOfSolution:
    print("Updated relic density is",relic_density)

    good_relic = relic_density >= 0.09 and relic_density <= 0.14
    upper_relic = relic_density > 0.14 and relic_density <= 0.2
    lower_relic = relic_density > 0 and relic_density < 0.09

    print("good_relic is ",good_relic)
    print("lower_relic is ",lower_relic)
    print("upper_relic is ",upper_relic)

    LHA = MyPySLHA()
    LHA.LHAFileFullPath         = LHAFileFullPath
    LHA.LHAFiledirPath          = LHAFiledirPath
    LHA.LHAFileName             = LHAFileName
    LHA.newLHAFileFullPath      = newLHAFileFullPath
    LHA.newLHAFileName          = newLHAFileName
    LHA.SLHAFileFullPath        = SLHAFileFullPath
    LHA.SLHAFiledirPath         = SLHAFiledirPath
    LHA.SLHAFileName            = SLHAFileName
    LHA.destPathforNewSLHA      = destPathforNewSLHA
    LHA.PathforMicrOMEGAsResult = PathforMicrOMEGAsResult
    LHA.PathforChannelsOutput   = PathforChannelsOutput
    
    if LHA.CheckLHAexist(LHA.LHAFileName):
        with open(LHA.LHAFileName, 'r') as file:
            lines = file.readlines()
            SPheno_input = xslha.read(LHA.LHAFileName)
            m0 = SPheno_input.blocks['MINPAR']['1']
            m12 = SPheno_input.blocks['MINPAR']['2'] 
            SignumMu = SPheno_input.blocks['MINPAR']['4']
            MuR = SPheno_input.blocks['MINPAR']['5']
            A0 = SPheno_input.blocks['MINPAR']['3'] 
            #SignumMuR = SPheno_input.blocks['MINPAR']['6'] 
            TanBeta = SPheno_input.blocks['MINPAR']['6'] 
            TanBetaR = SPheno_input.blocks['MINPAR']['7']
            VR = SPheno_input.blocks['MINPAR']['8']
            YsDIG = SPheno_input.blocks['YSIN']['1,1'] 
            YsDIG = SPheno_input.blocks['YSIN']['2,2'] 
            YsDIG = SPheno_input.blocks['YSIN']['3,3'] 
            YvDIG = SPheno_input.blocks['YVIN']['1,1'] 
            YvDIG = SPheno_input.blocks['YVIN']['2,2']
            YvDIG = SPheno_input.blocks['YVIN']['3,3'] 
            if (good_relic):
                m0      += np.random.uniform(-2., 2.)
                m12      += np.random.uniform(-2.,2.)
                TanBeta      += np.random.uniform(-0.2, 0.2)
                A0      += np.random.uniform(-2., 2.)
                TanBetaR      += np.random.uniform(-0.005,.005)
                VR          += np.random.uniform(-5,5)
                SignumMu = 1
                MuR += np.random.uniform(-5.,5.)
                #SignumMuR = LHA.signGENERATOR()
                YvDIG += np.random.uniform(-.005,.005)
                YsDIG += np.random.uniform(-.005,.005)
            elif (upper_relic or lower_relic):
                m0      += np.random.uniform(-2., 2.)
                m12      += np.random.uniform(-2.,2.)
                TanBeta      += np.random.uniform(-0.2, 0.2)
                A0      += np.random.uniform(-2., 2.)
                TanBetaR      += np.random.uniform(-0.005,.005)
                VR          += np.random.uniform(-5,5)
                SignumMu = 1
                #SignumMuR = LHA.signGENERATOR()
                MuR += np.random.uniform(-5.,5.)
                YvDIG += np.random.uniform(-.005,.005)
                YsDIG += np.random.uniform(-.005,.005)
            
            SPheno_input.blocks['MINPAR']['1'] = m0
            SPheno_input.blocks['MINPAR']['2'] = m12
            SPheno_input.blocks['MINPAR']['4'] = SignumMu
            SPheno_input.blocks['MINPAR']['5'] = MuR
            SPheno_input.blocks['MINPAR']['3'] = A0
            #SPheno_input.blocks['MINPAR']['6'] = SignumMuR
            SPheno_input.blocks['MINPAR']['6'] = TanBeta
            SPheno_input.blocks['MINPAR']['7'] = TanBetaR
            SPheno_input.blocks['MINPAR']['8'] = VR
            SPheno_input.blocks['YSIN']['1,1'] = YsDIG
            SPheno_input.blocks['YSIN']['2,2'] = YsDIG
            SPheno_input.blocks['YSIN']['3,3'] = YsDIG
            SPheno_input.blocks['YVIN']['1,1'] = YvDIG
            SPheno_input.blocks['YVIN']['2,2'] = YvDIG
            SPheno_input.blocks['YVIN']['3,3'] = YvDIG
            # writing a new LHA file based on updated parameters
            write(SPheno_input.blocks, LHA.newLHAFileName)
            
########SPheno Run####################################################################
        LHA.RunSPheno(LHA.newLHAFileName)
############# Load SPheno Output into PySLHA #####################################################
        if LHA.CheckLHAexist(LHA.SLHAFileName):
            #LHA.Erase(LHA.newLHAFileName)
            p = subprocess.call("awk '{if(($2==12 && $3 !~ /E/) || ($2==14 && $3 !~ /E/) || ($2==16 && $3 !~ /E/) ) $3=0; print}' SPheno.spc.BLRinvSeesaw  > tmp.txt",shell=True)
            p = subprocess.call("cat tmp.txt > SPheno.spc.BLRinvSeesaw",shell=True)
            #p = subprocess.call("rm tmp.txt",shell=True)
            if (os.path.getsize(LHA.SLHAFileName)!= 0):
                try:
                    LHA.LoadLHAFile(LHA.SLHAFileName)
                    # checking the MASS block
                    LHA.allcontent.blocks["MASS"][25]
                    LHA.allcontent.blocks["MASS"][35]
                    LHA.allcontent.blocks["MASS"][225]
                    LHA.allcontent.blocks["MASS"][232]
                    LHA.allcontent.blocks["MASS"][99]
                    LHA.allcontent.blocks["MASS"][1000021]
                    LHA.allcontent.blocks["MASS"][1000022]
                    LHA.allcontent.blocks["MASS"][1000024]
                    #LHA.allcontent.blocks["ANGLES"][10]
                    LHA.allcontent.blocks["MASS"][1000015]
                    LHA.allcontent.blocks["MASS"][1000011]
                    LHA.allcontent.blocks["MASS"][1000006]
                    LHA.allcontent.blocks["MASS"][1000005]
                    LHA.allcontent.blocks["MASS"][1000013]

                    # checking the BPhysics
                    LHA.allcontent.blocks["FLAVORKITQFV"][200]
                    LHA.allcontent.blocks["FLAVORKITQFV"][4006]
                    LHA.allcontent.blocks["FLAVORKITQFV"][503]
                except:
                    continue
            else:
                continue
            print("******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************** point written ************************************************************************************************************************")
           
############# Check Constraints  ################################################################
            if  (LHA.MassBounds() and LHA.CheckBPhysics() and LHA.CheckWhoIsLSP() and LHA.benchmark_check(SLHAFileFullPath)):
                print("LHC constraint+LSP done!")
                # get the mass for neutralino and sneutrino
                neutralino_mass = LHA.allcontent.blocks["MASS"][1000022]
                sneutrino_mass = LHA.allcontent.blocks["MASS"][1000012]
                # micromegas run to get new_relic_density
                p = subprocess.call("CalcOmega_with_DDetection_MOv5 "+LHA.SLHAFileName+" > information.txt",shell=True)
                LHA.MicrOMEGA_Result_exist = os.path.isfile(LHA.PathforMicrOMEGAsResult)
                LHA.Channels_exist = os.path.isfile(LHA.PathforChannelsOutput)
                if (LHA.MicrOMEGA_Result_exist and LHA.Channels_exist):
                    # new_relic_density
                    p = os.popen("awk 'FNR==1 {print $2}' omg.out")
                    number = p.read()
                    p.close()
                    new_relic_density = float(number[0:len(number)-1])
                    print("New relic is ", new_relic_density)
                    if (upper_relic):
                        if (new_relic_density > 0.14 and new_relic_density < relic_density):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        elif (new_relic_density > 0.09 and new_relic_density < 0.14):
                            relic_density = new_relic_density
                            # Get some information from micromegas output
                            # DD_SI
                            p = os.popen("awk '/ proton/{print $3}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SI = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_p
                            p = os.popen("awk '/ proton/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_p = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_n
                            p = os.popen("awk '/ neutron/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_n = '%1.3e' %float(number[0:len(number)-1])

                            # appending the list
                            m0_list.append(m0)
                            m12_list.append(m12)
                            TanBeta_list.append(TanBeta)
                            A0_list.append(A0)
                            TanBetaR_list.append(TanBetaR)
                            VR_list.append(VR)
                            SignumMu_list.append(SignumMu)
                            MuR_list.append(MuR)
                            #SignumMuR_list.append(SignumMuR)
                            YvDIG_list.append(YvDIG)
                            YsDIG_list.append(YsDIG)
                            neutralino_mass_list.append(neutralino_mass)
                            sneutrino_mass_list.append(sneutrino_mass)
                            relic_list.append(relic_density)
                            DD_SI_list.append(DD_SI)
                            DD_SD_p_list.append(DD_SD_p)
                            DD_SD_n_list.append(DD_SD_n)
                            relic_boolean_list.append("True")


                            # SPheno writing
                            fileno = len(fnmatch.filter(os.listdir(LHA.destPathforNewSLHA), "SPheno.spc.BLRinvSeesaw.*"))
                            newfileno = fileno + 1
                            LHA.NewSLHAFileName = "SPheno.spc.BLRinvSeesaw."+str(newfileno)
                            LHA.NewSLHAFileFullPath = "SPhenoOutputs/" + LHA.NewSLHAFileName
                            with open("SPheno.spc.BLRinvSeesaw", 'r') as file:
                                new_data= file.read()
                            with open(LHA.NewSLHAFileFullPath, 'w') as newfile:
                                newfile.write(new_data)
                            # micromegas writing
                            LHA.MicromegasNewFileName = os.path.basename("Micromegas."+str(newfileno))
                            LHA.FullDestForMicromegas = "SPhenoOutputs/" + LHA.MicromegasNewFileName
                            LHA.RenameAndCopy(LHA.PathforMicrOMEGAsResult, LHA.FullDestForMicromegas)
                            LHA.ChannelsNewFileName = os.path.basename("Channels."+str(newfileno))
                            LHA.FullDestForChannels = "SPhenoOutputs/" + LHA.ChannelsNewFileName
                            LHA.RenameAndCopy(LHA.PathforChannelsOutput, LHA.FullDestForChannels)
                            LHA.RenameAndCopy(LHA.SLHAFileName,LHA.NewSLHAFileFullPath)
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            # writing dataframe object
                            df = pd.DataFrame({'m0': m0_list,
                                       'm12': m12_list,
                                       'A0': A0_list,
                                       'VR': VR_list,
                                       'TanBeta': TanBeta_list,
                                       'TanBetaR': TanBetaR_list,
                                       'YvDIG': YvDIG_list,
                                       'YsDIG': YsDIG_list,
                                       'SignumMu': SignumMu_list,
                                       'MuR': MuR_list,
                                       'relic density': relic_list,
                                       'sneutrino mass': sneutrino_mass_list,
                                       'neutralino mass': neutralino_mass_list,
                                       'DD_SI': DD_SI_list,
                                       'DD_SD_p': DD_SD_p_list,
                                       'DD_SD_n': DD_SD_n_list,
                                       'relic_boolean': relic_boolean_list})
                            df.to_csv('micrOMEGAS.csv')
                            LHA.Erase(LHA.PathforMicrOMEGAsResult)
                            LHA.Erase(LHA.PathforChannelsOutput)
                            LHA.Erase(LHA.SLHAFileName)



                        elif (new_relic_density > 0 and new_relic_density < 0.09):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        else:
                            LHA.Erase(LHA.SLHAFileName)
                            LHA.Erase(LHA.newLHAFileName)
                            continue
                      
                      
################################################################                      
                    if (good_relic):
                        if (new_relic_density > 0.14 and new_relic_density < 0.17):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        elif (new_relic_density > 0.09 and new_relic_density < 0.14):
                            relic_density = new_relic_density
                            # Get some information from micromegas output
                            # DD_SI
                            p = os.popen("awk '/ proton/{print $3}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SI = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_p
                            p = os.popen("awk '/ proton/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_p = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_n
                            p = os.popen("awk '/ neutron/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_n = '%1.3e' %float(number[0:len(number)-1])

                            # appending the list
                            m0_list.append(m0)
                            m12_list.append(m12)
                            TanBeta_list.append(TanBeta)
                            A0_list.append(A0)
                            TanBetaR_list.append(TanBetaR)
                            VR_list.append(VR)
                            SignumMu_list.append(SignumMu)
                            MuR_list.append(MuR)
                            YvDIG_list.append(YvDIG)
                            YsDIG_list.append(YsDIG)
                            neutralino_mass_list.append(neutralino_mass)
                            sneutrino_mass_list.append(sneutrino_mass)
                            relic_list.append(relic_density)
                            DD_SI_list.append(DD_SI)
                            DD_SD_p_list.append(DD_SD_p)
                            DD_SD_n_list.append(DD_SD_n)
                            relic_boolean_list.append("True")


                            # SPheno writing
                            fileno = len(fnmatch.filter(os.listdir(LHA.destPathforNewSLHA), "SPheno.spc.BLRinvSeesaw.*"))
                            newfileno = fileno + 1
                            LHA.NewSLHAFileName = "SPheno.spc.BLRinvSeesaw."+str(newfileno)
                            LHA.NewSLHAFileFullPath = "SPhenoOutputs/" + LHA.NewSLHAFileName
                            with open("SPheno.spc.BLRinvSeesaw", 'r') as file:
                                new_data= file.read()
                            with open(LHA.NewSLHAFileFullPath, 'w') as newfile:
                                newfile.write(new_data)
                            # micromegas writing
                            LHA.MicromegasNewFileName = os.path.basename("Micromegas."+str(newfileno))
                            LHA.FullDestForMicromegas = "SPhenoOutputs/" + LHA.MicromegasNewFileName
                            LHA.RenameAndCopy(LHA.PathforMicrOMEGAsResult, LHA.FullDestForMicromegas)
                            LHA.ChannelsNewFileName = os.path.basename("Channels."+str(newfileno))
                            LHA.FullDestForChannels = "SPhenoOutputs/" + LHA.ChannelsNewFileName
                            LHA.RenameAndCopy(LHA.PathforChannelsOutput, LHA.FullDestForChannels)
                            LHA.RenameAndCopy(LHA.SLHAFileName,LHA.NewSLHAFileFullPath)
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            # writing dataframe object
                            df = pd.DataFrame({'m0': m0_list,
                                       'm12': m12_list,
                                       'A0': A0_list,
                                       'VR': VR_list,
                                       'TanBeta': TanBeta_list,
                                       'TanBetaR': TanBetaR_list,
                                       'YvDIG': YvDIG_list,
                                       'YsDIG': YsDIG_list,
                                       'SignumMu': SignumMu_list,
                                       'MuR': MuR_list,
                                       'relic density': relic_list,
                                       'sneutrino mass': sneutrino_mass_list,
                                       'neutralino mass': neutralino_mass_list,
                                       'DD_SI': DD_SI_list,
                                       'DD_SD_p': DD_SD_p_list,
                                       'DD_SD_n': DD_SD_n_list,
                                       'relic_boolean': relic_boolean_list})
                            df.to_csv('micrOMEGAS.csv')
                            LHA.Erase(LHA.PathforMicrOMEGAsResult)
                            LHA.Erase(LHA.PathforChannelsOutput)
                            LHA.Erase(LHA.SLHAFileName)



                        elif (new_relic_density > 0.07 and new_relic_density < 0.09):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        else:
                            LHA.Erase(LHA.SLHAFileName)
                            LHA.Erase(LHA.newLHAFileName)
                            continue
  

####################################################################################
                    if (lower_relic):
                        if (new_relic_density > 0.14 and new_relic_density < 0.2):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        elif (new_relic_density > 0.09 and new_relic_density < 0.14):
                            relic_density = new_relic_density
                            # Get some information from micromegas output
                            # DD_SI
                            p = os.popen("awk '/ proton/{print $3}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SI = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_p
                            p = os.popen("awk '/ proton/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_p = '%1.3e' %float(number[0:len(number)-1])
                            # DD_SD_n
                            p = os.popen("awk '/ neutron/{print $5}' information.txt")
                            number = p.read()
                            p.close()
                            DD_SD_n = '%1.3e' %float(number[0:len(number)-1])

                            # appending the list
                            m0_list.append(m0)
                            m12_list.append(m12)
                            TanBeta_list.append(TanBeta)
                            A0_list.append(A0)
                            TanBetaR_list.append(TanBetaR)
                            VR_list.append(VR)
                            SignumMu_list.append(SignumMu)
                            MuR_list.append(MuR)
                            YvDIG_list.append(YvDIG)
                            YsDIG_list.append(YsDIG)
                            neutralino_mass_list.append(neutralino_mass)
                            sneutrino_mass_list.append(sneutrino_mass)
                            relic_list.append(relic_density)
                            DD_SI_list.append(DD_SI)
                            DD_SD_p_list.append(DD_SD_p)
                            DD_SD_n_list.append(DD_SD_n)
                            relic_boolean_list.append("True")


                            # SPheno writing
                            fileno = len(fnmatch.filter(os.listdir(LHA.destPathforNewSLHA), "SPheno.spc.BLRinvSeesaw.*"))
                            newfileno = fileno + 1
                            LHA.NewSLHAFileName = "SPheno.spc.BLRinvSeesaw."+str(newfileno)
                            LHA.NewSLHAFileFullPath = "SPhenoOutputs/" + LHA.NewSLHAFileName
                            with open("SPheno.spc.BLRinvSeesaw", 'r') as file:
                                new_data= file.read()
                            with open(LHA.NewSLHAFileFullPath, 'w') as newfile:
                                newfile.write(new_data)
                            # micromegas writing
                            LHA.MicromegasNewFileName = os.path.basename("Micromegas."+str(newfileno))
                            LHA.FullDestForMicromegas = "SPhenoOutputs/" + LHA.MicromegasNewFileName
                            LHA.RenameAndCopy(LHA.PathforMicrOMEGAsResult, LHA.FullDestForMicromegas)
                            LHA.ChannelsNewFileName = os.path.basename("Channels."+str(newfileno))
                            LHA.FullDestForChannels = "SPhenoOutputs/" + LHA.ChannelsNewFileName
                            LHA.RenameAndCopy(LHA.PathforChannelsOutput, LHA.FullDestForChannels)
                            LHA.RenameAndCopy(LHA.SLHAFileName,LHA.NewSLHAFileFullPath)
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            # writing dataframe object
                            df = pd.DataFrame({'m0': m0_list,
                                       'm12': m12_list,
                                       'A0': A0_list,
                                       'VR': VR_list,
                                       'TanBeta': TanBeta_list,
                                       'TanBetaR': TanBetaR_list,
                                       'YvDIG': YvDIG_list,
                                       'YsDIG': YsDIG_list,
                                       'SignumMu': SignumMu_list,
                                       'MuR': MuR_list,
                                       'relic density': relic_list,
                                       'sneutrino mass': sneutrino_mass_list,
                                       'neutralino mass': neutralino_mass_list,
                                       'DD_SI': DD_SI_list,
                                       'DD_SD_p': DD_SD_p_list,
                                       'DD_SD_n': DD_SD_n_list,
                                       'relic_boolean': relic_boolean_list})
                            df.to_csv('micrOMEGAS.csv')
                            LHA.Erase(LHA.PathforMicrOMEGAsResult)
                            LHA.Erase(LHA.PathforChannelsOutput)
                            LHA.Erase(LHA.SLHAFileName)



                        elif (new_relic_density > relic_density and new_relic_density < 0.09):
                            relic_density = new_relic_density
                            p = subprocess.call("cp LesHouches.in.BLRinvSeesaw_new LesHouches.in.BLRinvSeesaw",shell=True)
                            p = subprocess.call("rm -f LesHouches.in.BLRinvSeesaw_new",shell=True)
                            LHA.Erase(LHA.SLHAFileName)

                        else:
                            LHA.Erase(LHA.SLHAFileName)
                            LHA.Erase(LHA.newLHAFileName)
                            continue
                
                else:
                    LHA.Erase(LHA.SLHAFileName)
                    LHA.Erase(LHA.newLHAFileName)
                    continue
            else:
                LHA.Erase(LHA.SLHAFileName)
                LHA.Erase(LHA.newLHAFileName)
                continue
        else:
            LHA.Erase(LHA.newLHAFileName)
            continue
    else:
        break
        print("No initial LesHouche file!")
####################ENDENDENDENDEND##############################################

