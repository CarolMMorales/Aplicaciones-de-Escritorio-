#ventana_vacia.py
#importar módulos necesarios
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class VentanaVacia(QWidget):

    def __init__(self):
        """Constructor para la clase Ventana Vacia"""
        super().__init__();
        self.iniciarUI();

    def iniciarUI(self):
        """ Configurar la aplicación"""
        self.setGeometry(600,400,400,300);
        self.setWindowTitle("Bienvenidos UE AEI - ISF12A ");
        self.show();#muestra la ventana en la pantalla

#Ejecutar el programa
if __name__ == '__main__':
    app = QApplication(sys.argv);
    ventana = VentanaVacia();
    sys.exit(app.exec())
