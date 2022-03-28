# ReadMe Grupo 5 Robótica - Uniandes

## Generalidades y estructura de fucionamiento

Se tienen 3 códigos necesarios para la funcionalidad completa del robot:

- teleop
- central
- interface

### Nodo Teleop: 
Nodo en el que se especifican las velocidades deseadas para el movimiento del robot. Se pide al usuario ingresar velocidad lineal y angular.
Dichas velocidades deben ser dadas en [unidades] y tener el mismo número de dígitos (1 o 2). i.e.: Si la velocidad angular es 20, entonces la velocidad angular podrá ser 10 pero no 8. De igual manera, se espera que estas velocidades sean números enteros. De forma adicional, este nodo percibe las teclas que se precionan por teclado y envía la información correspondiente para que el robot se mueva con configuración de teclas 'WASD'.
  
### Nodo Central:
Este nodo es el encargado de recibir y procesar las velocidades que anteriormente se ingresaron en el nodo teleop. Este nodo convierte las velocidades de [unidades] a valores de porcentage de ancho de pulso de manera que se pueda determinar la velocidad de los motores del robot, permitiendo el movimiento del mismo en 4 direcciones: lineal (teclas 'WS') y giro sobre su propio eje (teclas 'AD'). Este nodo también procesa el avance y dirección del robot en función de las velocidades y el tiempo que el robot se está moviendo, permitiendo conocer la posición del mismo respecto a su posición inicial. Este nodo transmite el valor correspondiente ala posición del robot.

### Nodo Interface:
En este nodo se recibe información de la posición del robot y se genera una interfaz que permite ver el movimiento del mismo en tiempo real.







## Informe
Link de acceso a informe sobre desarrollo del taller 2  [solo lectura]

https://es.overleaf.com/read/qnnbpmcxjvyq

