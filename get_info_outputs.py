#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
from pandas import Series, DataFrame
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb
import sys
import pyslha
import xslha
rcParams['figure.figsize'] = 10, 10
#plt.rcParams['text.usetex'] = True
sb.set_style('whitegrid')

# Input file
m0=[]
m12=[]
A0=[]
signmuR=[]
tanbeta=[]
tanbetaR=[]
VR=[]
Ys=[]
Yv=[]

# Outputs
DD_SI=[]
relic_density=[]
Gluino_LHC = []
Cha1_LHC = []
MZp_LHC = []
stau_LHC = []
selectron_LHC = []
stop_LHC = []
sbottom_LHC = []
smuon_LHC = []
neutralino_LHC = []
sneutrino_LHC = []
mu_LHC = []
muR_LHC = []
h1_LHC = []
h2_LHC = []
h3_LHC = []

M1_LHC = []
M2_LHC = []
M3_LHC = []
M4_LHC = []

ZR_LHC = []


n_runs = len(os.listdir('/home/Universe/Research/BLRSSM/Cluster_run/Primary_run'))
n_runs1 = len(os.listdir('/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run'))
"""
for i in range(1,n_runs+1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Primary_run/SPhenoOutputs'+str(i)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(i,file)
            content = pyslha.read(path + '/' + file)

            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino<sneutrino
            

            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128
            
            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
            
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
            	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
           	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
            
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])
                
                Cha1_LHC.append(content.blocks["MASS"][1000024])
                MZp_LHC.append(content.blocks["MASS"][99])
                stau_LHC.append(content.blocks["MASS"][1000015])
                selectron_LHC.append(content.blocks["MASS"][1000011])
                stop_LHC.append(content.blocks["MASS"][1000006])
                sbottom_LHC.append(content.blocks["MASS"][1000005])
                smuon_LHC.append(content.blocks["MASS"][1000013])
                neutralino_LHC.append(neutralino)
                sneutrino_LHC.append(sneutrino)
                Gluino_LHC.append(content.blocks["MASS"][1000021])
                mu_LHC.append(content.blocks['HMIX'][1])
                muR_LHC.append(content.blocks['HMIX'][9])

                M1_LHC.append(content.blocks['MSOFT'][1])
                M2_LHC.append(content.blocks['MSOFT'][2])
                M3_LHC.append(content.blocks['MSOFT'][3])
                M4_LHC.append(content.blocks['MSOFT'][4])
                higgs = [content.blocks["MASS"][25],content.blocks["MASS"][35], content.blocks["MASS"][225]]
                higgs.sort()
                h1_LHC.append(higgs[0])
                h2_LHC.append(higgs[1])
                h3_LHC.append(higgs[2])
                ZR_LHC.append(content.blocks["MASS"][99])
            
            

df = pd.DataFrame({
    'm0': m0,
    'm12': m12,
    'A0': A0,
    'tanbeta': tanbeta,
    'tanbetaR': tanbetaR,
    'VR': VR,
    'signmuR': signmuR,
    'Ys': Ys,
    'Yv': Yv,
    'DD': DD_SI,
    'relic_density': relic_density,
    'neutralino_mass': neutralino_LHC,
    'sneutrino_mass': sneutrino_LHC,
    'gluino_mass': Gluino_LHC,
    'Cha1_mass': Cha1_LHC,
    'Mzp_mass':MZp_LHC,
    'stau_mass': stau_LHC,
    'selectron_mass': selectron_LHC,
    'stop_mass':stop_LHC,
    'sbottom_mass': sbottom_LHC,
    'smuon_mass': smuon_LHC,
    'mu_value': mu_LHC,
    'muR_value': muR_LHC,
    'h1_mass': h1_LHC,
    'h2_mass': h2_LHC,
    'h3_mass': h3_LHC,
    'M1': M1_LHC,
    'M2': M2_LHC,
    'M3': M3_LHC,
    'M4': M4_LHC,
    'ZR': ZR_LHC
})
df.to_csv('neutralino_LSP_LHC.csv')
"""
# Input file
m0=[]
m12=[]
A0=[]
signmuR=[]
tanbeta=[]
tanbetaR=[]
VR=[]
Ys=[]
Yv=[]

# Outputs
DD_SI=[]
relic_density=[]
Gluino_benchmark = []
Cha1_benchmark = []
MZp_benchmark = []
stau_benchmark = []
selectron_benchmark = []
stop_benchmark = []
sbottom_benchmark = []
smuon_benchmark = []
neutralino_benchmark = []
sneutrino_benchmark = []
mu_benchmark  = []
muR_benchmark  = []
h1_benchmark = []
h2_benchmark = []
h3_benchmark = []

M1_benchmark = []
M2_benchmark = []
M3_benchmark = []
M4_benchmark = []

ZR_BH = []

for j in range(0,n_runs1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run/SPhenoOutputs'+str(j)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(j,file)
            content = pyslha.read(path + '/' + file)
        
            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino<sneutrino


            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128

            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
        	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
                
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
       	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
                
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])
                
                # Outputs
                Cha1_benchmark.append(content.blocks["MASS"][1000024])
                MZp_benchmark.append(content.blocks["MASS"][99])
                stau_benchmark.append(content.blocks["MASS"][1000015])
                selectron_benchmark.append(content.blocks["MASS"][1000011])
                stop_benchmark.append(content.blocks["MASS"][1000006])
                sbottom_benchmark.append(content.blocks["MASS"][1000005])
                smuon_benchmark.append(content.blocks["MASS"][1000013])
                neutralino_benchmark.append(neutralino)
                sneutrino_benchmark.append(sneutrino)
                Gluino_benchmark.append(content.blocks["MASS"][1000021])
                mu_benchmark.append(content.blocks['HMIX'][1])
                muR_benchmark.append(content.blocks['HMIX'][9])

                M1_benchmark.append(content.blocks['MSOFT'][1])
                M2_benchmark.append(content.blocks['MSOFT'][2])
                M3_benchmark.append(content.blocks['MSOFT'][3])
                M4_benchmark.append(content.blocks['MSOFT'][4])

                higgs = [content.blocks["MASS"][25],content.blocks["MASS"][35], content.blocks["MASS"][225]]
                higgs.sort()
                h1_benchmark.append(higgs[0])
                h2_benchmark.append(higgs[1])
                h3_benchmark.append(higgs[2])

                ZR_BH.append(content.blocks["MASS"][99])

df = pd.DataFrame({
    'm0': m0,
    'm12': m12,
    'A0': A0,
    'tanbeta': tanbeta,
    'tanbetaR': tanbetaR,
    'VR': VR,
    'signmuR': signmuR,
    'Ys': Ys,
    'Yv': Yv,
    'DD': DD_SI,
    'relic_density': relic_density,
    'neutralino_mass': neutralino_benchmark,
    'sneutrino_mass': sneutrino_benchmark,
    'gluino_mass': Gluino_benchmark,
    'Cha1_mass': Cha1_benchmark,
    'Mzp_mass':MZp_benchmark,
    'stau_mass': stau_benchmark,
    'selectron_mass': selectron_benchmark,
    'stop_mass':stop_benchmark,
    'sbottom_mass': sbottom_benchmark,
    'smuon_mass': smuon_benchmark,
    'mu_value': mu_benchmark,
    'muR_value': muR_benchmark,
    'h1_mass': h1_benchmark,
    'h2_mass': h2_benchmark,
    'h3_mass': h3_benchmark,
    'M1': M1_benchmark,
    'M2': M2_benchmark,
    'M3': M3_benchmark,
    'M4': M4_benchmark,
    'ZR': ZR_BH
})
df.to_csv('neutralino_LSP_benchmark.csv')
"""
# Input file
m0=[]
m12=[]
A0=[]
signmuR=[]
tanbeta=[]
tanbetaR=[]
VR=[]
Ys=[]
Yv=[]

# Outputs
DD_SI=[]
relic_density=[]
Gluino_LHC = []
Cha1_LHC = []
MZp_LHC = []
stau_LHC = []
selectron_LHC = []
stop_LHC = []
sbottom_LHC = []
smuon_LHC = []
neutralino_LHC = []
sneutrino_LHC = []
mu_LHC = []
muR_LHC = []
h1_LHC = []
h2_LHC = []
h3_LHC = []

M1_LHC = []
M2_LHC = []
M3_LHC = []
M4_LHC = []

ZR_LHC = []

for i in range(1,n_runs+1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Primary_run/SPhenoOutputs'+str(i)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(i,file)
            content = pyslha.read(path + '/' + file)

            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino>sneutrino


            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128
        
            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
    
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
        	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
       	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
            
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])
            
                Cha1_LHC.append(content.blocks["MASS"][1000024])
                MZp_LHC.append(content.blocks["MASS"][99])
                stau_LHC.append(content.blocks["MASS"][1000015])
                selectron_LHC.append(content.blocks["MASS"][1000011])
                stop_LHC.append(content.blocks["MASS"][1000006])
                sbottom_LHC.append(content.blocks["MASS"][1000005])
                smuon_LHC.append(content.blocks["MASS"][1000013])
                neutralino_LHC.append(neutralino)
                sneutrino_LHC.append(sneutrino)
                Gluino_LHC.append(content.blocks["MASS"][1000021])
                mu_LHC.append(content.blocks['HMIX'][1])
                muR_LHC.append(content.blocks['HMIX'][9])
                
                M1_LHC.append(content.blocks['MSOFT'][1])
                M2_LHC.append(content.blocks['MSOFT'][2])
                M3_LHC.append(content.blocks['MSOFT'][3])
                M4_LHC.append(content.blocks['MSOFT'][4])
                higgs = [content.blocks["MASS"][25],content.blocks["MASS"][35], content.blocks["MASS"][225]]
                higgs.sort()
                h1_LHC.append(higgs[0])
                h2_LHC.append(higgs[1])
                h3_LHC.append(higgs[2])
            
                ZR_LHC.append(content.blocks["MASS"][99])
            
            

df = pd.DataFrame({
    'm0': m0,
    'm12': m12,
    'A0': A0,
    'tanbeta': tanbeta,
    'tanbetaR': tanbetaR,
    'VR': VR,
    'signmuR': signmuR,
    'Ys': Ys,
    'Yv': Yv,
    'DD': DD_SI,
    'relic_density': relic_density,
    'neutralino_mass': neutralino_LHC,
    'sneutrino_mass': sneutrino_LHC,
    'gluino_mass': Gluino_LHC,
    'Cha1_mass': Cha1_LHC,
    'Mzp_mass':MZp_LHC,
    'stau_mass': stau_LHC,
    'selectron_mass': selectron_LHC,
    'stop_mass':stop_LHC,
    'sbottom_mass': sbottom_LHC,
    'smuon_mass': smuon_LHC,
    'mu_value': mu_LHC,
    'muR_value': muR_LHC,
    'h1_mass': h1_LHC,
    'h2_mass': h2_LHC,
    'h3_mass': h3_LHC,
    'M1': M1_LHC,
    'M2': M2_LHC,
    'M3': M3_LHC,
    'M4': M4_LHC,
    'ZR': ZR_LHC
})
df.to_csv('sneutrino_LSP_LHC.csv')
"""

# Input file
m0=[]
m12=[]
A0=[]
signmuR=[]
tanbeta=[]
tanbetaR=[]
VR=[]
Ys=[]
Yv=[]

# Outputs
DD_SI=[]
relic_density=[]
Gluino_benchmark = []
Cha1_benchmark = []
MZp_benchmark = []
stau_benchmark = []
selectron_benchmark = []
stop_benchmark = []
sbottom_benchmark = []
smuon_benchmark = []
neutralino_benchmark = []
sneutrino_benchmark = []
mu_benchmark  = []
muR_benchmark  = []
h1_benchmark = []
h2_benchmark = []
h3_benchmark = []

M1_benchmark = []
M2_benchmark = []
M3_benchmark = []
M4_benchmark = []

ZR_BH = []

for j in range(0,n_runs1):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run/SPhenoOutputs'+str(j)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(j,file)
            content = pyslha.read(path + '/' + file)
        
            neutralino = abs(content.blocks["MASS"][1000022])
            sneutrino = abs(content.blocks["MASS"][1000012])
            lsp_condition = neutralino>sneutrino


            mh1 = content.blocks["MASS"][25]
            mh1_condition  = mh1>122 and mh1<128

            # Elicit file number
            p = os.popen("echo "+file+" | cut -d'.' -f4 ")
            number = p.read()
            p.close()
            file_num = number[0:len(number)-1]
            if lsp_condition and mh1_condition:
                try:
                    #relic and DD
                    p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                    number = p.read()
                    p.close()
                    relic = float(number[0:len(number)-1])
        	        	
                    p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                    number = p.read()
                    p.close()
                    DD = '%1.3e' %float(number[0:len(number)-1])
                except:
                    continue
                
                # relic and DD
                p = os.popen("awk '/Omega/ {print $3}' "+path+"/information_"+file_num+".txt"+" | cut -d'=' -f2")
                number = p.read()
                p.close()
                relic = float(number[0:len(number)-1])
       	        	
                p = os.popen("awk '/ proton/{print $3}' "+path+"/information_"+file_num+".txt")
                number = p.read()
                p.close()
                DD = '%1.3e' %float(number[0:len(number)-1])
                relic_density.append(relic)
                DD_SI.append(DD)
                
                # Input params
                m0.append(content.blocks["MINPAR"][1])
                m12.append(content.blocks["MINPAR"][2])
                A0.append(content.blocks["MINPAR"][5])
                signmuR.append(content.blocks["MINPAR"][6])
                tanbeta.append(content.blocks["MINPAR"][7])
                tanbetaR.append(content.blocks["MINPAR"][9])
                VR.append(content.blocks["MINPAR"][11])
                Ys.append(content.blocks["YS"][1,1])
                Yv.append(content.blocks["YV"][1,1])
                
                # Outputs
                Cha1_benchmark.append(content.blocks["MASS"][1000024])
                MZp_benchmark.append(content.blocks["MASS"][99])
                stau_benchmark.append(content.blocks["MASS"][1000015])
                selectron_benchmark.append(content.blocks["MASS"][1000011])
                stop_benchmark.append(content.blocks["MASS"][1000006])
                sbottom_benchmark.append(content.blocks["MASS"][1000005])
                smuon_benchmark.append(content.blocks["MASS"][1000013])
                neutralino_benchmark.append(neutralino)
                sneutrino_benchmark.append(sneutrino)
                Gluino_benchmark.append(content.blocks["MASS"][1000021])
                mu_benchmark.append(content.blocks['HMIX'][1])
                muR_benchmark.append(content.blocks['HMIX'][9])

                M1_benchmark.append(content.blocks['MSOFT'][1])
                M2_benchmark.append(content.blocks['MSOFT'][2])
                M3_benchmark.append(content.blocks['MSOFT'][3])
                M4_benchmark.append(content.blocks['MSOFT'][4])

                higgs = [content.blocks["MASS"][25],content.blocks["MASS"][35], content.blocks["MASS"][225]]
                higgs.sort()
                h1_benchmark.append(higgs[0])
                h2_benchmark.append(higgs[1])
                h3_benchmark.append(higgs[2])

                ZR_BH.append(content.blocks["MASS"][99])

df = pd.DataFrame({
    'm0': m0,
    'm12': m12,
    'A0': A0,
    'tanbeta': tanbeta,
    'tanbetaR': tanbetaR,
    'VR': VR,
    'signmuR': signmuR,
    'Ys': Ys,
    'Yv': Yv,
    'DD': DD_SI,
    'relic_density': relic_density,
    'neutralino_mass': neutralino_benchmark,
    'sneutrino_mass': sneutrino_benchmark,
    'gluino_mass': Gluino_benchmark,
    'Cha1_mass': Cha1_benchmark,
    'Mzp_mass':MZp_benchmark,
    'stau_mass': stau_benchmark,
    'selectron_mass': selectron_benchmark,
    'stop_mass':stop_benchmark,
    'sbottom_mass': sbottom_benchmark,
    'smuon_mass': smuon_benchmark,
    'mu_value': mu_benchmark,
    'muR_value': muR_benchmark,
    'h1_mass': h1_benchmark,
    'h2_mass': h2_benchmark,
    'h3_mass': h3_benchmark,
    'M1': M1_benchmark,
    'M2': M2_benchmark,
    'M3': M3_benchmark,
    'M4': M4_benchmark,
    'ZR': ZR_BH
})
df.to_csv('sneutrino_LSP_benchmark.csv')
