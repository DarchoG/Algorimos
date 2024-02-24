#include <bits/stdc++.h>
#include <vector>
using namespace std;

bool busquedaBinaria(vector<int>Arreglo, int Dato){
	
	int Inicio = 0;
	int Final = Arreglo.size() - 1;
	
	while(Final >= Inicio){
		
		int Mitad = (Final - Inicio)/2;
		
		if(Arreglo[Mitad] == Dato) return true;
		else if(Arreglo[Mitad] > Dato) Final = Mitad - 1;
		else Inicio = Mitad + 1;
			
	}
	
	return false;
	
}

void countingSort(vector<int>&Arreglo, int Maximo){
	
	vector <int> Output(Arreglo.size());
	vector <int> Counting(Maximo + 1);
	
	for (int i = 0; i < Counting.size(); i++) Counting[i] = 0;
	
	for (int i = 0; i < Arreglo.size(); i++) Counting[Arreglo[i]]++;
	
	for (int i = 1; i < Counting.size(); i++) Counting[i] += Counting[i - 1];
	
	for (int i= 0; i < Arreglo.size(); i++){
		
		Output[Counting[Arreglo[i]]] = Arreglo[i];
		Counting[Arreglo[i]]--;
	}
	
	for (int i = 0; i < Arreglo.size(); i++) Arreglo[i] = Output[i];
	
}

void generarArreglo(vector<int>&Arreglo, int Cantidad){
	
	srand(time(NULL));
	
	for (int i = 0; i < Cantidad; i++) Arreglo.push_back(rand () % Cantidad);
	
}

void imprimirArreglo(vector<int>Arreglo){
	
	for (int i = 0; i < Arreglo.size(); i++) cout << Arreglo[i] << " ";
	
	cout << endl << endl;
	
}

void merge(vector<int>&Arreglo, int Inicio, int Mitad, int Final){
	
	int i, j, k;
	
	int ElementosIzquierda = Mitad - Inicio + 1;
	int ElementosDerecha = Final - Mitad;
	
	vector<int>Izquierda(ElementosIzquierda);
	vector<int>Derecha(ElementosDerecha);
	
	for(i = 0; i < ElementosIzquierda; i++) Izquierda[i] = Arreglo[Inicio + i];
	for(i = 0; i < ElementosDerecha; i++) Derecha[i] = Arreglo[Mitad + i + 1];
	
	i = 0; j = 0; k = Inicio;
	
	while(i < ElementosIzquierda && j < ElementosDerecha){
		
		if(Izquierda[i] <=  Derecha[j]){
			
			Arreglo[k] = Izquierda[i];
			i++;
		}
		else{
			
			Arreglo[k] = Derecha[j];
			j++;	
		}
		k++;
	}
	
	while (i < ElementosIzquierda){
		
		Arreglo[k] = Izquierda[i];
		i++; k++;
	}
	
	while (j < ElementosDerecha){
		
		Arreglo[k] = Derecha[j];
		j++; k++;
		
	}
	
	
}

void mergeSort(vector<int>&Arreglo, int Inicio, int Final){
	
	if(Final > Inicio){
		
		int Mitad = Inicio + (Final - Inicio)/2;
		mergeSort(Arreglo, Inicio, Mitad);
		mergeSort(Arreglo, Mitad + 1, Final);
		merge(Arreglo, Inicio, Mitad, Final);	
		
	}
	
}

int main (){
	
	vector<int>Datos;
	Datos.push_back(3);
	Datos.push_back(-3);
	Datos.push_back(1);
	
	//generarArreglo(Datos, 1e4);
	mergeSort(Datos, 0, Datos.size() - 1);
	//countingSort(Datos, 1e4);
	//imprimirArreglo(Datos);
	
	cout << busquedaBinaria(Datos, 0);
	
	//cout << a;
	
	return 0;
}
