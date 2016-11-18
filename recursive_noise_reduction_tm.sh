#!/bin/bash -x

python3.4 recursive_noise_reduction.py Twitter-mention 1 1 1 470 deg >log/tmt1deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 1 470 pr >log/tmt1pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 3 160 deg >log/tmt3deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 3 160 pr >log/tmt3pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 5 100 deg >log/tmt5deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 5 100 pr >log/tmt5pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 8 60 deg >log/tmt8deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 8 60 pr >log/tmt8pr.log &

wait

python3.4 recursive_noise_reduction.py Twitter-mention 1 1 10 45 deg >log/tmt10deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 10 45 pr >log/tmt10pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 30 15 deg >log/tmt30deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 30 15 pr >log/tmt30pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 50 7 deg >log/tmt50deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 50 7 pr >log/tmt50pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 70 4 deg >log/tmt70deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 70 4 pr >log/tmt70pr.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 90 3 deg >log/tmt90deg.log &
python3.4 recursive_noise_reduction.py Twitter-mention 1 1 90 3 pr >log/tmt90pr.log &

wait
