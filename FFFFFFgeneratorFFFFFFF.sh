#!/bin/bash
rm -rf Run*
for i in $(seq 1 16)
do
	mkdir Run$i
	mkdir Run$i/SPhenoOutputs
	cp base_run.py LesHouches.in.BLRinvSeesaw MyPySLHA.py Run$i
done


