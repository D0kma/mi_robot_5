#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Vector3
import numpy as np
import math

Gamma = 0
Theta = 0
# CUERPO DEL CÓDIGO

r1 = 15.8  # cm
r2 = 14  # cm
zinicial = 13  # cm


def callback(msg):
	global r1
	global r2
	global zinicial
	global Gamma
	global Theta

	message = Vector3()

	Gammarad = np.arcsin((msg.z)/r2)
	Gamma = Gammarad*180/np.pi
	Gamma = round(Gamma, 2)
	Thetarad = np.arccos(msg.x/(r2*np.cos(Gammarad)+r1))
	Theta = Thetarad*180/np.pi
	Theta = round(Theta, 2)

	message.x=Theta
	message.y=Gamma
	if np.isnan(Theta):
		print('Valores fuera del volumen de trabajo, intente de nuevo.')

	else:
		pub = rospy.Publisher('robot_cmdAngle', Vector3, queue_size=10)
		pub.publish(message)
		rospy.loginfo(message)

def robot_manipulator_planner():

	rospy.Subscriber('robot_manipulator_goal', Vector3,callback)
	rospy.init_node('robot_manipulator_planner', anonymous=True)
	rate = rospy.Rate(28)  # 10hz

	# Ingreso x, y, z
	# x_str = input("Ingrese el valor X del objetivo en cm:  ")
	# try:
	# 	x = float(x_str)
	# 	print('X: ', x, ' cm')
	# except:
	# 	print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# y_str = input("Ingrese el valor Y del objetivo en cm:  ")
	# try:
	# 	y = float(y_str)
	# 	print('Y: ', y, ' cm')
	# except:
	# 	print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# z_str = input("Ingrese el valor Z del objetivo en cm:  ")
	# try:
	# 	z = float(z_str)
	# 	print('Z: ', z, ' cm')
	# except:
	# 	print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# lista = [x_str, y_str, z_str]

	# message = Vector3()

	# pub.publish(message)

	# Press 'n Release  letras: (j, l) servo 1 izq derecha; (i, k) servo 2 arriba abajo; (u, o) servo 3 abre cierra

	# while True:
	# 	# Globales
	# 	global r1
	# 	global r2
	# 	global zinicial
	# 	global Gamma
	# 	global Theta

	# 	Gammarad = np.arcsin((z)/r2)
	# 	Gamma = Gammarad*180/np.pi
	# 	Gamma = round(Gamma, 2)
	# 	Thetarad = np.arccos(x/(r2*np.cos(Gammarad)+r1))
	# 	Theta = Thetarad*180/np.pi
	# 	Theta = round(Theta, 2)

	# 	if np.isnan(Theta):
	# 		print('Valores fuera del volumen de trabajo, intente de nuevo:')

	# 		# Ingreso x, y, z
	# 		x_str = input("Ingrese el valor X del objetivo en cm:  ")
	# 		try:
	# 			x = float(x_str)
	# 			print('X: ', x, ' cm')
	# 		except:
	# 			print(
	# 				'Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# 		y_str = input("Ingrese el valor Y del objetivo en cm:  ")
	# 		try:
	# 			y = float(y_str)
	# 			print('Y: ', y, ' cm')
	# 		except:
	# 			print(
	# 				'Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# 		z_str = input("Ingrese el valor Z del objetivo en cm:  ")
	# 		try:
	# 			z = float(z_str)
	# 			print('Z: ', z, ' cm')
	# 		except:
	# 			print(
	# 				'Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

	# 	else:

	# 		print('Gamma: ', Gamma, ' ; Theta: ', Theta)
	# 		message.x = Theta
	# 		message.y = Gamma
			
			# rospy.loginfo(message)
	rate.sleep()
	rospy.spin()


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_manipulator_planner()
    except rospy.ROSInterruptException:
        pass
