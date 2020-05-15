#!/bin/bash

if [ "$1" = "get" ]; then
	value=$(xfconf-query -c "$2" -p "/$3/$4" -l -v)
	value=$(echo "$value" | sed "s%/$3/$4  %%g")
	echo "$value"
	exit 0
elif [ "$1" = "set" ]; then
	xfconf-query -c "$2" -p "/$3/$4" -s "$5"
fi
