#!/bin/bash

# Setup environment and working dir, initialize state
PATH="/usr/local/bin:$PATH"
FI_HOME=/home/appelte1/T2VanderbiltStorageTools/FileInventory/
cd $FI_HOME
eval `/usr/local/bin/config_pkg -sh -a lio`
if [ -f $FI_HOME/fileInventory.state ]; then 
  source $FI_HOME/fileInventory.state
else
  COUNTER=0
fi 

# Perform Inventory
/usr/local/lio/bin/lio_du -h -s @:/cms/store/ > $FI_HOME/store.inv.$COUNTER
STORE_RESULT=$?
echo "$(date) - performed inventory of /cms/store/ with exit code $STORE_RESULT" >> $FI_HOME/fileInventory.log
# retry on 2 line output or error code twice
if [[ $( wc -l < store.inv.$COUNTER ) -lt 3 || $STORE_RESULT -ne 0 ]]; then
  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:/cms/store/ > $FI_HOME/store.inv.$COUNTER
  STORE_RESULT=$?
  echo "$(date) - Retry 1: /cms/store/ with exit code $STORE_RESULT" >> $FI_HOME/fileInventory.log
fi
if [[ $( wc -l < store.inv.$COUNTER ) -lt 3 || $STORE_RESULT -ne 0 ]]; then
  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:/cms/store/ > $FI_HOME/store.inv.$COUNTER
  STORE_RESULT=$?
  echo "$(date) - Retry 2: /cms/store/ with exit code $STORE_RESULT" >> $FI_HOME/fileInventory.log
fi

/usr/local/lio/bin/lio_du -h -s @:/cms/store/user/ > $FI_HOME/store.user.inv.$COUNTER
USER_RESULT=$?
echo "$(date) - performed inventory of /cms/store/user/ with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
# retry on 2 line output or error code twice
if [[ $( wc -l < store.inv.$COUNTER ) -lt 3 || $USER_RESULT -ne 0 ]]; then
  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:/cms/store/user/ > $FI_HOME/store.user.inv.$COUNTER
  USER_RESULT=$?
  echo "$(date) - Retry 1: /cms/store/user/ with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
fi
if [[ $( wc -l < store.inv.$COUNTER ) -lt 3 || $USER_RESULT -ne 0 ]]; then
  sleep 300
  /usr/local/lio/bin/lio_du -h -s @:/cms/store/user/ > $FI_HOME/store.user.inv.$COUNTER
  USER_RESULT=$?
  echo "$(date) - Retry 2: /cms/store/user/ with exit code $USER_RESULT" >> $FI_HOME/fileInventory.log
fi

# Report to webpage
/usr/local/bin/python reportFileInventory.py $COUNTER

#update and record state and exit
COUNTER=$(( $COUNTER + 1 ))
echo "COUNTER=$COUNTER" > $FI_HOME/fileInventory.state
