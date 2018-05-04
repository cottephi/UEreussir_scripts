#! /bin/bash
let i=0
if [ -f "vectors.txt" ] ; then
  rm "vectors.txt"
fi
while [ $i -lt 100 ] ; do
  python3 vectors.py 5 >> vectors.txt
  let i=i+1
done
