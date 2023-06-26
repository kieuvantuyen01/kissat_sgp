#!/usr/bin/bash
# ls input/binomial/cnf_noALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 --relaxed | ./process.py > output/binomial/noALO.txt
ls input_v3/binary/cnf_noALO_v3/*.cnf | xargs -n 1 ./build/kissat --time=1800 | ./process.py > output_v3/binary/noALO.txt