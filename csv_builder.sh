#!/bin/bash

echo ,m0,m12,A0,VR,TanBeta,TanBetaR,YvDIG,YsDIG,SignumMu,MuR,relic density,sneutrino mass,neutralino mass,DD_SI,DD_SD_p,DD_SD_n,relic_boolean > chosen.csv

for i in $(seq 1 16)
do
	awk 'FS=","{print}' Run*$i/micrOMEGAS.csv >> chosen.csv
done

cat chosen.csv |wc -l

