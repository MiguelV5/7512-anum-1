#Codigo de las celdas separadas del .ipynb

print("primer bloque")
x = 20

print("segundo bloque de prueba")
#shift + enter para ejecutar este bloque
#notar que es un mismo programa python, puedo volver a usar x del bloque anterior
print("variable x vale:", x) 
#notar que el numero en [] de la izquierda del bloque es el NUMERO DE EJECUCION correspondiente al bloque (por ejemplo, el primer bloque dice [15] porque su ejecución fue la numero 15 de TODA la notebook)

#shift + enter dos veces agrega automaticamente otro bloque abajo

#si quisiera reiniciar todas las ejecuciones, ir arriba a Kernel, Restart.


#Graficar

import numpy as np
import matplotlib.pyplot as plt

x = np.array([4,3,2,-2,-8])
f_x = np.array([1,4,9,16,25])

#ej grafica comparativa: dos plots en una misma figura
plt.figure(1)
plt.plot(x,f_x)
plt.plot(x,1/2*f_x)
plt.show()

#ej graficas separadas: las mismas plots de antes pero en figuras distintas
#plt.figure(2)
#plt.plot(x,f_x)
#plt.show()

#plt.figure(3)
#plt.plot(x,2*f_x)
#plt.show()



#más funcionalidades de las plots
plt.figure(4)

plt.plot(x, f_x,     label = 'gota 1',  color = 'green', linewidth = 5, linestyle = '--')
plt.plot(x, 1/2*f_x, label = 'gota 2',  color = 'red', linestyle= '-.')

plt.scatter(x, 1/2*f_x, color = 'blue') #marca solo los puntos que se le marcaron en la celda anterior al crear la variable del array del dominio x.

plt.legend() #para mostrar todas las configuraciones adicionales posteriores a "f_x" al crear las plots de arriba

plt.grid() #lineas guia

plt.title('Velocidad de gota al caer segun tiempo')
plt.xlabel('Velocidad [m/s]')
plt.ylabel('Tiempo [s]')

plt.xlim(-2,4) #limitar la grafica a un intervalo de los datos del dominio
plt.ylim(0,18) #limitar la grafica a un intervalo de los datos del eje y (imagen)

#plt.savefig('VelocidadDeGotaAlCaerGrafica.png') #Esto guarda la imagen en el mismo directorio de esta notebook
plt.show()



#Más funcionalidades de numpy

X = np.linspace(-np.pi, np.pi, 100) #crea un array de numpy con 100 muestras equidistantes entre sí desde -pi a pi
print(f"El tamaño de X es {X.size}")
#print(X)

COS = np.cos(X)
SIN = np.sin(X)

print(f"El tamaño de COS es {COS.size}") #Notar DE NUEVO que la base del dominio (al igual que en las celdas anteriores) debe tener la misma cantidad de elementos que las imagenes a graficar. 
#print(COS)

print(f"El tamaño de SIN es {SIN.size}")
#print(SIN)



#Subplots
plt.figure(5)
fig, matrix = plt.subplots(1,2) #se crea matriz de 1x2 para los plots, es decir más o menos: [plot0,plot1]

matrix[0].plot(X,COS) #se crea y se guarda el plot0 con la info del domino y la info de la imagen
matrix[1].plot(X,SIN) #lo mismo para el plot1
plt.show()

plt.figure(6) #otro ejemplo
fig, matrix = plt.subplots(2,1) #se crea matriz de 2x1 para los plots, es decir más o menos: [plot0]                                                                                                                        [plot1]
matrix[0].plot(X,COS) #se crea y se guarda el plot0 con la info del domino y la info de la imagen
matrix[1].plot(X,SIN) #lo mismo para el plot1
plt.show()

plt.figure(7) #otro ejemplo
fig, matrix = plt.subplots(2,2) #se crea matriz de 2x2 para los plots, es decir más o menos: [plot00,plot10]  (plot fil-col)                                                                                                [plot01,plot11]
matrix[0,0].plot(X,COS) #se crea y se guarda el plot00 con la info del domino y la info de la imagen
matrix[0,1].plot(X,SIN) #...
matrix[1,0].plot(X,-COS) #...
matrix[1,1].plot(X,-SIN) #...
plt.show()


plt.figure(5) #otro ejemplo con nombres
fig, matrix = plt.subplots(1,2) #se crea matriz de 1x2 para los plots
fig.suptitle('Funciones trigonometricas')

matrix[0].plot(X,COS) 
matrix[0].set_title('Coseno')

matrix[1].plot(X,SIN) 
matrix[1].set_title('Seno')
plt.show()



#Test posterior a instalacion de WSL
print("Test muy original")