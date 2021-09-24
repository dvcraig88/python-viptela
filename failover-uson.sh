#!/bin/bash
#Activate python environment

source /home/dcraig/python-viptela/env/bin/activate

#Define vmanage and password
export VMANAGE_HOST=int1-uson-vmanage1
read -p 'username: ' VMANAGE_USERNAME
read -sp 'password: ' VMANAGE_PASSWORD

export VMANAGE_USERNAME
export VMANAGE_PASSWORD

read -p 'What is the site name: ' site

curr_dt=$(date +%m-%d-%Y)
log=/home/dcraig/python-viptela/logs/failover-$site-$curr_dt.log
exec &> >(tee -a "$log")

echo -----------------------------------------------------
echo $site-MDFA-VRT1
echo -----------------------------------------------------
vmanage show omp summary $site-MDFA1-VRT1
vmanage show interface list $site-MDFA1-VRT1
vmanage show control connections $site-MDFA1-VRT1

echo ------------------------------------------------------
echo $site-MDFA1-VRT2
echo ------------------------------------------------------
vmanage show omp summary $site-MDFA1-VRT2
vmanage show interface list $site-MDFA1-VRT2
vmanage show control connections $site-MDFA1-VRT2

#ssh $VMANAGE_USERNAME@$site-MDFA1-ASW1

