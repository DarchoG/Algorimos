def dijkstra (Grafo, Inicio):

    Pesos = {}
    Visitados = set();

    for nodo in Grafo:
        Pesos[nodo] = float("inf");
    
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

    return Pesos;

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print("Distancias más cortas desde el nodo", start_node)
print(dijkstra(graph, start_node))
