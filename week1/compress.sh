#!/bin/bash

if [ "$1" = "-h" ] || [ "$1" = "-help" ]; then
    echo "Help text"
    exit 1
fi

if [ "$#" -ne 2 ]; then
    echo "You need two input arguments, first path, then minimum size"
    exit 1
else
    gzip `find "$1" -size "+$2"`  
fi


