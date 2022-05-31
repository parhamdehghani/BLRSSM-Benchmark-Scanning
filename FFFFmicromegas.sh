#!/bin/bash
for file in $(echo SP*)
do
	echo $file
	cd $file
	rm -f inform*
	#cp -r /home/Universe/Softwares/micromegas_5.2.7.a/BLRISS/* .
	for file1 in $(echo SP*w.*)
	do
		echo $file1
		IFS="."
		read -a strarr <<< "$file1"
		num=`echo ${strarr[3]}`
		IFS=" "
		cp $file1 SPheno.spc.BLRinvSeesaw
		CalcOmega_with_DDetection_MOv5 SPheno.spc.BLRinvSeesaw > information_$num.txt 
		rm -f SPheno.spc.BLRinvSeesaw
	done
	cd ..
done


