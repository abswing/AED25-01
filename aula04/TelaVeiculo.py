import sys
from PyQt5.QtWidgets import *

from Veiculo import Veiculo

class Telaveiculo(QMainWindow):

    def __init__(self , titulo = "tela de veiculo" ): 
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 303, 300)
        self.layout = QVBoxLayout()

        self.definirlayout()

    # implemantar o botao salvar
    
    container = QWidget()
    container.setLayout( self.layout)
    self.setCentralWidget( container )

    def definirlayout(self):
        self.lblModelo = QLabel("modelo: ")
        self.txtModelo = QLineEdit(self)
        self.lblAno = QLabel("Ano: ")
        self.txtAno = QLineEdit(self)

        self.layout.addWidget( self.lblModelo)
        self.layout.addWidget( self.txtModelo)
        self.layout.addWidget( self.lblAno)
        self.layout.addWidget( self.txtAno)
    

    def salvar(self):
        modelo = self.txtModelo.text()
        