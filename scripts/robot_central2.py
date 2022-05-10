#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Vector3
import numpy as np
import RPi.GPIO as GPIO
import time as time
import os
from time import sleep
from gpiozero import AngularServo
os.system("sudo pigpiod")


limInf = 0
limSup = 90

angularx=0
angulary=0
angularz=0

# Pines motor 1 izquierdo
servo1 = AngularServo(17, min_angle=limInf, max_angle=limSup)
servo2 = AngularServo(5, min_angle=limInf, max_angle=limSup)
servo3 = AngularServo(6, min_angle=limInf, max_angle=limSup)




servo1.angle = 45
servo2.angle = 90
servo3.angle = 90

r1=15.8 #cm
r2=14 #cm
zinicial=13 #cm


def callback(msg):

    # print('prueba2')
    
    angularz = round(msg.z, 2)
    angularx = round(msg.x, 2)
    angulary = round(msg.y, 2)


    servo1.angle = angularx-45
    servo2.angle = angulary
    servo3.angle = angularz


    message = Vector3()


    
    #Posición
    angularx=angularx*np.pi/180
    angulary=angulary*np.pi/180
    angularz=angularz*np.pi/180
    
    message.x = (r2*np.cos(angulary)+r1)*np.cos(angularx)
    message.y = (r2*np.cos(angulary)+r1)*np.sin(angularx)
    message.z = r2*np.sin(angulary)+zinicial
    
    
    

# rospy.loginfo(servo1.value,',',servo.value)


# CUERPO DEL CÓDIGO
def robot_central():

    
    
    rospy.init_node('robot_central', anonymous=True)
    pub = rospy.Publisher('robot_manipulator_ping_pong', String, queue_size=10)	
    pub.publish('blue')    
    rospy.loginfo(message)
    rospy.Subscriber('robot_cmdAngle', Vector3, callback)
    rate = rospy.Rate(28)  # 10hz

    rospy.spin()
    



# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_central()
    except rospy.ROSInterruptException:
        pass
