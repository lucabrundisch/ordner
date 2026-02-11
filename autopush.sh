#!/bin/sh

while true
do
	git add .
	git commit -m "Auto update $(date)" 2>/dev/null
	git push 2>/dev/null
	sleep 30
done
