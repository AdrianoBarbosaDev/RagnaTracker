# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
# )
# from PySide6.QtGui import QKeySequence, QKeyEvent
# from PySide6.QtCore import Qt

# from ui.janela_teste import JanelaPrincipal

#Import models
from models.instancia import Instancia, instancas
from models.personagem import personagem, personagens

import sys



# app = QApplication(sys.argv)

# window = QWidget();
# window.show();

# app.exec();

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = JanelaPrincipal()
#     window.show()
#     sys.exit(app.exec())

def startTracker():
    print("""
██████╗░░█████╗░░██████╗░███╗░░██╗░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝░████╗░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝███████║██║░░██╗░██╔██╗██║███████║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗██╔══██║██║░░╚██╗██║╚████║██╔══██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚██████╔╝██║░╚███║██║░░██║░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
    
    print ("1 - Personagens")
    print("2 - Instâncias")
    print("3- Sair")

    opcaoEscolhida = input("Escolha uma opção: ")

    if(int(opcaoEscolhida) == 1):
        print(personagens)
    elif(int(opcaoEscolhida) == 2 ):
        print(instancas)
    else:
        print("Saindo..")

    

    
    

if __name__ == "__main__":
    startTracker()