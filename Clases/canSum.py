import matplotlib.pyplot as plt
from time import perf_counter

def canSumDinamico(Digito, Valores, Memoria = {}):

    if(Digito in Memoria):
        return Memoria[Digito];
    if(Digito == 0):
        return True;
    if(0 > Digito):
        return False;

    for i in Valores:

        Restante = Digito - i;
        if(canSumDinamico(Restante, Valores, Memoria)):
            #Memoria[Digito] = True; No es necesario retornar un caso de verdad porque se sabe que la operación es posible
            return True;

    Memoria[Digito] = False;
    return False;

def canSum(Digito, Valores):

    if(Digito == 0):
        return True;
    if(0 > Digito):
        return False;

    for i in Valores:

        Restante = Digito - i;
        if(canSum(Restante, Valores)):
            return True;

    return False;

Stock = []
programacionDinamica = []

Inicio = perf_counter();
print(canSum(7, [4, 3])); #True
Final = perf_counter();
Stock.append(Final - Inicio);

Inicio = perf_counter();
print(canSum(31, [6, 3, 9])); #False
Final = perf_counter();
Stock.append(Final - Inicio);

Inicio = perf_counter();
print(canSum(73, [15, 7, 2, 1])); #True
Final = perf_counter();
Stock.append(Final - Inicio);

Inicio = perf_counter();
print(canSum(250, [7, 14])); # False
Final = perf_counter();
Stock.append(Final - Inicio);

print("\n");

Inicio = perf_counter();
print(canSumDinamico(7, [4, 3]));
Final = perf_counter();
programacionDinamica.append(Final - Inicio);

Inicio = perf_counter();
print(canSumDinamico(31, [6, 3, 9]));
Final = perf_counter();
programacionDinamica.append(Final - Inicio);

Inicio = perf_counter();
print(canSumDinamico(73, [15, 7, 2, 1]));
Final = perf_counter();
programacionDinamica.append(Final - Inicio);

Inicio = perf_counter();
print(canSumDinamico(250, [7, 14]));
Final = perf_counter();
programacionDinamica.append(Final - Inicio);

print(Stock, programacionDinamica);

Ejercicio = ['A', 'B', 'C', 'D'];

Ancho = 0.35
indice = range(len(Ejercicio))

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Crear las barras para cada conjunto de valores
rects1 = ax.bar(indice, Stock, Ancho, label='Normal')
rects2 = ax.bar([i + Ancho for i in indice], programacionDinamica, Ancho, label='Programación Dinamica')

# Etiquetas, título y leyenda
ax.set_xlabel('Categorías')
ax.set_ylabel('Valores')
ax.set_title('Tiempo Ejecución')
ax.set_xticks([i + Ancho / 2 for i in indice])
ax.set_xticklabels(Ejercicio)
ax.legend()

# Mostrar el gráfico
plt.show()
