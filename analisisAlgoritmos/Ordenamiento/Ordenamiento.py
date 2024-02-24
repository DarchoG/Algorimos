from IPython.display import clear_output
import matplotlib.pyplot as plt
import numpy as np
import random
import time

print("--- Actividad 2 ----");

Multiplicador = int(input("\nIngrese en número entero la cantidad de veces que desea evaluar los datos en base a 1000: "))

print("\nDato recibido, espere unos momentos.")


Tiempos = []
#Multiplicador = 1 # En base 1000

Cantidad = [i for i in range(50, 1000 * Multiplicador + 1, 50)]

def generarDatos(n):

    valores = [] #Costo: Valor Elemental 1

    for i in range (n): #Costo: Valor Dependiente n

      valores.append(random.random()) #Costo: 1 * n

    return valores;

def Ordenar(N, M):

    if(N > 1000 * Multiplicador): #Caso base

      M += 1

      Ordenar(50, M);

      return;

    if(M > 10):

      return;

    Datos = generarDatos(N)

    Inicio = time.time(); #Return the time in seconds since the epoch as a floating point number.
    #Epoch hace referencia a 1 Enero de 1970 por lo tanto retorna el valor en segundos desde ese dia, de tal manera que es necesario calcular la diferencia de tiempo en dos puntos para obtener el tiempo de ejecución.

    for i in range (len(Datos)): #Itera n veces la lista, valor dependiente

      Minimo = Datos[i]; #Seleccionar el valor minimo para tomarlo como referencia.
      Indice = 0;
      Bandera = True;

      for j in range (i, len(Datos)): #Iterar N(N - i)

        if(Minimo >= Datos[j]): #Actualiza el valor minimo en cada iteración del arrelgo incial

          Indice = j;
          Minimo = Datos[j];
          Bandera = False;

      if(not(Bandera)): #Solamente intercambiar en caso de encontrar valor menor

        Auxiliar = Datos[i];
        Datos[i] = Datos[Indice];
        Datos[j] = Auxiliar;

    #Costo: (N + 7) * ((N - i) + 4), ignoranado contantes (N)*(N - i), por lo tanto N^2

    Final = time.time();
    Tiempo = Final - Inicio;

    Tiempos.append(Tiempo);

    Ordenar(N + 50, M); #Recursividad

Ordenar(50, 0);

fig, ax = plt.subplots();

k = 0

for i in range(10):

  Auxiliar = [];

  for j in range(20 * Multiplicador):

    Auxiliar.append(Tiempos[j + k])

  k += 20 * Multiplicador
  ax.plot(Cantidad, Auxiliar, label='Línea' + str(i + 1))
  ax.legend()

clear_output()
print("Tiempos de ejecución obtenidos para {} elementos".format(Multiplicador * 1000))
print('\n')

plt.title('Tiempo de ejecución')
plt.xlabel('Cantidad')
plt.ylabel('Tiempo / s')
plt.show();
