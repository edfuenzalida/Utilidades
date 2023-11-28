#/bin/bash

#Guarda la ruta de donde se extraeran los archivos de busqueda
ruta=$1

#Guarda url indicada al lanzar script
url=$2

#Guardar ruta donde se guardaran los reportes
save=$3

cd $ruta

ls=`ls`

for file in $ls;
do

nombre=`echo $file | cut -d "." -f 1`

ffuf -u $url/FUZZ/ -c -v -fc 200 -w $file -o $save/result_$nombre.csv -of csv
done
