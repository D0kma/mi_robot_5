#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Vector3
import numpy as np
M1 = 90
M2 = 90
M3 = 90

# CUERPO DEL CÓDIGO


def robot_manipulator_teleop():

    pub = rospy.Publisher('robot_cmdAngle', Vector3, queue_size=10)
    rospy.init_node('robot_manipulator_teleop', anonymous=True)
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
    message = Vector3()
    global M1
    global M2
    global M3
    message.x=M1
    message.y=M2
    message.z=M3
    while not rospy.is_shutdown():

        
        

    # pub.publish(message)

       # Press 'n Release  letras: (j, l) servo 1 izq derecha; (i, k) servo 2 arriba abajo; (u, o) servo 3 abre cierra

        def on_press(key):
            global M1
            global M2
            global M3

            try:

                # rospy.loginfo(key.char)
                # key.char
                if key.char == 'l':
                    x=M1-angle
                    if (x) < 45:
                        M1=50
                    else:
                        M1 -=angle
                    
                    message.x = M1
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'j':
                    x=M1+angle
                    if (x) > 135:
                        M1=130
                    else:
                        M1 +=angle
                    message.x = M1
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'k':
                    x=M2-angle
                    if (x) < 0:
                        M2=5
                    else:
                        M2 -=angle
                    
                    message.y = M2
                    
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'i':
                    x=M2+angle
                    if (x) > 90:
                        M2=85
                    else:
                        M2 +=angle
                    
                    message.y = M2
                    
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'u':
                    x=M3-angle
                    if (x) < 0:
                        M3=5
                    else:
                        M3 -=angle
                    
                    message.z = M3
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                elif key.char == 'o':
                    x=M3+angle
                    if (x) > 90:
                        M3=85
                    else:
                        M3 +=angle
                    
                    message.z = M3
                    pub.publish(message)

                    lista.append(str(key.char))
                    #print("lista: ", lista)
                    rospy.loginfo(message)

                else:
                    None

                np.savetxt('lista.txt', lista, fmt="%s")

            except:

                pass
                rospy.loginfo('malo')

        def on_release(key):

            #
            try:
                if key.char == 'j':

                    lista.append('*')
                    #print("lista: ", lista)

                elif key.char == 'l':

                    lista.append('*')
                    #print("lista: ", lista)

                elif key.char == 'k':

                    lista.append('*')
                    #print("lista: ", lista)

                elif key.char == 'i':

                    lista.append('*')
                    #print("lista: ", lista)

                elif key.char == 'u':

                    lista.append('*')
                    #print("lista: ", lista)

                elif key.char == 'o':

                    lista.append('*')
                    #print("lista: ", lista)

                else:
                    None

                np.savetxt('lista.txt', lista, fmt="%s")

            except:
                pass
        #
        #

        # rospy.loginfo(message)
        rate.sleep()

        # Collect events until released
        with keyboard.Listener(on_press, on_release) as listener:
            listener.join()


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_manipulator_teleop()
    except rospy.ROSInterruptException:
        pass
