#!/bin/sh
dataset=("Facebook" "Twitter-mention" "APS")


#R --vanilla --slave --args Twitter-mention/data/link.edgelist analysis/Twitter-mention_ True < 100per_deg_clo_bet_pr.R &

R --vanilla --slave --args Facebook/data/link.edgelist analysis/Facebook_ False < 100per_deg_clo_bet_pr.R &
R --vanilla --slave --args APS/data/link.edgelist analysis/APS_ False < 100per_deg_clo_bet_pr.R &
R --vanilla --slave --args Twitter-follow/data/link_1.edgelist analysis/Twitter-follow_1_ True < 100per_deg_clo_bet_pr.R &
