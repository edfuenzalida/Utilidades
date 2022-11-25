#!/bin/bash

PS3="
Ingrese una opción: "

<<<<<<< HEAD
menu=("Limpiar caché")
=======
menu=("Limpiar caché" "Actualizar DNF")
>>>>>>> ramaBeta

while true; do

    echo

    select opc in "${menu[@]}" Salir
        
        do

            case $REPLY in

            1)
                echo
#               echo "Actual espacio consumido en Caché: " 
                sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'
<<<<<<< HEAD
                echo "Limpiando memoria cache"
                echo
                echo "Limpieza realizada...."
                exit
            break 2;;

=======
                echo "*******************************"
                echo "Limpiando memoria cache"
                echo "*******************************"
                sleep 2
                echo "Limpieza realizada...."
                echo "*******************************"
                echo
                exit
            break 2;;

            2)
                echo
                sudo dnf upgrade -y
                echo "********************************"
                echo
                echo "Sistema actualizado....."
                echo
                echo "********************************"
                echo
                exit
            break 2;;
                
>>>>>>> ramaBeta
            $((${#menu[@]}+1)))

                echo
                echo "---------------------------"
                echo
                echo "See you later bro!... :3"
                echo
                echo "---------------------------"
            break 2;;


            

            *)
                echo
                echo "---------------------------"
                echo
                echo "Menú ingresado no existente"
                echo "Favor leer el menú e introducir un menù existente"
                echo
                echo "---------------------------"
                echo
    
            break;;
            
    esac
  done            
done

