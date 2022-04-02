#!/usr/bin/env python3


import rospy
import tty
import sys
import termios
import keyboard
# from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Twist
import numpy as np
import time


# CUERPO DEL CÓDIGO
def robot_teleop():

    pub = rospy.Publisher('robot_cmdVel', Twist, queue_size=10)
    rospy.init_node('robot_teleop', anonymous=True)
    rate = rospy.Rate(25)  # 10hz

    # Set velocidad lineal y angular
    speed_str = input("Enter the speed in int (max 7 cm/s): ")
    try:
        speed = int(speed_str)
        print('Speed: ', speed)
    except:
        print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

    angle_str = input("Enter the angle in int (max 8 rpm): ")

    try:
        angle = int(angle_str)
        print('Angle: ', angle)
    except:
        print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')

    lista = [speed_str, angle_str]

    filedescriptors = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)
    x = 0

    

    while not rospy.is_shutdown():

        message = Twist()
        message.linear.x = 0
        message.linear.y = 0
        message.linear.z = 0
        message.angular.x = 0
        message.angular.y = 0
        message.angular.z = 0
        pub.publish(message)

        # Press 'n Release
        # def key_press(key):
        # try:
        # x
        
        x = sys.stdin.read(1)[0]
        if x == 'w':
            message.linear.x = speed
            message.linear.y = 0
            message.linear.z = 0
            pub.publish(message)

            

        elif x == 'a':
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = angle
            pub.publish(message)



        elif x == 's':
            message.linear.x = (-1)*speed
            message.linear.y = 0
            message.linear.z = 0
            pub.publish(message)


        elif x == 'd':
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = (-1)*angle
            pub.publish(message)


        else:
            x = 'o'


        np.savetxt('lista.txt', lista, fmt="%s")
        lista.append(str(x))
        print("lista: ", lista)
        rospy.loginfo(message)

        # except:
        #   pass

        #
        #

        # rospy.loginfo(message)
        rate.sleep()

        # Collect events until released
        # with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        # listener.join()


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_teleop()
    except rospy.ROSInterruptException:
        pass
