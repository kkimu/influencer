#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Twitter-follow 1 3 10 20 &
py recursive_noise_reduction.py Twitter-follow 4 6 10 20 &
py recursive_noise_reduction.py Twitter-follow 7 10 10 20 &
py recursive_noise_reduction.py Facebook 1 3 10 20 &
py recursive_noise_reduction.py Facebook 4 6 10 20 &
py recursive_noise_reduction.py Facebook 7 10 10 20 &

wait

py recursive_noise_reduction.py Twitter-mention 1 2 10 20 &
py recursive_noise_reduction.py Twitter-mention 3 4 10 20 &
py recursive_noise_reduction.py Twitter-mention 5 6 10 20 &
py recursive_noise_reduction.py Twitter-mention 7 8 10 20 &
py recursive_noise_reduction.py Twitter-mention 9 10 10 20 &
py recursive_noise_reduction.py APS 1 2 10 20 &
py recursive_noise_reduction.py APS 3 4 10 20 &
py recursive_noise_reduction.py APS 5 6 10 20 &
py recursive_noise_reduction.py APS 7 8 10 20 &
py recursive_noise_reduction.py APS 9 10 10 20 &
