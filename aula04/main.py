import sys
from PyQt5.QtWidgets import *

from TelaVeiculo import Telaveiculo

app =   QApplication(sys.argv )
telaveiculo = Telaveiculo("cadastro de veiculo")

telaveiculo.show()

sys.exit(app.exec_() )