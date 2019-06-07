#!/bin/bash
. /home/xuq7/codestudy/python/FileInventory/fileInventory.sh
listdir=("HI" "codestudy")
date=`date +%s`
for dir in ${listdir[@]};do
cd /home/xuq7/$dir
git add -A
git commit -m "autopush $date"
git push origin master
done
exit
