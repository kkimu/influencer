#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Twitter-follow 1 1 1 470 deg >log/tmn1t1deg.log &
py recursive_noise_reduction.py Twitter-follow 1 1 1 470 clo >log/tmn1t1clo.log &
py recursive_noise_reduction.py Twitter-follow 1 1 1 470 pr >log/tmn1t1pr.log &
py recursive_noise_reduction.py Twitter-follow 1 1 1 470 ci >log/tmn1t1ci.log &
py recursive_noise_reduction.py Twitter-follow 1 1 3 160 deg >log/tmn1t3deg.log &
py recursive_noise_reduction.py Twitter-follow 1 1 3 160 clo >log/tmn1t3clo.log &
py recursive_noise_reduction.py Twitter-follow 1 1 3 160 pr >log/tmn1t3pr.log &
py recursive_noise_reduction.py Twitter-follow 1 1 3 160 ci >log/tmn1t3ci.log &

wait

py recursive_noise_reduction.py Twitter-follow 1 1 5 100 deg >log/tmn1t5deg.log &
py recursive_noise_reduction.py Twitter-follow 1 1 5 100 clo >log/tmn1t5clo.log &
py recursive_noise_reduction.py Twitter-follow 1 1 5 100 pr >log/tmn1t5pr.log &
py recursive_noise_reduction.py Twitter-follow 1 1 5 100 ci >log/tmn1t5ci.log &
py recursive_noise_reduction.py Twitter-follow 1 1 8 60 deg >log/tmn1t8deg.log &
py recursive_noise_reduction.py Twitter-follow 1 1 8 60 clo >log/tmn1t8clo.log &
py recursive_noise_reduction.py Twitter-follow 1 1 8 60 pr >log/tmn1t8pr.log &
py recursive_noise_reduction.py Twitter-follow 1 1 8 60 ci >log/tmn1t8ci.log &

