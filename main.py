from PyQt6 import QtWidgets , uic, QtGui,QtCore
import os
import sys
import shutil


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

main_ui = os.path.join(script_dir,"ui","mainwindow.ui") 

class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(main_ui,self)
        self.setWindowOpacity(0.95)

        self.botonA.clicked.connect(lambda: self.buscar())
        self.botonB.clicked.connect(lambda: self.ubicacion())
        self.botonM.clicked.connect(lambda: self.mover())
        
        
        self.mover_2.clicked.connect(lambda: self.moverArchivos())
        self.cancelar.clicked.connect(lambda: self.cancelarboton())
        self.mensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
    def buscar(self):
        buscarpath = QtWidgets.QFileDialog.getExistingDirectory(self, "selecciona una carpeta :")
        if buscarpath:
            self.archivos.setText(buscarpath)
    
    def ubicacion(self):        
        buscarpath = QtWidgets.QFileDialog.getExistingDirectory(self, "selecciona una carpeta :")
        if buscarpath:
            self.buscardir.setText(buscarpath)
    def mover(self):
        buscarpath = QtWidgets.QFileDialog.getExistingDirectory(self, "selecciona una carpeta :")
        if buscarpath:
            self.moverdir.setText(buscarpath)
    
    def moverArchivos(self):
        archi = self.archivos.text().rstrip()
        donde = self.buscardir.text().rstrip()
        movera = self.moverdir.text().rstrip()
        if archi != "" and donde != "" and movera != "":
            self.moverAction(archi,donde,movera)   
        else:
            self.mensaje.setText("Ingrese ubicaciones validas.")

    def moverAction(self,archi,donde,movera):
        rojo = QtGui.QColor(235,64,64)
        verde = QtGui.QColor(0,190,0)
        archelist = os.listdir(archi)
        try:
            for i in archelist:
                i = i.strip()
                z = i+".zip"
                x = i+".7z"
                y = i+".rar"
                if z in os.listdir(donde):
                    ruta_origen = os.path.join(donde,z)
                    shutil.move(ruta_origen,movera)
                    self.textEdit.setTextColor(verde)
                    self.textEdit.append(f"Exito : {i}/n")
                elif x in os.listdir(donde):
                    ruta_origen = os.path.join(donde,x)
                    shutil.move(ruta_origen,movera)
                    self.textEdit.setTextColor(verde)
                    self.textEdit.append(f"Exito : {i}")
                elif y in os.listdir(donde):
                    ruta_origen = os.path.join(donde,y)
                    shutil.move(ruta_origen,movera)
                    self.textEdit.setTextColor(verde)
                    self.textEdit.append(f"Exito : {i}")
                else:
                    self.textEdit.setTextColor(rojo)
                    self.textEdit.append(f"Alerta : Archivo {i} no fue encontrado.")
                self.mensaje.setText(f"Archivos Trasladados a {movera}.")
        except Exception as e:
            self.mensaje.setText(f"Ingrese Ubicaciones validas. Error:{e}")
    def cancelarboton(self):
        self.close()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
    