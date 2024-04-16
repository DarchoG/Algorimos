    def dikstraRecursivo(Grafo, Inicio):

        Diccionario = {};
        Visitados = set();
        
        for Nodo, Peso in Grafo:

            Diccionario[Nodo] = float("inf");

        Diccionario[Inicio].update(0);

        for Nodo, Peso in Grafo[Inicio]:
            camino(Grafo, Nodo, Peso, Visitados)


    def camino(Grafo, Direccion, Peso, Visitados):

        Visitados.append(Direccion);
        
        if(Direccion in Visitados):
            return;

        Copia = Visitados.copy();

        for Vertice, Arista in Grafo[Direccion]:
            
            camino(Grafo, Direccion, Peso, Visitados);

    def dikstra(Grafo, Inicio):

        Diccionario = {};
        Visitados = set();
        
        for Nodo, Peso in Grafo:

            Diccionario[Nodo] = float("inf");

        Diccionario[Inicio].update(0);

        for Nodo, Peso in Grafo[Inicio]:
            camino(Grafo, Nodo, Peso, Visitados)

    def camino(Grafo, Direccion, Peso, Visitados):

        Visitados.append(Direccion);
        
        if(Direccion in Visitados):
            return;

        Copia = Visitados.copy();

        for Vertice, Arista in Grafo[Direccion]:
            
            camino(Grafo, Vertice, Peso + Arista, Visitados);

    def dikstra(Grafo, Inicio, Final):

        Diccionario = {};
        
        for Nodo, Peso in Grafo:

            Diccionario[Nodo] = float("inf");

        Diccionario[Inicio].update(0);

        for Nodo, Peso in Grafo[Inicio]:
            camino(Grafo, Nodo, Peso, Visitados)
