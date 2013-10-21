#!/usr/bin/env bash

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

python2 ./table_create.py  2&> /dev/null

python2 ./../judy_server.py
