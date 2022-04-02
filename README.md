# ReadMe Grupo 5 Robótica - Uniandes

## Generalidades y estructura de fucionamiento

Se tienen 4 códigos necesarios para la funcionalidad completa del robot:

- teleop
- central
- interface
- player

### Nodo Teleop: 
Nodo en el que se especifican las velocidades deseadas para el movimiento del robot. Se pide al usuario ingresar velocidad lineal y angular.
Dichas velocidades deben ser dadas en cm/s y tener el mismo número de dígitos (1 o 2). i.e.: Si la velocidad angular es 20, entonces la velocidad angular podrá ser 10 pero no 8. De igual manera, se espera que estas velocidades sean números enteros. De forma adicional, este nodo percibe las teclas que se precionan por teclado y envía la información correspondiente para que el robot se mueva con configuración de teclas 'WASD'.
  
### Nodo Central:
Este nodo es el encargado de recibir y procesar las velocidades que anteriormente se ingresaron en el nodo teleop. Este nodo convierte las velocidades de cm/s a valores de porcentage de ancho de pulso de manera que se pueda determinar la velocidad de los motores del robot, permitiendo el movimiento del mismo en 4 direcciones: lineal (teclas 'WS') y giro sobre su propio eje (teclas 'AD'). Este nodo también procesa el avance y dirección del robot en función de las velocidades y el tiempo que el robot se está moviendo, permitiendo conocer la posición del mismo respecto a su posición inicial. Este nodo transmite el valor correspondiente ala posición del robot.

### Nodo Interface:
En este nodo se recibe información de la posición del robot y se genera una interfaz que permite ver el movimiento del mismo en tiempo real. Este nodo también guarda un arreglo con las velocidades lineal y angular ingresadas en el nodo Teleop junto con las posiciones registradas en un archivo .txt con el objetivo de poder replicar el recorrido realizado posteriormente.

### Nodo Player:
El nodo "player" realiza un recorrido por un arreglo de datos ingresado por parámetro. Este arreglo deberá poseer tanto las velocidades tanto angular como lineal junto con las posiciones deseadas para el recorrido del robot. Para la integración de este nodo con el resto de nodos, se utiliza el arreglo guardado en el nodo Interface; esto permitirá que el robot realize de manera autónoma un recorrido que se ha realizado anteriormente de manera manual.


## Funcionamiento del código

## Consideraciones:

- Recuerde ingresar valores de velocidad (lineal y angular) con el mismo número de dígitos.
- Tenga en cuenta que los valores de velocidad no deben tener más de 2 dígitos.
- Tenga presente que las velocidades lineal y angular máximas del robót son 7 y 8 respectivamente. Si se ingresan valores mayores a los mencionados anteriormente, se tomarán como ingresados los valores máximos.

## Informe
En el contenido del repositorio se encuentra un archivo .pdf en el que se reporta el informe de desarrollo del taller 2.

