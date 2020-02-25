#!/bin/bash

# 1 - must accept one arg
# 2 - have at least one conditional statement
# 3 - Provide the user with feedback on what it is doing (echo status to console	
# 4 - Be useful in some way

# stopwatch

read -p "Let The Race Begin! (click 'space' to start, stop = 's')" start

stop='s'
start_time=$(date +%s)
current_time=$(date +%s)
total_time=0

if [ start = ' ' ]
then
	while[ stop != 's' ]
	do
	current_time=$(date +%s)
	total_time=current_time-start_time
	echo $total_time
	done
	echo "The total time of the race was: " + $total_time
fi



