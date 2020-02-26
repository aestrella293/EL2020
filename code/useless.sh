#!/bin/bash

# 1 - must accept one arg
# 2 - have at least one conditional statement
# 3 - Provide the user with feedback on what it is doing (echo status to console
# 4 - Be useful in some way

# stopwatch

read -p "Let Time Begin! (Press 'Enter' to start to start the 'Stopwatch'!)" start

stop=0

echo  "Start! Press 'Enter' to stop the Stopwatch" 
start_time=0

current_time=0

total_time=0

if  [ $stop != "" ]
then
	while [ $stop != "" ]
	do
		sleep 1
		let current_time++
		echo $current_time
		if [ $stop == " " ]
		then
			break
		fi
	done
fi
echo "The total time of the race was: " + $total_time




