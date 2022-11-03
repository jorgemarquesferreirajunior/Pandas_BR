# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_caminho.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(541, 383)
        self.txt_caminho = QLineEdit(Form)
        self.txt_caminho.setObjectName(u"txt_caminho")
        self.txt_caminho.setGeometry(QRect(40, 50, 471, 31))
        self.txt_caminho.setAlignment(Qt.AlignCenter)
        self.btn_enviar_caminho = QPushButton(Form)
        self.btn_enviar_caminho.setObjectName(u"btn_enviar_caminho")
        self.btn_enviar_caminho.setGeometry(QRect(190, 160, 151, 51))
        font = QFont()
        font.setPointSize(16)
        self.btn_enviar_caminho.setFont(font)
        self.btn_enviar_caminho.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 20px	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txt_caminho.setPlaceholderText(QCoreApplication.translate("Form", u"caminho", None))
        self.btn_enviar_caminho.setText(QCoreApplication.translate("Form", u"Enviar", None))
    # retranslateUi

