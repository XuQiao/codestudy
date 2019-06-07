#!/bin/bash
clear
echo "This is information provided by mysystem.sh.  Program starts now."
echo "Hello, $USER"
echo
echo "Today's date is `date`, this is week `date +"%V"`."
echo
echo "These users are currently connected:"w | cut -d " " -f 1 - | grep -v USER | sort -u
echo
echo "This is `uname -s` running on a `uname -m` processor."
echo "This is the uptime information:"
uptime
echo
echo "That's all folks!"

#!/bin/bash
clear
printf "This is information provided by mysystem.sh.  Program starts now.\n"
printf "Hello, $USER.\n\n"
printf "Today's date is `date`, this is week `date +"%V"`.\n\n"
printf "These users are currently connected:\n"
w | cut -d " " -f 1 - | grep -v USER | sort -u
printf "\n"
printf "This is `uname -s` running on a `uname -m` processor.\n\n"
printf "This is the uptime information:\n"
uptime
printf "\n"
printf "That's all folks!\n"
