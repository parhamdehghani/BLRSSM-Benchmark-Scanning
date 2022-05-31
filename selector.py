#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:01:06 2022

@author: Universe
"""

import pyslha
import numpy as np
import xslha
import os
import sys

with open("address.txt","w") as text:
     text.write('')
     text.close()

#n_runs = len(os.listdir('/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run'))

for j in range(1,51):
    path = '/home/Universe/Research/BLRSSM/Cluster_run/Secondary_run/SPhenoOutputs'+str(j)
    files = os.listdir(path)
    for file in files:
        if file[0]=='S':
            print(path+'/'+file)
            content = pyslha.read(path + '/' + file)
            binoBL = abs(content.blocks['NMIX'][1,1])
            binoR = abs(content.blocks['NMIX'][1,5])
            
            wino = abs(content.blocks['NMIX'][1,2])
            higgsinoU = abs(content.blocks['NMIX'][1,3])
            higgsinoD = abs(content.blocks['NMIX'][1,4])
            higgsinoR = abs(content.blocks['NMIX'][1,6])
            higgsinoRbar = abs(content.blocks['NMIX'][1,7])
            
            neutralino = abs(content.blocks['MASS'][1000022])
            slepton = abs(content.blocks['MASS'][1000011])
            
            
            condition1 = binoBL < wino or binoBL < higgsinoU or binoBL < higgsinoD or binoBL < higgsinoR or binoBL < higgsinoRbar or binoR < wino or binoR < higgsinoU or binoR < higgsinoD or binoR < higgsinoR or binoR < higgsinoRbar
            condition2 = neutralino<slepton
            if (condition1 and condition2):
                with open("address.txt","a") as text:
                    text.write(path+'/'+file+'\n')
                    text.close()
                    

