#!/usr/bin/bash
ls input/binary/cnf_ALO/*.cnf | xargs -n 1 ./build/kissat --time=1800 --relaxed | ./process.py > output/binary/ALO.txt