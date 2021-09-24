#!/bin/bash
#Activate python environment

log=/home/dcraig/python-viptela/failover.log
exec &> >(tee -a "$log")

source /home/dcraig/python-viptela/env/bin/activate

#Define vmanage and password
read -p 'vmanage ip address: ' VMANAGE_HOST
read -p 'username: ' VMANAGE_USERNAME
read -sp 'password: ' VMANAGE_PASSWORD

read -p 'What is the site name: ' site

echo -----------------------------------------------------
echo $site-LAB1-VRT1-LAB
echo -----------------------------------------------------
vmanage show omp summary $site-LAB1-VRT1-LAB
vmanage show interface list $site-LAB1-VRT1-LAB
vmanage show control connections $site-LAB1-VRT1-LAB

echo ------------------------------------------------------
echo $site-LAB1-VRT2-LAB
echo ------------------------------------------------------
vmanage show omp summary $site-LAB1-VRT2-LAB
vmanage show interface list $site-LAB1-VRT2-LAB
vmanage show control connections $site-LAB1-VRT2-LAB
