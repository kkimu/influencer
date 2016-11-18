#!/bin/bash -x

python3.4 recursive_noise_reduction.py Twitter-follow 1 1 1 470 deg >log/tft1deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 1 470 pr >log/tft1pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 3 160 deg >log/tft3deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 3 160 pr >log/tft3pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 5 100 deg >log/tft5deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 5 100 pr >log/tft5pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 8 60 deg >log/tft8deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 8 60 pr >log/tft8pr.log &

wait

python3.4 recursive_noise_reduction.py Twitter-follow 1 1 10 45 deg >log/tft10deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 10 45 pr >log/tft10pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 30 15 deg >log/tft30deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 30 15 pr >log/tft30pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 50 7 deg >log/tft50deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 50 7 pr >log/tft50pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 70 4 deg >log/tft70deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 70 4 pr >log/tft70pr.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 90 3 deg >log/tft90deg.log &
python3.4 recursive_noise_reduction.py Twitter-follow 1 1 90 3 pr >log/tft90pr.log &

wait
