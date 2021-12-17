import pyfiglet
import sys
import socket
from datetime import datetime		#Obtenemos la fecha
  
resultadobanner = pyfiglet.figlet_format("ESCANER DE PUERTOS") #Banner with pyfiglet
print(resultadobanner)

# Segundo banner

print("-" * 50)
print("BY PABLITE5")
print("-" * 50)

if len(sys.argv) == 2:  # Objetivo a definir
     
   objetivo = socket.gethostbyname(sys.argv[1])	#conexión para obtener la IP del host, obtiene la IP del objetivo
else:
    print("ERROR")				#error al obtener objetivo
 
# BANNER
print("-" * 50)
print("Escaneando... " + objetivo)
print("Inicio escáner" + str(datetime.now()))
print("-" * 50)
  
try:
     
    
    for puerto in range(1,65535):					#rango de puertos a escanear
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#conexión socket por cada puerto
        socket.setdefaulttimeout(1)
         
        # error
        resultado = s.connect_ex((objetivo,puerto))			#Obtenemos true o false
        if resultado == 0:						#Indicador 0, la operación se realiza correctamente
            print("Puerto {} abierto".format(puerto))			#Impresión puerto
        s.close()
         
#EXCEPCIONES
except KeyboardInterrupt:      
        print("\n SALIENDO !!!!")
        sys.exit()
except socket.gaierror:
        print("\n No se puede resolver !!!!")
        sys.exit()
except socket.error:
        print("\ SERVIDOR NO RESPONDE !!!!")
        sys.exit()
