#!/usr/bin/bash
# ls input/binomial/cnf_noALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 --relaxed | ./process.py > output/binomial/noALO.txt
ls input/binomial/cnf_ALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 | ./process.py > output_v3/binomial/ALO.txt