#!/bin/bash
rm -rf Run_mic*
for i in $(seq 1 16)
do
	mkdir Run_mic$i
	mkdir Run_mic$i/SPhenoOutputs
	cp micromegas_focused.py LesHouches.in.BLRinvSeesaw_init MyPySLHA.py chosen.csv Run_mic$i
done


