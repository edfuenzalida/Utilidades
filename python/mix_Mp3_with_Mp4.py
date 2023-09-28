# Importa librerias
import sys
import os
import moviepy.editor as mp

"""
   autor: edrox

    El siguiente script permite mezclar un archivo de audio con un archivo de video
con una compresion media para equilibrar peso vs calidad.

    Para ejecutar el script es necesario darle 2 parametros la 1° ruta  es la del archivo 
de audio y la segunda es la del archivo de video, de tal forma que:

        python mixMp3Mp4.py ruta/ruta/ruta/archivo_audio.mp3 ruta/ruta/archivo_video.mp4

    Dado el ejemplo anterior el archivo de salida seria "archivo_video.mp4" en la ruta desde
donde se lanzo el script.

"""

def procesa_ruta(ruta_audio, ruta_video):

    # Verificar si el archivo audio local existe
    if os.path.exists(ruta_audio):

        # Imprime en caso de ser cierta la ruta del archivo ingresado
        print(f"La ruta ingresada del archivo {ruta_audio} existe en el sistema")
        print

        # Verificar si el archivo video local existe
        if os.path.exists(ruta_video):
        
            print(f"La ruta ingresada del archivo {ruta_video} existe en el sistema")

            # Recibe ruta de archivo audio mp3
            audio = mp.AudioFileClip(ruta_audio)

            #Recibe ruta de archvio video mp4
            video = mp.VideoFileClip(ruta_video)

            # Toma el valor de la ruta del archivo de video y lo separa por / en una lista
            # y retorna el ultimo valor de esa lista
            nombre_archivo = ruta_video.split("/")[-1]

            # Toma el valor de nombre_archivo y lo separa por . en una lista, se queda con
            # el penultimo valor de la cadena como nombre de referencia sin su extension.
            nombre_archivo = nombre_archivo.split(".")[-0]

            # Mezcla el audio y video
            video.audio = audio

            #Escribe un nuevo archivo llamado nombre_archivo.mp4
            video.write_videofile(f"{nombre_archivo}.mp4", preset ="medium")        

        # Si no encuentra el archvio de video
        else:    

            print(f"La ruta ingresada {ruta_video} no existen, ingresar una ruta valida")

    # Si no existe el archivo
    else:

        # Imprime en caso de encontrar el archivo ingresado en sistema
        print(f"La ruta ingresada {ruta_audio} no existen, ingresar una ruta valida")

if __name__ == "__main__":

    # Obtiene la ruta del archivo de sonido
    ruta_audio = sys.argv[1]

    # Obtiene la ruta del archivo de video
    ruta_video = sys.argv[2]

    # Llama a la funcion procesa_ruta
    procesa_ruta(ruta_audio, ruta_video)
