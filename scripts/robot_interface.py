#!/usr/bin/env python3
from tkinter import Tk, Frame, Button, Label, ttk,Entry
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
import rospy
import tty
import sys
import termios
import keyboard
from std_msgs.msg import String
from geometry_msgs.msg import Twist

xr=[]
yr=[]

def callback(msg):
	
	x = round(msg.linear.x,4)
	y = round(msg.linear.y,4)
	xr.append(x)
	yr.append(y)

def robot_interface():

	rospy.init_node('robot_interface', anonymous=True)
	rospy.Subscriber('robot_position', Twist, callback)

def animate(i):
	ax.clear()
	ax.plot(xr,yr)
	

def guardar():
	print(nom.get())
	f=open('lista.txt','r')
	datos=f.read()
	lista_nueva=[]
	for i in datos:
		if i!='\n':
			lista_nueva.append(i)
	recorrido = []
	recorrido.append(lista_nueva[0]+lista_nueva[1])
	recorrido.append(lista_nueva[2]+lista_nueva[3])
	for j in range (2,len(lista_nueva)-2):
		recorrido.append(lista_nueva[j+2])
	print(recorrido)
	np.savetxt('/home/ubuntu/catkin_ws/src/mi_robot_5/results/'+nom.get()+'.txt',recorrido,fmt="%s")

def guardarGraf():
	plt.title(nomGraf.get())
	plt.savefig('/home/ubuntu/catkin_ws/src/mi_robot_5/results/'+nomGraf.get()+'.png')


def pausar():
	ani.event_source.stop()
	
#Creacion de ventana de interfaz
ventana = Tk()
ventana.geometry('950x650')
ventana.wm_title('Interfaz')
ventana.minsize(width=950, height=650)

#Color de la ventana
e1=Label(ventana,text="Nombre del archivo: ",bg="#50C878",fg="white" )
e1.pack(pady=5,expand=1)

nom=Entry(ventana)
nom.pack(pady=5,expand=1)

e2=Label(ventana,text="Nombre del gráfico: ",bg="#50C878",fg="white" )
e2.pack(pady=5,expand=1)

nomGraf=Entry(ventana)
nomGraf.pack(pady=5,expand=1)

frame = Frame(ventana, bg='#D7DBDD')
frame.pack(expand=1, fill='both')

fig, ax = plt.subplots(facecolor='#FFFFFF')
plt.title("Interfaz", color='black', size=16)


canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')



Button(frame, text="Guardar.txt",width=15,bg="#50C878",fg="white",command=guardar).pack(pady=5,side="left",expand=1)
 
Button(frame, text="Guardar gráfica",width=15,bg="#50C878",fg="white",command=guardarGraf).pack(pady=5,side="left",expand=1)
 
Button(frame, text="Pausar",width=15,bg="#50C878",fg="white",command=pausar).pack(pady=5,side="left",expand=1)
 
ani=animation.FuncAnimation(fig,animate,interval=1000)
canvas.draw()    
if __name__ == '__main__':
    robot_interface()
    ventana.mainloop()
