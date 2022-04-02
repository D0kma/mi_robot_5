#!/usr/bin/env python3

from mi_robot_5.srv import SrvGreek
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import numpy as np
import time

# Funcion a llamar cuando llegue peticion del cliente
def multiplica_2_num(req):
	pub = rospy.Publisher('robot_cmdVel', Twist, queue_size=10)
	rate = rospy.Rate(10)  # 10hz
	message = Twist()
	f=open('/home/ubuntu/catkin_ws/src/mi_robot_5/results/'+req.name,'r')
	datos=f.read()
	lista_nueva=[]
	for i in datos:
		if i!='\n':
			lista_nueva.append(i)
			
	try:
		int(lista_nueva[3]) # 2 dígitos
		vel_lineal= int(lista_nueva[0]+lista_nueva[1])
		vel_angular= int(lista_nueva[2]+lista_nueva[3])
		
	except: #1 idigito
		vel_lineal= int(lista_nueva[0])
		vel_angular= int(lista_nueva[1])
	
	for j in range(2,len(lista_nueva)):
		if lista_nueva[j] == 's':
		    message.linear.x = -1*vel_lineal
		    message.linear.y = 0
		    message.linear.z = 0
		    print(message)
		    pub.publish(message)

		elif lista_nueva[j] =='w':
		    message.linear.x = vel_lineal
		    message.linear.y = 0
		    message.linear.z = 0
		    print(message)
		    pub.publish(message)

		elif lista_nueva[j] == 'a':
		    message.angular.x = 0
		    message.angular.y = 0
		    message.angular.z = vel_angular
		    print(message)
		    pub.publish(message)

		elif lista_nueva[j] == 'd':
		    message.angular.x = 0
		    message.angular.y = 0
		    message.angular.z = -1*vel_angular
		    print(message)
		    pub.publish(message)
		else:
		    message.linear.x = 0
		    message.linear.y = 0
		    message.linear.z = 0
		    message.angular.x = 0
		    message.angular.y = 0
		    message.angular.z = 0
		    print(message)
		    pub.publish(message)
		time.sleep(0.5)
	res='Proceso Finalizado'
	return res

def main_server():

    	#Iniciamos nodo con nombre server
	rospy.init_node('robot_player')

    	# Creamos el servicio llamado 'mul2num', con tipo de servicio 'SrvGeek', 
    	# llamaremos a la funcion 'multiplica_2_num' cuando llegue peticion
	s = rospy.Service('robot_player', SrvGreek, multiplica_2_num)
	print ("Esperando peticion...")
	rospy.spin()
	print ("\nCerrando servidor")
if __name__ == "__main__":
    main_server()
