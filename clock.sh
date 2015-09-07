#!/bin/bash

control_c()
# run if user hits control-c
{
  echo
  echo "Bye Bye"
  exit 1
}


while [ 1 > 0 ] 
do
    date
    trap control_c SIGINT
done
