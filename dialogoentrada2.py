import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit)
from PyQt6.QtCore import Qt;
from PyQt6.QtGui import QFont

class VentanaCuadroDialogo(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 350, 150)
        self.setWindowTitle("ISF12B - Campo con QMessageBox")
        self.configurarPantalla()
        self.show()

    def configurarPantalla(self):

        catalogue_label = QLabel("Autor Catálogo", self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont("Arial", 18))
        search_label = QLabel("Buscar el índice por un autor:", self)
        search_label.move(20, 40)

        author_label = QLabel("Nombre:", self)
        author_label.move(20, 74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(240, 24)
        self.author_edit.setPlaceholderText("Entrar nombre como: Jennifer Lopez")

        # Create the search QPushButton
        search_button = QPushButton("Search", self);
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors);

    def searchAuthors(self):
        file = "archivos/autoress.txt"
        try:
            with open(file, "r") as f:
                autores = [line.rstrip("\n") for line in f]
         
            if self.author_edit.text() in autores:
                QMessageBox.information(self, "Autor encontrado", "Autor encontrado en catálogo!", QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self,
                "Autor no fue encontrado",
                """<p>Autor no fue encontrado.</p>
                <p>¿Desea continuar?</p>""",
                QMessageBox.StandardButton.Yes | \
                QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No)
                if answer == QMessageBox.StandardButton.No:
                    print("Cerrar aplicación.")
                    self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error", f"""<p>Archivo no encontrado.</p>    <p>Error: {error}</p>
            Cerrar aplicación.""",
            QMessageBox.StandardButton.Ok)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VentanaCuadroDialogo()
    sys.exit(app.exec())