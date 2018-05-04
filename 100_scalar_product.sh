#! /bin/bash
let i=0
if [ -f "scalar_product.txt" ] ; then
  rm "scalar_product.txt"
fi
while [ $i -lt 100 ] ; do
  python3 scalar_product.py 5 >> scalar_product.txt
  let i=i+1
done
