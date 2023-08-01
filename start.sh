#!/usr/bin/bash
# ls input/binomial/cnf_noALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 --relaxed | ./process.py > output/binomial/noALO.txt
# run with cnf_ALO_v3 in input_v3
# ls input_v3/binary/cnf_ALO_v3/*.cnf | xargs -n 1 ./build/kissat --time=1800 | ./process.py > output_v3/binary/ALO.txt
# run with cnf_ALO_v4 with input_v4 and output_v4, output filename is ALO + Datetime + .txt (timeout 900s)
ls input_v4/binary/cnf_ALO_v4/*.cnf | xargs -n 1 ./build/kissat --time=900 | ./process.py > output_v4/binary/ALO_$(date +%Y%m%d_%H%M%S).txt