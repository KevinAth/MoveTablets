import os

try:
    path = input("Ingresa la ruta de la carpeta : ")
    nomtxt = input("Nombra al archivo resultante : ") + ".txt"
    archivo = open(nomtxt,"w")
    dirlec = os.listdir(path)
    print(dirlec)
except Exception as e:
    print("Directorio invalido" , e)
    
for num,ric in enumerate(dirlec):
    num = str(num+1)
    archivo.write(num+") "+ric+"\n")
    
    