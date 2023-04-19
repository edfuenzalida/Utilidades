#!/bin/bash
# Version 1.2.5
# Fecha 18.04.2023
# by edrox

PS3="
Ingrese una opción: "

menu=("Borrar Cache" "Actualizar paquetes DNF" "Consultar espacio en disco" "Memoria RAM Disponible")

while true; do

    echo
    echo "            Bienvenido al menu de utilidades"
    echo
    echo "Seleccione una opción:"
    echo

    select opc in "${menu[@]}" Salir
        
        do

            case $REPLY in

            1)
                echo
                sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'
                echo "*******************************"
                echo
                echo "Limpiando memoria cache"
                echo
                echo "*******************************"
                sleep 2
                echo "Limpieza realizada...."
                echo
                echo "*******************************"
                echo
                sleep 2
            break;;

            2)
                echo
                sudo dnf upgrade -y
                echo "********************************"
                echo
                echo "Sistema actualizado....."
                echo
                echo "********************************"
                echo
                sleep 2
            break;;

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
                sleep 2
            break;;
                
	        4)
                free_answer=`free -h`
                echo
                echo "**********************************"
                echo
                echo " Cantidad de memoria RAM disponible: "
                echo
                echo "$free_answer"
                echo 
                echo "**********************************"
                echo
                sleep 2
            break;;

	        $((${#menu[@]}+1)))

                echo
                echo "---------------------------"
                echo
                echo "See you later bro!... :3"
                echo
                echo "---------------------------"
                echo
                exit
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

