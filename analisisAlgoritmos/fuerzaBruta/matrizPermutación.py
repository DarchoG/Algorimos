import pandas as pd
#Experimentacion

#Generar el total de las combinaciones de los booleanos acorde a la formula 2^n
#En mi función recursivo paso la iteración de la función actual
#Para determinar si es true o false en orden de obtener todos los posibles resultados realizo la formula 2^n/2 en base a su posición mas o menos significativa
#/2 Es porque tengo dos estados posibles unicamente, finalmente realizo la división de mi iteración entre n y asigno los pares para true y los impares para false
#La division tiene que ser entera y no generar parte decimal usar // if == 0 caso especial

# Especifica la ruta del archivo Excel
archivo_excel = "datos.xlsx"

# Lee el archivo Excel en un DataFrame de pandas
#df = pd.read_excel(archivo_excel)

# Almacenar en memoria temporal las columnas
#Posiciones = df['A'].values
#Referencias = df['B'].values
#Alternar = df['C'].values

def Boolean(Booleanos, Iteracion):

  for i in range(len(Booleanos)):

      pass;

    #Iteracion


#def Combinaciones(Objetos, Booleanos, Iteracion):

    #pass;

def permutaciones(N):

  Lista = [];

  for i in range(2**N):

    Auxiliar = [];

    for j in range(N -1, -1, -1):

      Posicion = (2**j); #Tasa Cambio

      if(i == 0):

          Auxiliar.append(0);
          continue;

      Resultado = (i + Posicion) // Posicion; #Paridad  0 mod 2 = 0
      Paridad = Resultado % 2;

      if(Paridad == 1):
        #Posicion Impar
        Auxiliar.append(0);
      else:
        Auxiliar.append(1);

    Lista.append(Auxiliar);

  Lectura(Lista);

def Lectura(Lista):

  for i in range(len(Lista)):

      print(Lista[i]);

def Recorrido(Lista, Longitud, tasaRecorrido):

  Auxiliar = [];

  for i in range(Longitud, tasaRecorrido, len(Lista)):

    Cadena = "";

    for j in range(i, tasaRecorrido, Longitud):

      Cadena += Lista[j]

    Auxiliar.append(Cadena);

  return Auxiliar;

#Test = "ATGCCACTCTA"
#Recorrido(Test, 3, 2)
Test(5);
