#!/bin/bash

PS3="
Ingrese una opción: 
"

select opc in Sumar Restar Salir

 do
  case $opc in

    Sumar)

            echo 
            read -p "Ingrese el número de días a avanzar: " di 
            read -p "Ingrese el número de meses a avanzar: " me
            read -p "Ingrese el número de años a avanzar: " ye
            dat=$(date --date='+'"$di"' day +'"$me"' month +'"$ye"' year' +"%Y-%m-%d")
            fecha=$(date)
            
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
            echo "---------------------------------------"
    break;;

    Restar)

            echo 
            read -p "Ingrese el número de días a retroceder: " di 
            read -p "Ingrese el número de meses a retroceder: " me
            read -p "Ingrese el número de años a retroceder: " ye
            dat=$(date --date='-'"$di"' day -'"$me"' month -'"$ye"' year' +"%Y-%m-%d")
            fecha=$(date)
            
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
            echo "---------------------------------------"

    break;;

    Salir)

    break;;

    *)

        echo 
        echo " Opción ingresada no valida"
        echo " Favor ingresar una opciòn válida "    
        echo
    
    esac
    done