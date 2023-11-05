import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCheckBox;

class VentanaRotulo(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200,100,400,300);
        self.setWindowTitle("Rótulos en PyQt6 - ISF12B")

        label = QLabel("Colocación de un rótulo de estudiantes", self)
        label.setText("Danilo")
        fuente = label.font();
        fuente.setPointSize(30);
        label.move(0, 0)

        check1 = QCheckBox("ISF1O")
        diseno = QVBoxLayout()
        widgets = [check1, label];

        for w in widgets:
            diseno.addWidget(w)

        
        self.setLayout(diseno)
        self.show();



#Ejecutar el programa
app = QApplication(sys.argv);
ventana = VentanaRotulo();
sys.exit(app.exec())
