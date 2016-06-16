#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Facebook 1 1 10 15 deg >log/fdeg.log &
py recursive_noise_reduction.py Facebook 1 1 10 15 clo >log/fclo.log &
py recursive_noise_reduction.py Facebook 1 1 10 15 pr >log/fpr.log &
py recursive_noise_reduction.py Facebook 1 1 10 15 ci >log/fci.log &

wait
py recursive_noise_reduction.py Twitter-follow 1 5 10 15 deg >log/tfdeg.log &
py recursive_noise_reduction.py Twitter-follow 1 5 10 15 clo >log/tfclo.log &
py recursive_noise_reduction.py Twitter-follow 1 5 10 15 pr >log/tfpr.log &
py recursive_noise_reduction.py Twitter-follow 1 5 10 15 ci >log/tfci.log &

wait

py recursive_noise_reduction.py APS 1 1 10 15 deg >log/adeg.log &
py recursive_noise_reduction.py APS 1 1 10 15 clo >log/aclo.log &
py recursive_noise_reduction.py APS 1 1 10 15 pr >log/apr.log &
py recursive_noise_reduction.py APS 1 1 10 15 ci >log/aci.log &
wait
py recursive_noise_reduction.py Twitter-mention 1 1 10 15 deg >log/tmdeg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 10 15 clo >log/tmclo.log &
py recursive_noise_reduction.py Twitter-mention 1 1 10 15 pr >log/tmpr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 10 15 ci >log/tmci.log &
