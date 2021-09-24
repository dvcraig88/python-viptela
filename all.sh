#! /bin/sh
#Define vmanage and password
read -p 'vmanage ip address: ' VMANAGE_HOST
read -p 'Username: ' VMANAGE_USERNAME
read -p 'password: ' VMANAGE_PASSWORD

read -p 'What is the system ip: ' system_ip

vmanage show route table $system_ip
vmanage show interface list $system_ip
vmanage show control connections $system_ip


