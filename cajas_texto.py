import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, 
    QLabel)
from PyQt6.QtCore import Qt

class VentanaCheckbox(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializarPantalla()

    def inicializarPantalla(self):
        self.setGeometry(100, 100, 350, 150)
        self.setWindowTitle("Ejemplo uso de los componentes QCheckbox")
        self.configurarPantalla()
        self.show()

    def configurarPantalla(self):
        rotulo_principal = QLabel("Cuales materias va a ver a parte de esta? (Seleccione todas las requeridas)", self)
        rotulo_principal.setWordWrap(True)
        rotulo_principal.move(20, 10)
        
        #configurar checkboxes
        opcion_aplicaciones_web = QCheckBox("Aplicaciones Web I", self) 
        opcion_aplicaciones_web.move(40, 60)
        opcion_aplicaciones_web.toggled.connect(self.validarCheckboxSeleccionado)

        opcion_sistemas_operativos = QCheckBox("Sistemas Operativos", self) 
        opcion_sistemas_operativos.move(40, 80)   
        opcion_sistemas_operativos.toggled.connect(self.validarCheckboxSeleccionado)

        opcion_auditoria_software = QCheckBox("Auditoria de Software", self) 
        opcion_auditoria_software.move(40, 100)   
        opcion_auditoria_software.toggled.connect(self.validarCheckboxSeleccionado)

    def validarCheckboxSeleccionado(self, checked): 
        sender = self.sender()
        if checked:
            print(f"{sender.text()} seleccionado.")
        else:
            print(f"{sender.text()} no seleccionado.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaCheckbox()
    sys.exit(app.exec())