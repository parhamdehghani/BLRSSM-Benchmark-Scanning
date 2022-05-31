#!/bin/bash
Total_SLHA=0
for i in $(seq 1 1000)
do
	# for watching the number of solutions
	echo 'for watching the number of solutions'
	for file in $(echo Run*) 
	do  
		echo $file
		a=`ls $file/SPhenoOutputs | grep Micro* |wc -l`
		echo "$a"
	       	((Total_SLHA += a)) 
       	done
	# for watching the benchmarks
	echo "Total solutions are $Total_SLHA"
	Total_SLHA=0
	echo ------------
	echo 'for watching the benchmarks'
	#for file in $(echo Run*); do  echo $file; ls $file/SPhenoOutputs | grep Micro* ; done
	echo --------------------------------------------------------------------------------
sleep 10s
done
