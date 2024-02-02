#/bin/bash
# Este script funciona para automatizar el uso de la herramienta de fuzzing fuff, desde el repositorio apt puede se instalada con el comando
# sudo apt install fuff -y. 
# El script toma una ruta de directorio en donde se encontrara 1 o más diccionarios a ser utilizados durante el fuzzing
# leera todos uno por uno los diccionarios y para cada resultado, devolvera un archivo de texto el cual se guardado en la ruta predefinida
# en la variable "save".
# 
# La estrucutra para lanzar el script es:
# bash discovery_enum_web.sh ruta/diccionarios/ https://url.com/ejemplo ejemplo/resultadosfuff

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
