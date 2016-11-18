#!/bin/bash -x

python3.4 recursive_noise_reduction.py APS 1 1 1 470 deg >log/apst1deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 1 470 pr >log/apst1pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 3 160 deg >log/apst3deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 3 160 pr >log/apst3pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 5 100 deg >log/apst5deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 5 100 pr >log/apst5pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 8 60 deg >log/apst8deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 8 60 pr >log/apst8pr.log &

wait

python3.4 recursive_noise_reduction.py APS 1 1 10 45 deg >log/apst10deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 10 45 pr >log/apst10pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 30 15 deg >log/apst30deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 30 15 pr >log/apst30pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 50 7 deg >log/apst50deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 50 7 pr >log/apst50pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 70 4 deg >log/apst70deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 70 4 pr >log/apst70pr.log &
python3.4 recursive_noise_reduction.py APS 1 1 90 3 deg >log/apst90deg.log &
python3.4 recursive_noise_reduction.py APS 1 1 90 3 pr >log/apst90pr.log &

wait
