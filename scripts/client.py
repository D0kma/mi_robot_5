#!/usr/bin/env python3

import sys
import rospy
from mi_robot_5.srv import *

def main_client(x):

    # Esperamos a que el servicio este activo
    rospy.wait_for_service('robot_player')
    

    try:
	
	# Definimos el servicio y su tipo de mensaje
        mul2num = rospy.ServiceProxy('robot_player', SrvGreek)
        # Recibimos respuesta del servicio con los dos numeros enviados
        resp1=mul2num(x)
        
	
	 
        return print(resp1.name)
	
	# Gestion de errores
    except rospy.ServiceException as e:
        print ("Llamada al servicio fallida: %s",e)

# Funcion que muestra el uso del script
def uso():
    return "USO: rosrun geek_gasteiz client.py [num1 num2]"

if __name__ == "__main__":
    main_client(sys.argv[1])
    
