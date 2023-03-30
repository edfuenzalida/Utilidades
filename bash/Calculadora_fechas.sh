#!/bin/bash
# Versión 1.2

PS3="
Ingrese una opción: "

opciones=("Sumar" "Restar")

while true; do

        echo
        echo "Calculadora para fechas"
        echo

        select opc in "${opciones[@]}" Salir

        do
        case $REPLY in

        1)
                echo 
                read -p "Ingrese el número de días a avanzar: " di 
                read -p "Ingrese el número de meses a avanzar: " me
                read -p "Ingrese el número de años a avanzar: " ye
                dat=$(date --date='+'"$di"' day +'"$me"' month +'"$ye"' year' +"%Y-%m-%d")
                fecha=$(date)
                
                echo
                echo "---------------------------------------"
                echo 
                echo "Fecha actual: $fecha"
                echo 
                echo "Días a mover: +$di"
                echo
                echo "Meses a mover: +$me"
                echo
                echo "Años a mover: +$ye"
                echo 
                echo "Resultado de fecha modificada: $dat"
                echo
                cal "$(date --date='+'"$di"' day +'"$me"' month +'"$ye"' year' +"%Y-%m-%d")"
                echo
                echo "---------------------------------------"
        break;;

        2)

                echo 
                read -p "Ingrese el número de días a retroceder: " di 
                read -p "Ingrese el número de meses a retroceder: " me
                read -p "Ingrese el número de años a retroceder: " ye
                dat=$(date --date='-'"$di"' day -'"$me"' month -'"$ye"' year' +"%Y-%m-%d")
                fecha=$(date)
                
                echo
                echo "---------------------------------------"
                echo 
                echo "Fecha actual: $fecha"
                echo 
                echo "Días a retroceder: -$di"
                echo
                echo "Meses a retroceder: -$me"
                echo
                echo "Años a retroceder: -$ye"
                echo 
                echo "Resultado de fecha modificada: $dat"
                echo
                cal "$(date --date='-'"$di"' day -'"$me"' month -'"$ye"' year' +"%Y-%m-%d")"
                echo
                echo "---------------------------------------"

        break;;

        $((${#opciones[@]}+1)))

                echo
                echo "--------------------------"
                echo
                echo "Hasta pronto..."
                echo
                echo "---------------------------"
                echo

        break 2;;

        *)
                echo 
                echo "-------------------------------------"
                echo
                echo " Opción ingresada no válida"
                echo " Favor ingresar una opciòn válida "  
                echo
                echo "--------------------------------------"  
                echo
        
        esac
        done
done        