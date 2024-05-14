import os
import sys
from spire.barcode import BarCodeGenerator
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QFileDialog,
)

STYLE = """
    * {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 18pt;
        color: black;
    }

"""


# Erstellt den Barcode
class BarcodeGenerator(QWidget):

    def __init__(self):

        # Fenster erstellen
        super().__init__()

        # Fenster bearbeiten
        self.setWindowTitle("Barcode Generator")
        self.setMinimumSize(1700, 1000)
        self.setWindowIcon(QIcon("Barcode.jpg"))

        # Widgets
        self.__text_area = QTextEdit()
        self.__save = QPushButton("Speichern")
        self.__description = QLabel(
            "Barcode kann erstellt werden und wird anschließend im Textfeld angezeigt."
        )
        self.__generate_barcode_button = QPushButton("Generate Barcode")
        self.__delete = QPushButton("Alle Felder Löschen")

        # Layout
        self.__vbox_left = QVBoxLayout()
        self.__vbox_right = QVBoxLayout()
        self.__hbox = QHBoxLayout(self)

        # Komponenten in die Linke VBox hinzufügen
        self.__vbox_left.addWidget(self.__text_area)
        self.__vbox_left.addWidget(self.__save)

        # Komponenten in die Rechte VBox hinzufügen
        self.__vbox_right.addWidget(self.__description)
        self.__vbox_right.addWidget(self.__generate_barcode_button)
        self.__vbox_right.addWidget(self.__delete)

        # VBoxen zur HBox hinzufügen
        self.__hbox.addLayout(self.__vbox_left)
        self.__hbox.addLayout(self.__vbox_right)

        # Connections
        self.__generate_barcode_button.clicked.connect(self.generate)
        self.__save.clicked.connect(self.save)
        self.__delete.clicked.connect(self.delete_all)

        # Style
        self.__text_area.setReadOnly(True)
        self.__save.setFixedHeight(100)
        self.__save.setCursor(Qt.PointingHandCursor)
        self.__description.setFixedHeight(150)
        self.__description.setFixedWidth(700)
        self.__description.setAlignment(Qt.AlignCenter)
        self.__description.setWordWrap(True)
        self.__delete.setFixedHeight(100)
        self.__delete.setCursor(Qt.PointingHandCursor)
        self.__generate_barcode_button.setFixedHeight(100)
        self.__generate_barcode_button.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(STYLE)

        # Fenster zeigen
        self.show()

    # Generieren des Barcodes
    def generate(self):
        pass
    
    # Speichern des Barcodes
    def save(self):
        pass
    
    # Barcode Löschen
    def delete_all(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qrCode = BarcodeGenerator()
    qrCode.show()
    sys.exit(app.exec_())
