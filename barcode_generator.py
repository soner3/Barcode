import os
import sys
import random
from spire.barcode import BarcodeSettings, BarCodeType, BarCodeGenerator
from PyQt5.QtGui import QIcon, QPixmap
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

# CSS Style Code für die Widgets
STYLE = """
    QPushButton {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 18pt;
        color: black;
    }

    QTextEdit{
        font-family: Arial, Helvetica, sans-serif;
        font-size: 14pt;
        color: black;
    }
    
    QLabel {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 18pt;
        color: black;
    }

"""


# Erstellt den Barcode
class Barcode(QWidget):

    def __init__(self):

        # Fenster erstellen
        super().__init__()

        # Fenster bearbeiten
        self.setWindowTitle("Barcode Generator")
        self.setMinimumSize(1100, 900)
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
        self.__description.setFixedHeight(180)
        self.__description.setFixedWidth(400)
        self.__description.setAlignment(Qt.AlignCenter)
        self.__description.setWordWrap(True)
        self.__delete.setFixedHeight(100)
        self.__delete.setCursor(Qt.PointingHandCursor)
        self.__generate_barcode_button.setFixedHeight(100)
        self.__generate_barcode_button.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet(STYLE)

        # Barcode Komponenten und Format erstellen
        self.__barcode_settings = BarcodeSettings()
        self.__barcode_settings.Type = BarCodeType.EAN13
        self.__barcode_settings.ImageWidth = 500.0
        self.__barcode_settings.ImageHeight = 150.0
        self.__barcode_image = None
        self.__barcode_nummer = ""

        # Barcode Speicher Pfad
        self.__speicher_pfad = "BarcodeDirectory"

        # Fenster zeigen
        self.show()

    # Generieren des Barcodes
    def generate(self):
        # Directory erstellen, wenn nicht existiert
        if not os.path.exists(self.__speicher_pfad):
            os.mkdir(self.__speicher_pfad)

        # Barcodenummer erstellen
        for i in range(13):
            i = str(random.randint(0, 9))
            self.__barcode_nummer += i

        # Barcode erstellen und speichern
        self.__barcode_settings.Data = self.__barcode_nummer
        self.__barcode_generator = BarCodeGenerator(self.__barcode_settings)
        self.__barcode_image = self.__barcode_generator.GenerateImage()
        with open(f"BarcodeDirectory/{self.__barcode_nummer}.png", "wb") as f:
            f.write(self.__barcode_image)

        # Barcode Bild im Textfeld eingeben
        html = f"BarcodeDirectory/{self.__barcode_nummer}.png"
        self.__text_area.setHtml(
            f'<div style="text-align: center;"><img src="{html}" /></div>'
        )

    # Speichern des Barcodes
    def save(self):
        if self.__text_area == "":
            return
        else:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Barcode speichern", f"BarcodeDirectory/{self.__barcode_nummer}.png", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp);;GIF Files (*.gif)", options=options)
            if file_path:
                with open(f"{file_path}", "wb") as f:
                    f.write(self.__barcode_image)


    # Barcode Löschen
    def delete_all(self):
        self.__text_area.clear()


# Starten des Programms
if __name__ == "__main__":
    app = QApplication(sys.argv)
    qrCode = Barcode()
    qrCode.show()
    sys.exit(app.exec_())
