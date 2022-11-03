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
        path = self.txt_caminho.text()
        path = path[1:len(path)-1]
        print(path)
        return path

    def generate_table(self):
        df = pd.read_csv(fr"{self.copy_path()}", encoding="UTF-8", sep=";")
        print(df)


app = QApplication(sys.argv)

window = Login()
window.show()

app.exec_()
