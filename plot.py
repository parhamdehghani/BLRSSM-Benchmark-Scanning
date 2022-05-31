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
#sys.path.append("/home/sberam/Documents/pyslha-3.2.5")
#sys.path.append("/home/sberam/Documents/xSLHA-master")
import pyslha
import xslha
rcParams['figure.figsize'] = 10, 10
#plt.rcParams['text.usetex'] = True
sb.set_style('whitegrid')

labels = ['Neutralino LSP (All constraints without relic)', 'Sneutrino LSP (All constraints without relic)' , 'Neutralino LSP (All constraints with relic)', 'Sneutrino LSP (All constraints with relic)']

def abline(slope, intercept, color):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--', c=color)

#data = pd.read_csv('Master.csv')
#data = data[data['sneutrino mass']>0]
#data = data[data['neutralino mass']>0]
#data_benchmark = data[data['relic_boolean']==True]
#data_benchmark_neutralino = data_benchmark[abs(data_benchmark['neutralino mass'])<abs(data_benchmark['sneutrino mass'])]
#data_benchmark_sneutrino = data_benchmark[abs(data_benchmark['neutralino mass'])>abs(data_benchmark['sneutrino mass'])]
#data_LHC = data[data['relic_boolean']== False]
#data_LHC_neutralino = data_LHC[abs(data_LHC['neutralino mass'])<abs(data_LHC['sneutrino mass'])]
#data_LHC_sneutrino = data_LHC[abs(data_LHC['neutralino mass'])>abs(data_LHC['sneutrino mass'])]

#neutralino_LSP_LHC = data_LHC[data_LHC['sneutrino mass']>data_LHC['neutralino mass']]
#neutralino_LSP_BM = data_benchmark[data_benchmark['sneutrino mass']>data_benchmark['neutralino mass']]
#sneutrino_LSP_LHC = data_LHC[data_LHC['sneutrino mass']<data_LHC['neutralino mass']]
#sneutrino_LSP_BM = data_benchmark[data_benchmark['sneutrino mass']<data_benchmark['neutralino mass']]

neutralino_LSP_LHC = pd.read_csv('neutralino_LSP_LHC.csv')
neutralino_LSP_BM = pd.read_csv('neutralino_LSP_benchmark.csv')
sneutrino_LSP_LHC = pd.read_csv('sneutrino_LSP_LHC.csv')
sneutrino_LSP_BM = pd.read_csv('sneutrino_LSP_benchmark.csv')


plt.scatter(neutralino_LSP_LHC['m12'], neutralino_LSP_LHC['m0'], edgecolor="black", lw=.5, color='b',s=10)
plt.scatter(sneutrino_LSP_LHC['m12'], sneutrino_LSP_LHC['m0'], edgecolor="black", lw=.5, color='b',s=10)
plt.scatter(neutralino_LSP_BM['m12'], neutralino_LSP_BM['m0'], color='r',s=50,edgecolor="black", lw=.5, label = 'Neutralino LSP (All constraints with relic)')
plt.scatter(sneutrino_LSP_BM['m12'], sneutrino_LSP_BM['m0'], color='g',s=50,edgecolor="black", lw=.5, label = 'Sneutrino LSP (All constraints with relic)')
plt.xlabel(r'$M_{1/2} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{0} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('m0-m12.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['A0']/neutralino_LSP_LHC['m0'], neutralino_LSP_LHC['m0'], edgecolor="black", lw=.5,color='b',s=10)
plt.scatter(sneutrino_LSP_LHC['A0']/sneutrino_LSP_LHC['m0'], sneutrino_LSP_LHC['m0'], edgecolor="black", lw=.5,color='b',s=10)
plt.scatter(neutralino_LSP_BM['A0']/neutralino_LSP_BM['m0'], neutralino_LSP_BM['m0'], color='r',s=50,edgecolor="black", lw=.5, label = 'Neutralino LSP (All constraints with relic)')
plt.scatter(sneutrino_LSP_BM['A0']/sneutrino_LSP_BM['m0'], sneutrino_LSP_BM['m0'], color='g',s=50,edgecolor="black", lw=.5, label = 'Sneutrino LSP (All constraints with relic)')
plt.xlabel(r'$A_0/m_0$', fontsize=20)
plt.ylabel(r'$m_{0} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('m0-A0.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['tanbeta'], neutralino_LSP_LHC['m12'], color='b',edgecolor="black", lw=.5,s=10)
plt.scatter(sneutrino_LSP_LHC['tanbeta'], sneutrino_LSP_LHC['m12'], color='b',edgecolor="black", lw=.5,s=10)
plt.scatter(neutralino_LSP_BM['tanbeta'], neutralino_LSP_BM['m12'], color='r',s=50,edgecolor="black", lw=.5, label = 'Neutralino LSP (All constraints with relic)')
plt.scatter(sneutrino_LSP_BM['tanbeta'], sneutrino_LSP_BM['m12'], color='g',s=50,edgecolor="black", lw=.5, label = 'Sneutrino LSP (All constraints with relic)')
plt.xlabel(r'$tan\beta$', fontsize=20)
plt.ylabel(r'$M_{1/2} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('m12-tanbeta.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['stop_mass'], color='b',edgecolor="black", lw=.5,s=10, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['stop_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['stop_mass'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['stop_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])

abline(1,0, 'y')

plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{\tilde{t}_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('stop-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['sbottom_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['sbottom_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1] )
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['sbottom_mass'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['sbottom_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0, 'y')
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{\tilde{b}_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('sbottom-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['Cha1_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['Cha1_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1] )
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['Cha1_mass'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['Cha1_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0, 'y')
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{\tilde{\chi}_1^\pm} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('cha1-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['stau_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['stau_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['stau_mass'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['stau_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0, 'y')
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{\tilde{\tau}_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('stau-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['sneutrino_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['sneutrino_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['sneutrino_mass'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['sneutrino_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0, 'y')
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{\tilde{\nu}_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('sneutrino-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['M4']/neutralino_LSP_LHC['M1'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['M4']/sneutrino_LSP_LHC['M1'], color='cyan',s=10,edgecolor="black", lw=.5, label = labels[1] )
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['M4']/neutralino_LSP_BM['M1'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['M4']/sneutrino_LSP_BM['M1'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$M_4/M_1$', fontsize=20)
plt.legend()
plt.savefig('M4_M1-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['M1']/neutralino_LSP_LHC['mu_value'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['M1']/sneutrino_LSP_LHC['mu_value'], color='cyan',s=10,edgecolor="black", lw=.5, label = labels[1] )
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['M1']/neutralino_LSP_BM['mu_value'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['M1']/sneutrino_LSP_BM['mu_value'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$M_1/\mu$', fontsize=20)
plt.legend()
plt.savefig('M1_mu-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['M2']/neutralino_LSP_LHC['mu_value'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['neutralino_mass'], sneutrino_LSP_LHC['M2']/sneutrino_LSP_LHC['mu_value'], color='cyan',s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['M2']/neutralino_LSP_BM['mu_value'], color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['neutralino_mass'], sneutrino_LSP_BM['M2']/sneutrino_LSP_BM['mu_value'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$M_2/\mu$', fontsize=20)
plt.legend()
plt.savefig('M2_mu-neutralino.png')
plt.close()

plt.plot(abs(neutralino_LSP_LHC['neutralino_mass']), neutralino_LSP_LHC['relic_density'], '.', ms = 10,mec="black", color='b', label = labels[0])
plt.plot(abs(sneutrino_LSP_LHC['sneutrino_mass']), sneutrino_LSP_LHC['relic_density'], '.',  ms = 10,color='cyan',mec="black", label = labels[1])
plt.plot(abs(neutralino_LSP_BM['neutralino_mass']), neutralino_LSP_BM['relic_density'], '.', ms = 8,mec = "black", color='r', label = labels[2])
plt.axhline(y=0.09, color='y', linestyle='-')
plt.axhline(y=0.14, color='y', linestyle='-')
plt.ylabel(r'$\Omega_{DM}h^2$', fontsize=20)
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.yscale('log')
plt.savefig('relic-neutralino.png')
plt.close()

plt.plot(abs(neutralino_LSP_LHC['sneutrino_mass']), neutralino_LSP_LHC['relic_density'], '.', ms = 10, color='b',mec="black", label = labels[0])
plt.plot(abs(sneutrino_LSP_LHC['sneutrino_mass']), sneutrino_LSP_LHC['relic_density'], '.',  ms = 10,color='cyan',mec="black", label = labels[1])
plt.plot(abs(sneutrino_LSP_BM['sneutrino_mass']), sneutrino_LSP_BM['relic_density'],'.',  ms = 8,mec = "black",color='g', label = labels[3])
plt.axhline(y=0.09, color='y', linestyle='-')
plt.axhline(y=0.14, color='y', linestyle='-')
plt.ylabel(r'$\Omega_{DM}h^2$', fontsize=20)
plt.xlabel(r'$m_{\tilde{\nu}_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.yscale('log')
plt.savefig('relic-sneutrino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['mu_value'], neutralino_LSP_LHC['muR_value'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['mu_value'], sneutrino_LSP_LHC['muR_value'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['mu_value'], neutralino_LSP_BM['muR_value'],  color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['mu_value'], sneutrino_LSP_BM['muR_value'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
plt.xlabel(r'$\mu \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$\mu_R \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('muR-mu.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['h1_mass'], neutralino_LSP_LHC['h3_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['h1_mass'], sneutrino_LSP_LHC['h3_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['h1_mass'], neutralino_LSP_BM['h3_mass'],  color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['h1_mass'], sneutrino_LSP_BM['h3_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0,'y')
plt.xlabel(r'$m_{h_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{h_3} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('mh3-mh1.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['h1_mass'], neutralino_LSP_LHC['h2_mass'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['h1_mass'], sneutrino_LSP_LHC['h2_mass'], color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['h1_mass'], neutralino_LSP_BM['h2_mass'],  color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['h1_mass'], sneutrino_LSP_BM['h2_mass'], color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
abline(1,0,'y')
plt.xlabel(r'$m_{h_1} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$m_{h_2} \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('mh2-mh1.png')
plt.close()


plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['VR'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['VR'],  color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$VR \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('VR-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['neutralino_mass'], neutralino_LSP_LHC['ZR'], color='b',s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(neutralino_LSP_BM['neutralino_mass'], neutralino_LSP_BM['ZR'],  color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.xlabel(r'$m_{\tilde{\chi}_1^0} \,[\mathrm{GeV}]$', fontsize=20)
plt.ylabel(r'$ZR \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('ZR-neutralino.png')
plt.close()

plt.scatter(neutralino_LSP_LHC['tanbeta'], neutralino_LSP_LHC['M1'] , color='b', s=10,edgecolor="black", lw=.5, label = labels[0])
plt.scatter(sneutrino_LSP_LHC['tanbeta'], sneutrino_LSP_LHC['M1'] , color='cyan', s=10,edgecolor="black", lw=.5, label = labels[1])
plt.scatter(neutralino_LSP_BM['tanbeta'], neutralino_LSP_BM['M1'] , color='r',s=50,edgecolor="black", lw=.5, label = labels[2])
plt.scatter(sneutrino_LSP_BM['tanbeta'], sneutrino_LSP_BM['M1'] , color='g',s=50,edgecolor="black", lw=.5, label = labels[3])
plt.xlabel(r'$Tan \beta$', fontsize=20)
plt.ylabel(r'$M_1 \,[\mathrm{GeV}]$', fontsize=20)
plt.legend()
plt.savefig('M1-tanbeta.png')
plt.close()

