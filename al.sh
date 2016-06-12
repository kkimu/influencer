#!/bin/bash
for i in `seq 1 100`
do
    python3.4 adjacency_list.py Twitter-follow/data/link_${i}.txt Twitter-follow/data/link_${i}.adjacencylist
done
