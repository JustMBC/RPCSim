#!/bin/bash

let "i=0"
let "hv=51"

while [ $i -lt 3 ]
do
	time ./sim --config ./config/calice_copy.xml --e $hv
	let "hv += 1"
	let "i += 1"
done 
	
