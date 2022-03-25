#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Twist
import numpy as np



# CUERPO DEL CÓDIGO
def robot_teleop():
        
    pub = rospy.Publisher('robot_cmdVel', Twist, queue_size=10)
    rospy.init_node('robot_teleop', anonymous=True)
    rate = rospy.Rate(28)  # 10hz


    # Set velocidad lineal y angular
    speed_str = input("Enter the speed: ")
    try:
        speed = int(speed_str)
        print('Speed: ', speed)
    except:
        print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')
    
    
    angle_str = input("Enter the angle: ")
    
    try:
        angle = int(angle_str)
        print('Angle: ', angle)
    except:
        print('Se ha ingresado un valor inválido. Es necesario reiniciar el nodo')


    lista = [speed_str, angle_str]

    while not rospy.is_shutdown():

        message = Twist()
        message.linear.x = 0
        message.linear.y = 0
        message.linear.z = 0
        message.angular.x = 0
        message.angular.y = 0
        message.angular.z = 0
        #pub.publish(message)
        
        # Press 'n Release 
        def on_press(key):
            try:
                #key.char 
                if key.char == 'w':
                    message.linear.x = speed
                    message.linear.y = 0
                    message.linear.z = 0
                    pub.publish(message)

                    lista.append(str(key.char))
                    print("lista: ", lista)
                    rospy.loginfo(message)


                elif key.char == 'a':
                    message.angular.x = 0
                    message.angular.y = 0
                    message.angular.z = angle
                    pub.publish(message)

                    lista.append(str(key.char))
                    print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 's':
                    message.linear.x = (-1)*speed
                    message.linear.y = 0
                    message.linear.z = 0
                    pub.publish(message)

                    lista.append(str(key.char))
                    print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'd':
                    message.angular.x = 0
                    message.angular.y = 0
                    message.angular.z = (-1)*angle
                    pub.publish(message)

                    lista.append(str(key.char))
                    print("lista: ", lista)
                    rospy.loginfo(message)
                
                else:
                    None


                np.savetxt('lista.txt', lista, fmt="%s")
                                    
            except:
                pass


        def on_release(key):

            message.linear.x = 0
            message.linear.y = 0
            message.linear.z = 0
            message.angular.x = 0
            message.angular.y = 0
            message.angular.z = 0
            #
            try:
                if key.char == 'w':
                    pub.publish(message)
                    lista.append('o')
                    print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'a':
                    pub.publish(message)
                    lista.append('o')
                    print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 's':
                    pub.publish(message)
                    lista.append('o')
                    print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'd':
                    pub.publish(message)
                    lista.append('o')
                    print("lista: ", lista)
                    rospy.loginfo(message)
                
                else:
                    None
                
                
                np.savetxt('lista.txt', lista, fmt="%s")

            except:
                pass
            #
            #

        #rospy.loginfo(message)
        rate.sleep()

        # Collect events until released
        with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_teleop()
    except rospy.ROSInterruptException:
        pass