import os 
import shutil

class Color:
    rojo = '\033[38;5;124m'
    verde = '\033[38;5;22m'
    reset = '\033[0m'

try:
    busrut = input("Directorio de busqueda :")
    nomarchi = input("Direccion del listado de archivos :")
    moverut = input("Ruta a :")
    
    archelist = open(nomarchi,"r")    
except Exception as e:
    print("Directorios invalidos",e)
try:
    for i in archelist:
        expa = i.find(" ")+1
        i = i[expa:]
        i = i.strip()
        z = i+".zip"
        x = i+".7z"
        if z in os.listdir(busrut):
            ruta_origen = os.path.join(busrut,z)
            print(Color.verde,ruta_origen,Color.reset)
            shutil.move(ruta_origen,moverut)
        elif x in os.listdir(busrut):
            ruta_origen = os.path.join(busrut,x)
            print(Color.verde,ruta_origen,Color.reset)
            shutil.move(ruta_origen,moverut)
        else:
            print(f"{Color.rojo}Archivo {i} no encontrado.{Color.reset}")
except Exception as e:
    print("Error de Procesamiento :" , e)