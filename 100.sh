#! /bin/bash

if [ $# -eq 0 ] ; then
  echo "please specify an exercise (scalar_products, powers_of_ten, derivatives or vectors)"
  exit 1
fi

if [ ! -f $1.py ] ; then
  echo "Did not find $1.py"
  exit 1
fi

let i=0
if [ -f "$1.tex" ] ; then
  rm "$1.tex"
fi
while [ $i -lt 100 ] ; do
  python3 $1.py >> $1.tex
  let i=i+1
done

cat LateX_requierements.txt $1.tex > tmp.tex
rm $1.tex
mv tmp.tex $1.tex
echo "\end{document}" >> $1.tex
