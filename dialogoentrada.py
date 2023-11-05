import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)
from PyQt6.QtCore import Qt;

class VentanaBotones(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMaximumSize(310, 130)
        self.setWindowTitle("Ejemplo QLineEdit")
        self.configurarPantalla()
        self.show()

    def configurarPantalla(self):
        QLabel("Por favor, escriban su nombre debajo.", self).move(70, 10)
        nombre_rotulo = QLabel("Nombre:", self)
        nombre_rotulo.move(20, 50)
        self.nombre_editar = QLineEdit(self)
        self.nombre_editar.resize(210, 20)
        self.nombre_editar.move(70, 50)
        boton_limpiar = QPushButton("Limpiar", self)
        boton_limpiar.move(140, 90)
        boton_limpiar.clicked.connect(self.clearText)
        aceptar_boton = QPushButton("OK", self)
        aceptar_boton.move(210, 90)
        aceptar_boton.clicked.connect(self.acceptText)

    def clearText(self):
        self.nombre_editar.clear()

    def acceptText(self):
        print(self.nombre_editar.text())
        self.close()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaBotones()
    sys.exit(app.exec())