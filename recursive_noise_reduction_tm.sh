#!/bin/bash -x
alias py='python3.4'
shopt -s expand_aliases

py recursive_noise_reduction.py Twitter-mention 1 1 1 220 deg >log/tmt1deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 1 220 pr >log/tmt1pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 3 150 deg >log/tmt3deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 3 150 pr >log/tmt3pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 5 90 deg >log/tmt5deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 5 90 pr >log/tmt5pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 8 55 deg >log/tmt8deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 8 55 pr >log/tmt8pr.log &

wait

py recursive_noise_reduction.py Twitter-mention 1 1 10 40 deg >log/tmt10deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 10 40 pr >log/tmt10pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 30 15 deg >log/tmt30deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 30 15 pr >log/tmt30pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 50 6 deg >log/tmt50deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 50 6 pr >log/tmt50pr.log &
py recursive_noise_reduction.py Twitter-mention 1 1 80 3 deg >log/tmt80deg.log &
py recursive_noise_reduction.py Twitter-mention 1 1 80 3 pr >log/tmt80pr.log &



