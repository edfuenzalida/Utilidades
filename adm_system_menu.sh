#!/bin/bash
# Version 1.2
# Fecha 25.11.2022
# by edrox

PS3="
Ingrese una opción: "

while true; do

    echo

    select opc in "${menu[@]}" Salir
        
        do

            case $REPLY in

            1)
                echo
#               echo "Actual espacio consumido en Caché: " 
                sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'
                echo "Limpiando memoria cache"
                echo
                echo "Limpieza realizada...."
                exit
            break 2;;


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

            3)
                echo
                df_answer=`df -h .`
                echo "********************************"
                echo
                echo "Espacio en disco local: "
                echo
                echo "$df_answer"
                echo
                echo "********************************"
                echo
                exit
            break 2;;
                
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

