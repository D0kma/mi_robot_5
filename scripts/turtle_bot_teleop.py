#!/usr/bin/env python3

import rospy
import tty
import sys
import cv2
import numpy as np
import termios
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def turtle_bot_teleop():

	pub = rospy.Publisher('arm_color', String, queue_size=10) #declaramos la variable que publicará las velocidades
	rospy.init_node('turtle_bot_teleop', anonymous=True)  #inicializamos el nodo
	rate = rospy.Rate(10) #definimos la frecuencia de actualización

	filedescriptors = termios.tcgetattr(sys.stdin) 
	tty.setcbreak(sys.stdin)
	
	menssage="Esperando color"
	X=input()
	print(X)
		

	cap = cv2.VideoCapture(0)
	#Azul
	azBa = np.array([100,100,20],np.uint8)
	azAl = np.array([125,255,255],np.uint8)
	#amarillo
	amBa = np.array([15,100,20],np.uint8)
	amAl = np.array([45,255,255],np.uint8)
	#rojo 
	reBa1 = np.array([0,100,20],np.uint8)
	reAl1 = np.array([5,255,255],np.uint8)
	reBa2 = np.array([175,100,20],np.uint8)
	reAl2 = np.array([179,255,255],np.uint8)
	
	if X=="blue":		
		while True:
		  ret,frame = cap.read()
		  if ret==True:
		    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		    mask = cv2.inRange(frameHSV,azBa,azAl)
		    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
		    for c in contornos:
		      area = cv2.contourArea(c)
		      if area > 3000:
		        M = cv2.moments(c)
		        if (M["m00"]==0): M["m00"]=1
		        x = int(M["m10"]/M["m00"])
		        y = int(M['m01']/M['m00'])
		        cv2.circle(frame, (x,y), 7, (0,255,0), -1)
		        font = cv2.FONT_HERSHEY_SIMPLEX
		        cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
		        nuevoContorno = cv2.convexHull(c)
		        cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
		    cv2.imshow('frame',frame)
		    if cv2.waitKey(1) & 0xFF == ord('s'):
		      break
		cap.release()
		cv2.destroyAllWindows()
	if X=="yellow":
		while True:
		  ret,frame = cap.read()
		  if ret==True:
		    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		    mask = cv2.inRange(frameHSV,amBa,amAl)
		    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
		    for c in contornos:
		      area = cv2.contourArea(c)
		      if area > 3000:
		        M = cv2.moments(c)
		        if (M["m00"]==0): M["m00"]=1
		        x = int(M["m10"]/M["m00"])
		        y = int(M['m01']/M['m00'])
		        cv2.circle(frame, (x,y), 7, (0,0,255), -1)
		        font = cv2.FONT_HERSHEY_SIMPLEX
		        cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
		        nuevoContorno = cv2.convexHull(c)
		        cv2.drawContours(frame, [nuevoContorno], 0, (0,255,255), 3)
		    #cv2.imshow('maskAzul',mask)
		    cv2.imshow('frame',frame)
		    if cv2.waitKey(1) & 0xFF == ord('s'):
		      break
		cap.release()
		cv2.destroyAllWindows()
		
	if X=="red":	
		while True:
		  ret,frame = cap.read()
		  if ret==True:
		    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		    maskRed1 = cv2.inRange(frameHSV, reBa1, reAl1)
		    maskRed2 = cv2.inRange(frameHSV, reBa2, reAl2)
		    maskRed = cv2.add(maskRed1, maskRed2)
		    contornos,_ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
		    for c in contornos:
		      area = cv2.contourArea(c)
		      if area > 3000:
		        M = cv2.moments(c)
		        if (M["m00"]==0): M["m00"]=1
		        x = int(M["m10"]/M["m00"])
		        y = int(M['m01']/M['m00'])
		        cv2.circle(frame, (x,y), 7, (0,255,0), -1)
		        font = cv2.FONT_HERSHEY_SIMPLEX
		        cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
		        nuevoContorno = cv2.convexHull(c)
		        cv2.drawContours(frame, [nuevoContorno], 0, (0,0,255), 3)
		    #cv2.imshow('maskAzul',mask)
		    cv2.imshow('frame',frame)
		    if cv2.waitKey(1) & 0xFF == ord('s'):
		      break
		cap.release()
		cv2.destroyAllWindows()
if __name__ == '__main__':
	try:

		turtle_bot_teleop()
	except rospy.ROSInterruptException:
		pass
