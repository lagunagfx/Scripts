#!/usr/bin/env bash

# Description : an abbreviated form for uptime, suitable for tmux status bar
#
# written by Jorge Barrientos AKA LagunaGFX

extract() {
	local word="$1"

	if [ ! -z "$word" ];
	then
		local uptime="$( uptime --pretty | sed 's/up //' | grep "$word" | awk -F " $word" '{print $1}' | rev | cut -d " " -f1 | rev )"
		if [ ! -z "$uptime" ];
		then
			local suffix=
			printf "%s%s" $uptime $( echo "$word" | cut -b1 )
	 		if [ "$word" != "minute" ];
			then
				printf " "
			fi
		fi
	fi
}

main() {
	extract year
	extract month
	extract week
	extract day
	extract hour
	extract minute
}

main
