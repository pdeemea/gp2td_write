#!/bin/sh

export PYTHONHOME=/usr/local
export PATH=$PATH:/usr/local/lib/python2.7
export JAVA_HOME=/usr/bin
test_input=/dev/stdin

#cat $test_input >> /home/gpadmin/export.txt
cat $test_input | python2.7 /home/gpadmin/test_jdbc.py
