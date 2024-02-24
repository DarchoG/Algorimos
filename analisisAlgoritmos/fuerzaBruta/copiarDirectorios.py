import os
import shutil

def Copiar(Origen, Destino, Archivos):
    
    for i in range(len(Archivos)):
        
        #Copiar Archivos

        Archivo = Origen + "\\" + Archivos[i]
        
        print(Archivo)
        print(Destino)
        
        #shutil.copyfile(Archivo, Destino)

def Obtener(Valor):
    
    Validacion = False;
    
    while(not(Validacion)):
    
        Direccion = input("Ingrese Dirección {}: ".format(Valor))
        
        if(os.path.exists(Direccion)):
            
            return Direccion;
        
        else:
            
            print("\nDirección Invalida\n")
            
def  Copy(Origen, Destino):
    
    Archivos_Origen = []
    Archivos_Destino = []
    
    #print(isfile(Origen));
    
    for i in os.listdir(Origen): #Iterar total de la carpeta
    
        Archivos_Origen.append(i);
        
    for i in os.listdir(Destino):
        
        Archivos_Destino.append(i);
        
    Copiar(Origen, Destino, Archivos_Origen)
    Copiar(Destino, Origen, Archivos_Destino)
            
def Main():
    
    Origen = Obtener(1);
    Destino = Obtener(2);
    
    Copy(Origen, Destino)
    
    #No valida copias de archivos identicos, vuelve a iterar elementos que la primera carpeta ya dispone.
    
    #shutil.copyfile(Origen, Destino); #Requiere permisos de administrador para copiar
    #shutil.copyfile(Destino, Origen);
    
Main()
