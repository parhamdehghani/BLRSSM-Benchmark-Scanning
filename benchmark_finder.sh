#!/bin/bash

for i in $(seq 1 50)
do
	for file in $(echo SP*$i)
	do
		for file1 in $file/SP*
		do
			awk '/# MuR/{print $2}' $file1 > new.txt
			MuR=`awk 'NR==1{print}' new.txt`
			if [[ $MuR == "8.36098048E+02" ]]
			then
				echo $MuR
				realpath $file1 > address.txt
			fi
		done

	done

done
rm new.txt

