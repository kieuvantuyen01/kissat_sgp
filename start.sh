#!/usr/bin/bash
ls input/binary/cnf_noALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 --relaxed | ./process.py > output/binary/noALO.txt
