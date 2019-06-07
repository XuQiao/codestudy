#!/bin/bash

# Setup environment and working dir, initialize state
#PATH="/usr/local/bin:$PATH"
FI_HOME=/home/xuq7/codestudy/python/FileInventory
INS_DIR1=/cms/store/user/qixu/flow/PACorrHM/skim
INS_DIR2=/cms/store/user/qixu/flow/PACorrHM
INS_DIR3=/cms/store/user/qixu/
cd $FI_HOME
eval `/usr/local/bin/config_pkg -sh -a lio`
if [ -f $FI_HOME/fileInventory.state ]; then 
  source $FI_HOME/fileInventory.state
else
  COUNTER=0
fi 

# Perform Inventory
echo -n `du -sb $INS_DIR1` > $FI_HOME/store.inv1.$COUNTER
echo -ne '\t'`find $INS_DIR1 -type f | wc -l` >> $FI_HOME/store.inv1.$COUNTER
RESULT1=$?
echo "$(date) - performed inventory of $INS_DIR1 with exit code $RESULT1" >> $FI_HOME/fileInventory.log
# retry on 2 line output or error code twice
if [[ $( wc -l < store.inv1.$COUNTER ) -lt 3 || $RESULT1 -ne 0 ]]; then
#  sleep 300
  echo -n `du -sb $INS_DIR1` > $FI_HOME/store.inv1.$COUNTER
  echo -ne '\t'`find $INS_DIR1 -type f | wc -l` >> $FI_HOME/store.inv1.$COUNTER
  RESULT1=$?
  echo "$(date) - Retry 1: $INS_DIR1 with exit code $RESULT1" >> $FI_HOME/fileInventory.log
fi
if [[ $( wc -l < store.inv1.$COUNTER ) -lt 3 || $RESULT1 -ne 0 ]]; then
#  sleep 300
  echo -n `du -sb $INS_DIR1/*` > $FI_HOME/store.inv1.$COUNTER
  echo -ne '\t'`find $INS_DIR1 -type f | wc -l` >> $FI_HOME/store.inv1.$COUNTER
  RESULT1=$?
  echo "$(date) - Retry 2: $INS_DIR1 with exit code $RESULT1" >> $FI_HOME/fileInventory.log
fi

/usr/local/lio/bin/lio_du -h -s @:$INS_DIR2/* > $FI_HOME/store.inv2.$COUNTER
RESULT2=$?
echo "$(date) - performed inventory of $INS_DIR2 with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
# retry on 2 line output or error code twice
if [[ $( wc -l < store.inv2.$COUNTER ) -lt 3 || $USER_RESULT -ne 0 ]]; then
#  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:$INS_DIR2/* > $FI_HOME/store.inv2.$COUNTER
  USER_RESULT=$?
  echo "$(date) - Retry 1: /cms/store/user/ with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
fi
if [[ $( wc -l < store.inv2.$COUNTER ) -lt 3 || $USER_RESULT -ne 0 ]]; then
#  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:$INS_DIR2/* > $FI_HOME/store.inv2.$COUNTER
  USER_RESULT=$?
  echo "$(date) - Retry 2: $INS_DIR2 with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
fi

echo -n `du -sb $INS_DIR3` > $FI_HOME/store.inv3.$COUNTER
echo -ne '\t'`find $INS_DIR3 -type f | wc -l` >> $FI_HOME/store.inv3.$COUNTER
RESULT3=$?
echo "$(date) - performed inventory of $INS_DIR3 with exit code $RESULT3" >> $FI_HOME/fileInventory.log
# retry on 2 line output or error code twice
if [[ $( wc -l < store.inv3.$COUNTER ) -lt 3 || $RESULT3 -ne 0 ]]; then
#  sleep 300
  echo -n `du -sb $INS_DIR3` > $FI_HOME/store.inv3.$COUNTER
  echo -ne '\t'`find $INS_DIR3 -type f | wc -l` >> $FI_HOME/store.inv3.$COUNTER
  RESULT3=$?
  echo "$(date) - Retry 1: $INS_DIR3 with exit code $RESULT3" >> $FI_HOME/fileInventory.log
fi
if [[ $( wc -l < store.inv3.$COUNTER ) -lt 3 || $RESULT1 -ne 0 ]]; then
#  sleep 300
  echo -n `du -sb $INS_DIR3/*` > $FI_HOME/store.inv3.$COUNTER
  echo -ne '\t'`find $INS_DIR3 -type f | wc -l` >> $FI_HOME/store.inv3.$COUNTER
  RESULT3=$?
  echo "$(date) - Retry 2: $INS_DIR3 with exit code $RESULT3" >> $FI_HOME/fileInventory.log
fi

# Report to webpage
python reportFileInventory.py $COUNTER

#update and record state and exit
#COUNTER=$(( $COUNTER + 1 ))
#echo "COUNTER=$COUNTER" > $FI_HOME/fileInventory.state
