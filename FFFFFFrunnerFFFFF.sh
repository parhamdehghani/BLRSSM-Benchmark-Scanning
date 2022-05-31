# !/bin/bash

for i in $(seq 1 16)
do
        cd Run_mic$i
	python3 micromegas_focused.py &
	cd ../
done
