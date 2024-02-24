from IPython.display import clear_output
import matplotlib.pyplot as plt
import random
import time

Tiempos = []
N = list(range(0, 91, 3))
M = list(range(0, 31 , 1))

def Graficar():

    print("Espere unos momentos esto podria tardar hasta un minuto.")

    for i in range(len(N)):

      Lista_Inicial = GenerarDatos(N[i], 10, 99);
      Lista_Auxiliar = []
      Lista_Objetivo = GenerarDatos(M[i], 100, 999);
      Lista_Resultados = []

      Inicio = time.time();

      for j in range(len(Lista_Objetivo)):

        Resultado = Solve(Lista_Inicial,Lista_Auxiliar, Lista_Objetivo[j], 0);

      Final = time.time();
      Tiempo = Final - Inicio;
      Tiempos.append(Tiempo);

    clear_output()
    plt.plot(N, Tiempos)
    plt.title('Tiempo de ejecucion')
    plt.xlabel('Cantidad')
    plt.ylabel('Tiempo / s')
    plt.show();


def GenerarDatos(Cantidad, Minimo, Maximo):

    Lista_Random = []
    while len(Lista_Random) < Cantidad:
        Numero = random.randint(Minimo, Maximo)
        if Numero not in Lista_Random:
            Lista_Random.append(Numero)
    return Lista_Random

def Solve(Dimension, Usados, Objetivo, Elemento):

  Usados_Valores = Usados.copy()

  if(Elemento != 0):

    Usados_Valores.append(Elemento);

  if(Objetivo == 0):

      return Usados_Valores #Paso por valor

  if(Objetivo < 0):

      return None;

  for i in Dimension:

    if i in Usados_Valores:
      return None;

    Resultado = Solve(Dimension, Usados_Valores, Objetivo - i, i);
    if Resultado is not None:
      return Resultado

def Main():

  Control = True;

  while(Control):

    Lista_Inicial = GenerarDatos(20, 10, 99);
    Lista_Auxiliar = []
    Lista_Objetivo = GenerarDatos(10, 100, 999);
    Lista_Resultados = []

    for i in range(len(Lista_Objetivo)):

      Resultado = Solve(Lista_Inicial,Lista_Auxiliar, Lista_Objetivo[i], 0);

      if Resultado is not None:

        Lista_Resultados.append(Resultado)

    print("Datos con caso de pruebas obtenidos: \n")
    print("Lista_Inicial: {}".format(Lista_Inicial))
    print("Lista_Objetivo: {}".format(Lista_Objetivo))
    print("\nSubconjuntos Obtenidos: \n")
    for i in range(len(Lista_Resultados)):
      Contador = 0;

      for j in range(len(Lista_Resultados[i])):
        Contador += Lista_Resultados[i][j];

      print(Lista_Resultados[i], " = ", Contador);

    Decision = int(input("\nDigite 1 para volver a iterar el algoritmo pero con números aleatorios, en caso contrario introduzca cualquier dato: "))

    if(Decision != 1):
      Control = False
      Grafica = int(input("\n¿Desea ver la gráfica de tiempos? Introduzca 1, en caso omiso cualquiera número: "))

      if(Grafica == 1):

        clear_output()
        Graficar()

Main()
