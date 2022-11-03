import pandas as pd
from tela_caminho import Ui_Form

import sys
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.path = None
        self.setupUi(self)
        self.setWindowTitle("Caminho")
        self.btn_enviar_caminho.clicked.connect(self.copy_path)
        self.btn_tabela.clicked.connect(self.generate_table)

    def copy_path(self):
        self.path = self.txt_caminho.text()
        print(self.path)

    def generate_table(self):
        if self.path is not None:
            df = pd.read_csv(self.path, encoding="UTF-8", sep=";")
            print(df)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Erro de Caminho')
            msg.setIcon(QMessageBox.Information)
            msg.setText('Primeiro insira um caminho na LineEdit')


app = QApplication(sys.argv)

window = Login()
window.show()

app.exec_()