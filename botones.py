import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QPushButton)
from PyQt6.QtCore import Qt

class VentanaBotones(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarVentana()

    def inicializarVentana(self):
        self.setGeometry(200, 200, 300, 150)
        self.setWindowTitle("Ejemplo utilizando botones: QPushButton")
        self.configurarPantalla()
        self.show()

    def configurarPantalla(self):
        self.cantidad_presiones_boton = 0
        self.rotulo_no_presionar = QLabel("No presionen el botón", self)
        self.rotulo_no_presionar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rotulo_no_presionar.move(60, 30) 
            
        self.boton = QPushButton("Presióneme", self)
        self.boton.move(80, 70)
        self.boton.clicked.connect(self.ejecutarEventoClick)

    def ejecutarEventoClick(self):
        self.cantidad_presiones_boton += 1

        if self.cantidad_presiones_boton == 1:
            self.rotulo_no_presionar.setText("Presionaste una vez")
        if self.cantidad_presiones_boton == 2:
            self.rotulo_no_presionar.setText("Presionaste dos veces")
            self.boton.adjustSize()
            self.boton.move(70, 70)
        if self.cantidad_presiones_boton == 3:
            print("Voy a finalizar el programa")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaBotones()
    sys.exit(app.exec())