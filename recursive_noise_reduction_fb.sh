#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Facebook 1 1 10 40 deg >log/f10deg.log &
py recursive_noise_reduction.py Facebook 1 1 10 40 clo >log/f10clo.log &
py recursive_noise_reduction.py Facebook 1 1 10 40 pr >log/f10pr.log &
py recursive_noise_reduction.py Facebook 1 1 10 40 ci >log/f10ci.log &

py recursive_noise_reduction.py Facebook 1 1 30 15 deg >log/f30deg.log &
py recursive_noise_reduction.py Facebook 1 1 30 15 clo >log/f30clo.log &
py recursive_noise_reduction.py Facebook 1 1 30 15 pr >log/f30pr.log &
py recursive_noise_reduction.py Facebook 1 1 30 15 ci >log/f30ci.log &

wait

py recursive_noise_reduction.py Facebook 1 1 50 7 deg >log/f50deg.log &
py recursive_noise_reduction.py Facebook 1 1 50 7 clo >log/f50clo.log &
py recursive_noise_reduction.py Facebook 1 1 50 7 pr >log/f50pr.log &
py recursive_noise_reduction.py Facebook 1 1 50 7 ci >log/f50ci.log &

py recursive_noise_reduction.py Facebook 1 1 80 3 deg >log/f80deg.log &
py recursive_noise_reduction.py Facebook 1 1 80 3 clo >log/f80clo.log &
py recursive_noise_reduction.py Facebook 1 1 80 3 pr >log/f80pr.log &
py recursive_noise_reduction.py Facebook 1 1 80 3 ci >log/f80ci.log &

#wait

#py recursive_noise_reduction.py Twitter-follow 1 5 10 15 deg >log/tf10deg.log &
#py recursive_noise_reduction.py Twitter-follow 1 5 10 15 clo >log/tf10clo.log &
#py recursive_noise_reduction.py Twitter-follow 1 5 10 15 pr >log/tf10pr.log &
#py recursive_noise_reduction.py Twitter-follow 1 5 10 15 ci >log/tf10ci.log &

#wait

#py recursive_noise_reduction.py APS 1 1 10 15 deg >log/adeg.log &
#py recursive_noise_reduction.py APS 1 1 10 15 clo >log/aclo.log &
#py recursive_noise_reduction.py APS 1 1 10 15 pr >log/apr.log &
#py recursive_noise_reduction.py APS 1 1 10 15 ci >log/aci.log &

#py recursive_noise_reduction.py Twitter-mention 1 1 10 15 deg >log/tmdeg.log &
#py recursive_noise_reduction.py Twitter-mention 1 1 10 15 clo >log/tmclo.log &
#py recursive_noise_reduction.py Twitter-mention 1 1 10 15 pr >log/tmpr.log &
#py recursive_noise_reduction.py Twitter-mention 1 1 10 15 ci >log/tmci.log &
