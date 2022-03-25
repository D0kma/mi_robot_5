#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Twist
import numpy as np
import RPi.GPIO as GPIO
import time as time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

Motor1E = 22  # Enable pin 1 of the controller IC
Motor1A = 27  # Input 1 of the controller IC
Motor1B = 7  # Input 2 of the controller IC


Motor2E = 24  # Enable pin 1 of the controller IC
Motor2A = 25  # Input 1 of the controller IC
Motor2B = 8  # Input 2 of the controller IC


# Pines motor 1 izquierdo

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)


# Pines motor 2 derecho
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)


forward1 = GPIO.PWM(Motor1B, 100)  # configuring Enable pin for PWM
reverse1 = GPIO.PWM(Motor1A, 100)  # configuring Enable pin for PWM

forward2 = GPIO.PWM(Motor2B, 100)  # configuring Enable pin for PWM
reverse2 = GPIO.PWM(Motor2A, 100)  # configuring Enable pin for PWM

lineal = 0
angular = 0

x = [0]
y = [0]
theta = [0]

rw = 3.25  # cm Radio rueda
l = 17  # cm Distancia entre ruedas


phi_r = 0
phi_l = 0

Vr = 0
Vl = 0

posicion = Twist()


def callback(msg):
    lineal = round(msg.linear.x, 2)
    angular = round(msg.angular.z, 2)
    
    phi_r = 0  # Velocidad angular en radianes rueda derecha
    phi_l = 0  # Velocidad angular en radianes rueda izquierda
    
    Vr = rw*phi_r  # Velocidad lineal rueda derecha
    Vl = rw*phi_l  # Velocidad lineal rueda izquierda

    
    
    forward1.start(0)
    reverse1.start(0)
    forward2.start(0)
    reverse2.start(0)

    # GPIO a motores

    if lineal > 0:  # Movimiento hacia adelante

        GPIO.output(Motor1E, GPIO.HIGH)
        forward1.ChangeDutyCycle(abs(lineal))
        reverse1.ChangeDutyCycle(0)

        GPIO.output(Motor2E, GPIO.HIGH)
        forward2.ChangeDutyCycle(abs(lineal))
        reverse2.ChangeDutyCycle(0)
        rospy.loginfo(lineal)


    elif lineal < 0:  # Movimiento hacia atrás

        GPIO.output(Motor1E, GPIO.HIGH)
        forward1.ChangeDutyCycle(0)
        reverse1.ChangeDutyCycle(abs(lineal))

        GPIO.output(Motor2E, GPIO.HIGH)
        forward2.ChangeDutyCycle(0)
        reverse2.ChangeDutyCycle(abs(lineal))
        rospy.loginfo(lineal)




    if angular > 0: # Giro a la izquierda

        GPIO.output(Motor1E, GPIO.HIGH)
        forward1.ChangeDutyCycle(abs(angular))
        reverse1.ChangeDutyCycle(0)

        GPIO.output(Motor2E, GPIO.HIGH)
        forward2.ChangeDutyCycle(0)
        reverse2.ChangeDutyCycle(abs(angular))
        rospy.loginfo(angular)

    elif angular < 0:  # Giro a la derecha

        GPIO.output(Motor1E, GPIO.HIGH)
        forward1.ChangeDutyCycle(0)
        reverse1.ChangeDutyCycle(abs(angular))

        GPIO.output(Motor2E, GPIO.HIGH)
        forward2.ChangeDutyCycle(abs(angular))
        reverse2.ChangeDutyCycle(0)
        rospy.loginfo(angular)




    

    
    # Procesamiento de posición

    #posicion.linear.x = x[-1] + 0.5*(Vr+Vl)*np.cos(theta[-1])*dt
    # x.append(posicion.linear.x)
    #posicion.linear.y = y[-1] + 0.5*(Vr+Vl)*np.sin(theta[-1])*dt
    # y.append(posicion.linear.y)
    # theta.append(theta[-1]+(1/l)*(Vr-Vl)*dt)
    # pub.publish(posicion)


# CUERPO DEL CÓDIGO
def robot_central():

    #pub = rospy.Publisher('robot_position', Twist, queue_size=10)
    rospy.init_node('robot_central', anonymous=True)
    rospy.Subscriber('robot_cmdVel', Twist, callback)
    
    rospy.spin()
    
    # 10hz
    
    
    
# Ejecuta función turtle_bot
if __name__ == '__main__':
    robot_central()