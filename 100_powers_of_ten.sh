#! /bin/bash

difficulty=5
if [ $# -eq 1 ] ; then
  difficulty=$1
fi

let i=0
if [ -f "powers_of_ten.txt" ] ; then
  rm "powers_of_ten.txt"
fi
while [ $i -lt 100 ] ; do
  python3 powers_of_ten.py $difficulty >> powers_of_ten.txt
  let i=i+1
done

