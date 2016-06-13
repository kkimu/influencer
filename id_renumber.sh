#!/bin/bash
for i in `seq 1 100`
do
    python3.4 id_renumber.py Twitter-follow/data/link_${i}.txt Twitter-follow/data/diffusion_result_${i}.txt
done
