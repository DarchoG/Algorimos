def dijkstra (Grafo, Inicio):

    Pesos = {}
    Caminos = {}
    Visitados = set();

    for nodo in Grafo:
        Pesos[nodo] = float("inf");
        Caminos[nodo] = None;
    
    Pesos[Inicio] = 0     

    while (len(Visitados) < len(Pesos)):

        pesoMinimo = float("inf");
        nodoMinimo = None;

        for Nodo in Grafo:

            if(Nodo not in Visitados and Pesos[Nodo] < pesoMinimo):

                pesoMinimo = Pesos[Nodo];
                nodoMinimo = Nodo;

        if (nodoMinimo == None):
            return Pesos;

        Visitados.add(nodoMinimo);

        for conexiones, costo in Grafo[nodoMinimo].items():

            distanciaActual = Pesos[nodoMinimo] + costo;

            if(distanciaActual < Pesos[conexiones]):

                Pesos[conexiones] = distanciaActual;
                Caminos[conexiones] = nodoMinimo

    return Pesos, Caminos;

def generarCaminos(Grafo, Nodo):
    Camino = [Nodo];
    while Grafo[Nodo] is not None:
        Nodo = Grafo[Nodo]
        Camino.append(Nodo);
    Camino.reverse();
    return Camino;

Grafo = {
    'A': {'B': 11, 'C': 43, 'E' : 12},
    'B': {'A': 13, 'C': 31, 'D': 22},
    'C': {'A': 43, 'B': 12, 'D': 1},
    'D': {'B': 51, 'C': 13},
    'E': {'A': 3, 'C' : 23}
}

Inicio  = 'A'
Pesos, Rutas = dijkstra(Grafo, Inicio)
print("Distancias más cortas desde el nodo", Inicio)
print(Pesos)
print()

for Elemento in Grafo:
    Camino = generarCaminos(Rutas, Elemento);
    print("Camino corto de ", Elemento, " : ", Camino)
