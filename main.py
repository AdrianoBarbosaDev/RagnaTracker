#Import models
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
)
from PySide6.QtGui import QFont
import sys

from PySide6.QtCore import Qt

from database.buscas_db import buscarPersonagens, buscarInstancias

class TrackerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG Tracker")
        self.setGeometry(100, 100, 600, 400)

        self.main_layout = QVBoxLayout()

        self.logo = QLabel("""
██████╗░░█████╗░░██████╗░███╗░░██╗░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝░████╗░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝███████║██║░░██╗░██╔██╗██║███████║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗██╔══██║██║░░╚██╗██║╚████║██╔══██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚██████╔╝██║░╚███║██║░░██║░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
        self.logo.setFont(QFont("Courier", 8))
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(True)
        self.main_layout.addWidget(self.logo)

        # Botões
        self.btn_personagens = QPushButton("1 - Personagens")
        self.btn_personagens.clicked.connect(self.exibirPersonagens)

        self.btn_instancias = QPushButton("2 - Instâncias")
        self.btn_instancias.clicked.connect(self.exibirInstancias)

        self.btn_sair = QPushButton("3 - Sair")
        self.btn_sair.clicked.connect(self.close)

        self.main_layout.addWidget(self.btn_personagens)
        self.main_layout.addWidget(self.btn_instancias)
        self.main_layout.addWidget(self.btn_sair)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.main_layout.addWidget(self.output)

        self.setLayout(self.main_layout)

    def exibirPersonagens(self):
        personagens = buscarPersonagens()
        if personagens:
            texto = "\n".join([f"{p['id']} - {p['nome']} ({p['classe']}, nível {p['nivel']})" for p in personagens])
        else:
            texto = "Nenhum personagem encontrado."
        self.output.setPlainText(texto)

    def exibirInstancias(self):
        instancias = buscarInstancias()
        if instancias:
            texto = "\n".join([f"{i['id']} - {i['nome']} (nível {i['nivel']})" for i in instancias])
        else:
            texto = "Nenhuma instância encontrada."
        self.output.setPlainText(texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TrackerGUI()
    gui.show()
    sys.exit(app.exec())
