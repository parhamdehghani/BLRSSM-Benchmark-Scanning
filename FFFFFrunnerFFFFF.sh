# !/bin/bash

for i in $(seq 1 16)
do
        cd Run$i
	python3 base_run.py &
	cd ../
done
