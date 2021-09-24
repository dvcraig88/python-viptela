#!/usr/bin/expect -f

set Username "e9f7m7v"
set Password "Dcbd@y1011"
set site "DEC1"


spawn ssh $Username@$site-MDFA1-ASW1.uson-net.mckesson.com
expect "*assword: "
send "$Password\r"
expect ">"

