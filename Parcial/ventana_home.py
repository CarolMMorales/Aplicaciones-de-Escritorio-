#ventana2.py
#importar módulos necesarios

import sys
from PyQt6.QtWidgets import  QApplication, QWidget, QLabel;
from PyQt6.QtGui import QPixmap;
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit)
from PyQt6.QtCore import Qt;
from PyQt6.QtGui import QFont

class VentanaConImagen(QWidget):

    def __init__(self):
        super().__init__();
        self.iniciarUI();

    def iniciarUI(self):
        """ Configurar GUI aplicación """
        #self.setGeometry(100,100,300,400);
        self.setMinimumWidth(800)
        self.setFixedHeight(700)
        self.setWindowTitle("Parcial 1");
        self.configurarVentanaConImagen();
        self.show();


    def configurarVentanaConImagen(self):
        
        catalogue_label = QLabel("Style C&S", self)
        catalogue_label.move(450, 40)  
        catalogue_label.setFont(QFont("Arial", 18))
        
        mensaje_rotulo = QLabel(self);
        mensaje_rotulo.setText("Camisa");
        mensaje_rotulo.move(600,320);
        mensaje_rotulo.setFont(QFont("Arial", 13))
        imagen = "imagenes/camisa.png";

        try:
            with open(imagen):
                rotulo_uniempresarial = QLabel(self);
                pixmap = QPixmap(imagen).scaled(180,180);
                rotulo_uniempresarial.setPixmap(pixmap);
                rotulo_uniempresarial.move(600,120);

        except FileNotFoundError as error:
            print(f"Imagen no encontrada.\nError: {error}");

        mensaje_rotulo2 = QLabel(self);
        mensaje_rotulo2.setText("Hoodie");
        mensaje_rotulo2.move(250,320);
        mensaje_rotulo2.setFont(QFont("Arial", 13))
        imagen2 = "imagenes/hoodie.png";

        try:
            with open(imagen2):
                rotulo_uniempresarial = QLabel(self);
                pixmap = QPixmap(imagen2).scaled(180,180);
                rotulo_uniempresarial.setPixmap(pixmap);
                rotulo_uniempresarial.move(250,120);
                
        except FileNotFoundError as error:
            print(f"Imagen no encontrada.\nError: {error}");

        mensaje_rotulo3 = QLabel(self);
        mensaje_rotulo3.setText("Jeans");
        mensaje_rotulo3.move(250,580);
        mensaje_rotulo3.setFont(QFont("Arial", 13))
        imagen3 = "imagenes/jeans.png";

        try:
            with open(imagen2):
                rotulo_uniempresarial = QLabel(self);
                pixmap = QPixmap(imagen3).scaled(180,180);
                rotulo_uniempresarial.setPixmap(pixmap);
                rotulo_uniempresarial.move(250,390);
                
        except FileNotFoundError as error:
            print(f"Imagen no encontrada.\nError: {error}");

        mensaje_rotulo4 = QLabel(self);
        mensaje_rotulo4.setText("Vestido");
        mensaje_rotulo4.move(600,580);
        mensaje_rotulo4.setFont(QFont("Arial", 13))
        imagen4 = "imagenes/vestido.png";

        try:
            with open(imagen4):
                rotulo_uniempresarial = QLabel(self);
                pixmap = QPixmap(imagen4).scaled(180,180);
                rotulo_uniempresarial.setPixmap(pixmap);
                rotulo_uniempresarial.move(600,390);

        except FileNotFoundError as error:
            print(f"Imagen no encontrada.\nError: {error}");
            
        self.boton = QPushButton("Comprar Ariculo", self)
        self.boton.move(80, 70)
        


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv);
    ventana = VentanaConImagen();
    sys.exit(aplicacion.exec());
