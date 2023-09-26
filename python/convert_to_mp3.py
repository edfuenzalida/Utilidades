# Importa librerias
import sys
import os
import moviepy.editor as mp


""""

autor: edrox

    El siguiente script permite convertir un archivo de audio mp4 a mp3 con una tasa
de transferencia de bits de 192kbps, lo equivale a un sonido de CD, equilibrando el
sonido con el peso de l archivo sin perder calidad.

    Para ejecutar el script es necesario darle como parametro la ruta del archivo 
que se quiere convertir, de tal forma que:

        python convert_to_mp3.py ruta/ruta/ruta/archivo.mp4

    Dado el ejemplo anterior el archivo de salida seria "archivo.mp3" en la ruta desde
donde se lanzo el script.

"""

def ingresa_ruta(ruta):

    # Verificar si el archivo existe
    if os.path.exists(ruta):

        # Imprime en caso de ser cierto la ruta del archivo ingresado
        print(f"La ruta ingresada {ruta} existe en el sistema")

        # Recibe ruta de archivo mp4 a convertir
        audiomp4 = mp.AudioFileClip(ruta)

        # Pasa el resultado de la conversion
        audiomp3 = audiomp4

        # Toma el valor de ruta y lo separa por / en una lista y retorna el ulitmo
        # valor de la lista
        nombre = ruta.split("/")[-1]
        
        # Toma el valor y lo separa por . en una lista y se queda con el penultimo 
        # valor de la cadena ruta que es el nombre original del archivo sin su 
        # extension
        nombre = nombre.split(".")[-0]

        # Se queda con el penultimo valor de la cadena ruta que es el nombre original
        # del archivo sin su extension
        
        # Escribe un nuevo archivo llamado audioMp3.mp3 con tasa de bits de 192 kbps
        # en la misma ruta desde donde se ejecuta el script
        audiomp3.write_audiofile(f"{nombre}.mp3", bitrate="192k")

    # Sino existe el archivo
    else:

        # Imprime en caso de no encontrarse el archivo ingresado
        print(f"La ruta ingresa {ruta} no existe, ingresar una ruta valida")

if __name__ == "__main__":
         
            #Obtiene la ruta del archivo desde los argumentos de la linea de comandos
            ruta = sys.argv[1]

            #Llama a la funcion ingresa_ruta para procesar el argumento entregado
            ingresa_ruta(ruta)