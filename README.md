# ReadMe Grupo 5 Robótica - Uniandes

## Generalidades y estructura de fucionamiento

Se tienen 9 códigos necesarios para la funcionalidad completa del robot:

- teleop
- central
- interface
- player
- manipulador teleop
- mainpulador central
- manipulador interface
- manipulador planner
- manipulator camara

### Nodo Teleop: 
Nodo en el que se especifican las velocidades deseadas para el movimiento del robot. Se pide al usuario ingresar velocidad lineal y angular.
Dichas velocidades deben ser dadas en cm/s y tener el mismo número de dígitos (1 o 2). i.e.: Si la velocidad angular es 20, entonces la velocidad angular podrá ser 10 pero no 8. De igual manera, se espera que estas velocidades sean números enteros. De forma adicional, este nodo percibe las teclas que se precionan por teclado y envía la información correspondiente para que el robot se mueva con configuración de teclas 'WASD'.
  
### Nodo Central:
Este nodo es el encargado de recibir y procesar las velocidades que anteriormente se ingresaron en el nodo teleop. Este nodo convierte las velocidades de cm/s a valores de porcentage de ancho de pulso de manera que se pueda determinar la velocidad de los motores del robot, permitiendo el movimiento del mismo en 4 direcciones: lineal (teclas 'WS') y giro sobre su propio eje (teclas 'AD'). Este nodo también procesa el avance y dirección del robot en función de las velocidades y el tiempo que el robot se está moviendo, permitiendo conocer la posición del mismo respecto a su posición inicial. Este nodo transmite el valor correspondiente ala posición del robot.

### Nodo Interface:
En este nodo se recibe información de la posición del robot y se genera una interfaz que permite ver el movimiento del mismo en tiempo real. Este nodo también guarda un arreglo con las velocidades lineal y angular ingresadas en el nodo Teleop junto con las posiciones registradas en un archivo .txt con el objetivo de poder replicar el recorrido realizado posteriormente.


### Nodo Player y Client:
El nodo "Client" recibe por parámetro un arreglo con las velocidades lineal y angular junto con los movimientos ingresados en el nodo "Teleop" para el movimiento del robot. Este arreglo, por facilidad, es el obtenido del nodo "Interfaz". El nodo lee los valores del arreglo y envía un mensaje tipo twist por un tópico configurado, simulando ser el noto "Teleop".

El nodo "player", que funciona como servicio del nodo "Client", recibe el mensaje enviado por "Client" y realiza el movimiento correspondiente. De esta forma, los nodos "Client" y "Player" permiten replicar de manera autónoma un recorrido previamente realizado desde el nodo "Teleop".

### Nodo Manipulador Teleop:
De manera similar al funcionamiento del _Nodo Teleop_, este nodo permite modificar de manera remota la posicoń del end-effector del manipulador. Este nodo pregunta por medio de imputs la velocidad de cada uno de los joints que componen el brazo; el valor ingresado será tratado como una variación en el ángulo de cada uno de los joints. Los cambios en la posición se manipularán por teclado, utilizando la configuración _i,j,k,l_ para movimientos verticales y horizontales, adicionalmente se tienen las teclas _u,o_ que permiten accionar el end-effector.

### Nodo Manipulador Central:
Este nodo recibe los ángulos deseados para cada uno de los servos que forman cada uno de los joints del manipulador. Teniendo los ángulos actuales de los joints, este nodo calcula las posiciones _[x, y, z]_.

### Nodo Manipulador Interface:
Este nodo permite visualizar en una grilla 3D el recorrido realizado por el end-effector. Esta interfaz permite poner un título a la gráfica realizada, guardarla como un archivo tipo .png y adicionalmente permite pausar la visualización del recorrido de manera que si se pulsa este botón, la gráfica dejará de registrar el recorrido a pesar del movimiento del manipulador. Dicho nodo recibe la posición del end-effector que son enviadas desde en _Nodo Manipulador Central_.

### Nodo Manipulador Panner:

Este nodo recibe una posición deseada para el end-effector y por medio de cinemática inversa calcula los ángulos necesarios en los servomotores para que así el _Nodo Manipulador Central_ sea capaz de llevar los servos a dicha posición.

### Nodo Manipulador Camara:

Este nodo utiliza reconocimiento de máscaras de color por computador (mediante una cámara) para identificar el pingpong con el color deseado. Una vez se identifica el pingpong deseado, se envía un valor de cambio de orientación en el plano _x,y_, esto buscando que el pingpong se quede centrado para así, proceder a accionar el segundo joint en conjunto con el end-effector y así poder recoger la bola.



## Consideraciones:

- Recuerde ingresar valores de velocidad (lineal y angular) con el mismo número de dígitos.
- Tenga en cuenta que los valores de velocidad no deben tener más de 2 dígitos.
- Tenga presente que las velocidades lineal y angular máximas del robót son 7 y 8 respectivamente. Si se ingresan valores mayores a los mencionados anteriormente, se tomarán como ingresados los valores máximos.
- Tenga presente que el joint que se mueve en el plano _x,y_ tiene un rango de acción de 45 a 135 grados y el joint que se mueve en el plano _y,z_ tiene un rango de acción entre 0 y 90 grados.

## Informe
En el contenido del repositorio se encuentra un archivo .pdf en el que se reporta el informe de desarrollo del taller 2, correspondiente a cinemática del cuerpo del robot. De igual manera, se encuentra un archivo .pdf en el que se reporta el informe de desarrollo del taller 3, correspondiente a la cinemática del manipulador.

