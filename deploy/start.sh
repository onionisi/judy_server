#!/usr/bin/env bash

SRC_DIR=`pwd`

function dep_detect() {
	which mysqld > /dev/null
	if [ $? -ne 0 ]; then
		echo "You need to install mysql !!!"
		return 1
	fi

	which python2 > /dev/null
	if [ $? -ne 0 ]; then
		echo "You need to install python2"
		return 2
	fi
}

dep_detect

# create MenuTbl|MenuTypeTbl|OrderDetailTbl|OrderTbl|TableTbl|UserTbl 
python2 $SRC_DIR/deploy/table_create.py  2&> /dev/null
# create procedure
mysql -u root -D cook < unite_proc.sql

# start server
python2 $SRC_DIR/judy_server.py
