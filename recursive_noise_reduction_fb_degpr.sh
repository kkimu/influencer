#!/bin/bash -x

python3.4 recursive_noise_reduction.py Facebook 1 1 1 470 deg >log/fbt1deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 1 470 pr >log/fbt1pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 3 160 deg >log/fbt3deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 3 160 pr >log/fbt3pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 5 100 deg >log/fbt5deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 5 100 pr >log/fbt5pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 8 60 deg >log/fbt8deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 8 60 pr >log/fbt8pr.log &

wait

python3.4 recursive_noise_reduction.py Facebook 1 1 10 45 deg >log/fbt10deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 10 45 pr >log/fbt10pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 30 15 deg >log/fbt30deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 30 15 pr >log/fbt30pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 50 7 deg >log/fbt50deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 50 7 pr >log/fbt50pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 70 4 deg >log/fbt70deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 70 4 pr >log/fbt70pr.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 90 3 deg >log/fbt90deg.log &
python3.4 recursive_noise_reduction.py Facebook 1 1 90 3 pr >log/fbt90pr.log &

wait
