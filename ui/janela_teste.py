from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtGui import QKeySequence, QKeyEvent
from PySide6.QtCore import Qt

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste de multiescolha")
        self.setFixedSize(300, 200)

        self.label = QLabel("Use Tab para navegar e Enter para selecionar")
        self.botao1 = QPushButton("Opção 1")
        self.botao2 = QPushButton("Opção 2")
        self.botao3 = QPushButton("Opção 3")

        # Linka os botões a janela
        self.botao1.clicked.connect(lambda: self.mostrar_opcao("Opção 1"))
        self.botao2.clicked.connect(lambda: self.mostrar_opcao("Opção 2"))
        self.botao3.clicked.connect(lambda: self.mostrar_opcao("Opção 3"))

        # Config Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao1)
        layout.addWidget(self.botao2)
        layout.addWidget(self.botao3)
        self.setLayout(layout)


        # Começa com o botao1 focado
        self.botao1.setFocus()

    def mostrar_opcao(self, texto):
        self.label.setText(f"Selecionado: {texto}")
