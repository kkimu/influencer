#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Twitter-follow 2 2 10 40 deg >log/tmn2t10deg.log &
py recursive_noise_reduction.py Twitter-follow 2 2 10 40 clo >log/tmn2t10clo.log &
py recursive_noise_reduction.py Twitter-follow 2 2 10 40 pr >log/tmn2t10pr.log &
py recursive_noise_reduction.py Twitter-follow 2 2 10 40 ci >log/tmn2t10ci.log &
py recursive_noise_reduction.py Twitter-follow 3 3 10 40 deg >log/tmn3t10deg.log &
py recursive_noise_reduction.py Twitter-follow 3 3 10 40 clo >log/tmn3t10clo.log &
py recursive_noise_reduction.py Twitter-follow 3 3 10 40 pr >log/tmn3t10pr.log &
py recursive_noise_reduction.py Twitter-follow 3 3 10 40 ci >log/tmn3t10ci.log &

wait

py recursive_noise_reduction.py Twitter-follow 4 4 10 40 deg >log/tmn4t10deg.log &
py recursive_noise_reduction.py Twitter-follow 4 4 10 40 clo >log/tmn4t10clo.log &
py recursive_noise_reduction.py Twitter-follow 4 4 10 40 pr >log/tmn4t10pr.log &
py recursive_noise_reduction.py Twitter-follow 4 4 10 40 ci >log/tmn4t10ci.log &
py recursive_noise_reduction.py Twitter-follow 5 5 10 40 deg >log/tmn5t10deg.log &
py recursive_noise_reduction.py Twitter-follow 5 5 10 40 clo >log/tmn5t10clo.log &
py recursive_noise_reduction.py Twitter-follow 5 5 10 40 pr >log/tmn5t10pr.log &
py recursive_noise_reduction.py Twitter-follow 5 5 10 40 ci >log/tmn5t10ci.log &

wait

py recursive_noise_reduction.py Twitter-follow 2 2 30 15 deg >log/tmn2t30deg.log &
py recursive_noise_reduction.py Twitter-follow 2 2 30 15 clo >log/tmn2t30clo.log &
py recursive_noise_reduction.py Twitter-follow 2 2 30 15 pr >log/tmn2t30pr.log &
py recursive_noise_reduction.py Twitter-follow 2 2 30 15 ci >log/tmn2t30ci.log &
py recursive_noise_reduction.py Twitter-follow 3 3 30 15 deg >log/tmn3t30deg.log &
py recursive_noise_reduction.py Twitter-follow 3 3 30 15 clo >log/tmn3t30clo.log &
py recursive_noise_reduction.py Twitter-follow 3 3 30 15 pr >log/tmn3t30pr.log &
py recursive_noise_reduction.py Twitter-follow 3 3 30 15 ci >log/tmn3t30ci.log &

wait

py recursive_noise_reduction.py Twitter-follow 4 4 30 15 deg >log/tmn4t30deg.log &
py recursive_noise_reduction.py Twitter-follow 4 4 30 15 clo >log/tmn4t30clo.log &
py recursive_noise_reduction.py Twitter-follow 4 4 30 15 pr >log/tmn4t30pr.log &
py recursive_noise_reduction.py Twitter-follow 4 4 30 15 ci >log/tmn4t30ci.log &
py recursive_noise_reduction.py Twitter-follow 5 5 30 15 deg >log/tmn5t30deg.log &
py recursive_noise_reduction.py Twitter-follow 5 5 30 15 clo >log/tmn5t30clo.log &
py recursive_noise_reduction.py Twitter-follow 5 5 30 15 pr >log/tmn5t30pr.log &
py recursive_noise_reduction.py Twitter-follow 5 5 30 15 ci >log/tmn5t30ci.log &


