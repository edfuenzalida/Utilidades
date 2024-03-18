import requests
from bs4 import BeautifulSoup
import re
from termcolor import colored

# Banner bonito
def banner():
    banner = """
    Oo      oO                     o          o      O                 o     
    O O    o o                    O           O      o                 O     
    o  o  O  O          O         o           o      O                 o     
    O   Oo   O         oOo        O           OoOooOOo                 o     
    O        o .oOoO'   o   .oOo  OoOo.       o      O .oOoO' 'o     O O  o  
    o        O O   o    O   O     o   o       O      o O   o   O  o  o OoO   
    o        O o   O    o   o     o   O       o      o o   O   o  O  O o  O  
    O        o `OoO'o   `oO `OoO' O   o       o      O `OoO'o  `Oo'oO' O   o 
    
   *@@@@@@/                                                %@#/@@(                                            
 @*&&%%%%&@%/@@*                                         .@(&%%%%/@@@%%&(/@@                                  
@#%%%%%%%%%%&@%/@/                                      @%#%%%%%&(%@%(&&&@@*@@                                
/*%%%%%%%%%%%%&@%#@#                                   @%%%&%(&@&%%(&&&&&#&@%&@                               
.*%%%%#((#%%%%%%&@%%@/                    (@&#/***/(#%%&&&&%%%%%&#&&&&&&&/&&&%&@                              
./%%%(((((((%%%%%%&@#&@/             @&,/%%%%%%%%%%%%%%%%%%%%%%%(&&&&(&&&/&&&&(@%                             
*/%%#(((*###/(%%&%%%&&&(@@       &@/#%%%%%%%%%%%&%%%%%%%%%%%%%%#&&&&&/&&&%%&&&&,@,                            
#/%%(((((#####/#%%%%%%%%&%(@@  @%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%*&&&&&(&&&&*%&&&(%@                            
@%%%((((/#######/#%%&%%%&%%%&#**(%%%&%%%&%%#&%%%&%%%&%%%&%%%&%%(&&&&&(&&&&&*(&&&*,                            
 @(%((((((########*(%%%%%%%%%%%%&%%%%%%%%.&%%%%%%%%%%%%%%%%%%%%#&&&&&,&&&&&&&&&&,%                            
  @&/((((((#####/(##(*((#%%%%%%%&%%%%%%%%#%%%%%%&%%%%%%%%%%%%%%(&&&&&//&&&&&&&&#,&                            
   .@((((((/(######(*(###((((,/%&%%%%%%%%*&#%%%%%%%%%%%%%%%%%%%#&&&&&&#&&&&&&&(*%,                            
     @#/((((((/###########(/(%%%&%%%%%%%%&, *%%%&%%%%%%%&%%%%%%%(&&&&&&&&&&&#%(&%                             
      %@*(((((((((/****/(((#%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%(&&&&%/%%%(#@                              
         @%/((((((((((((((%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%/%%&#,/@*                         
               %%%@@@@,((%%%%%%%&%%%%%%#&####%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%//#%%%%%%%#,#/*/#%&@,.             
                    #%/(%%&%&%&%&%&%%%%%%%%%%%%%&%&%&%&%&%&%&%&%&%&%&%&%%#*%&%&%&#(%%%&%&%%,,,.@@             
                     %/(%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%&%%%%%%#((%%%%%/%%%%%%%%%%%/,,.(@             
                     @*%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%##%%%%%&%%#(((/%%%%%%%%&%%%%%%%%%%%(*,****/(&##(     
                     &.%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%.**/*//*%%%%%%%%%%%%%%%%%%%%%(%%%%%%&%%%%%%%%%.(@@
                     (,%%%%%%%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%(#/(((,&/&%%&%%%%%%%&%%%#(((&%%%%%%%&%%%%%%%&%&..@
                     (%/%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%(#&/#/%%,%%%%%%%%%%%%%%%##%&%%%%%%%%#%%%%%%#(**%@(
                      %,%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%&,%%%&%%/#%%%%%%%%%%%&%%%%%%%%%%%%%%%(((((,%@%     
                      @#(%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%*&%%%&#,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%//*@&         
                       @.%%%&%%%&%%%&%%%&%%%&%%%&%%%&%%%&%%%%%(((((%%%%%&%%%&%%%&%%%&%%%&%%%&%%%,             
                       /@,%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,&            
                        &&,&%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%(#.            
                         *@,%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,/             
                          #**%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%%%%%&%%%%#,/              
                            &&,&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%%%%%%%%/%@               
                              &&*&%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%&%%%%%%%%%(,@&                
                                @@,#%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%&%%%%%%%%%%%%%%%#/.@&                  
                                   &&,(%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&/&&&&&&%%&%#/*(((((,@&                
                                       @#/(#%%%%%%%%%%%%%%%%%%%%&%%%%%%%%*##(((((((((((((((((,@               
                                          @@%,/(((#%%%%%%%%%%%%%&%%%%%%%%%%*(((/,///*/((((.....@/             
                                               %@@%**/(((((/%%%%&%%&@@&%%%%%/@#         @%*. @*               
                                                          ###@%*(%%%&%%%&%%%/&#                               
                                                                  /@#*%/,,,,,.%                               
                                                                      ,@/.,,,.@  
    by ed :3

    """
    print(colored(banner , 'magenta' , attrs=["bold"]))

banner()
print()

#------------
# FUNCIONES |
#------------

# Función que consulta el recurso .js en caso de error, devuelve el valor del estado de respuesta
def recurso(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error al obtener el recurso {url} - Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al obtener el recurso {url} : {e}")
        return None


# Función que realiza la busqueda de palabras en el recurso y devuelve el número de coincidencias
def hawksearchNum(contenido_js, palabra_buscar):
    matchNum = {}
    for palabra in palabra_buscar:
        matchNum[palabra] = len(re.findall(r'\b' + re.escape(palabra) + r'\b', contenido_js, re.IGNORECASE))
    return matchNum


# Función que realiza la busqueda de palabras en el recurso y devuelve la candena de texto hasta el proximo signo ;

def hawksearchChar(contenido_js, palabra_buscar):
    matchChar = {}
    for palabra in palabra_buscar:
        matchChar[palabra] = re.finditer(r'\b' + re.escape(palabra) + r'\b[^;]*', contenido_js, re.IGNORECASE)
    return matchChar


#------------
# VARIABLES |
#------------

# Variable con la url del recurso a escanear
url = input(colored("Ingrese el recurso .js a analizar: " , 'cyan', attrs=["bold"]))

# Variable que contiene arreglo con palabras a buscar
palabra_buscar = ["http","php","pass","location","redir","url","adm","index","get","post","set","#","ws",\
        "hash","sql","database","db","form","root","key","bkp","qa","dev","html","encry","decry","cipher"]

# Variable que obtiene el contenido del recurso
contenido_js = recurso(url)

#----------------
# CONDICIONALES |
#----------------

# Si hay contenido que leer
if contenido_js:
    # Buscar palabras en el contenido del recurso
    matchNum = hawksearchNum(contenido_js, palabra_buscar)
    matchChar = hawksearchChar(contenido_js, palabra_buscar)

    # Imprime el número de resultados econtrados de la función hawksearchNum
    print()
    print(colored("Número de coincidencias encontradas: " , 'blue', attrs=["bold"]))
    print()
    for palabra, cadena in matchNum.items():
        print(colored(f"{palabra}:", 'green', attrs=["bold"]), colored(f"{cadena} veces" , 'green'))

    # Imprime el detalle de la cadena capturada
    print()
    print(colored("Detalle de cadena capturada: ", 'light_grey', attrs=["bold"]))
    print()
    for palabra, cadena in matchChar.items():
        print(colored(f"{palabra}: ", 'green', attrs=["bold"]))
        print()
        print(*cadena, sep='\n')
        print()



