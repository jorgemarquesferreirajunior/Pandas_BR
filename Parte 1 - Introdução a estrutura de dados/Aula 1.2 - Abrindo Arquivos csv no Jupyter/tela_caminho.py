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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_caminho = QLineEdit(Form)
        self.txt_caminho.setObjectName(u"txt_caminho")
        self.txt_caminho.setMinimumSize(QSize(470, 30))
        self.txt_caminho.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_caminho)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.btn_enviar_caminho = QPushButton(Form)
        self.btn_enviar_caminho.setObjectName(u"btn_enviar_caminho")
        self.btn_enviar_caminho.setMinimumSize(QSize(150, 50))
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

        self.horizontalLayout.addWidget(self.btn_enviar_caminho)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.btn_tabela = QPushButton(Form)
        self.btn_tabela.setObjectName(u"btn_tabela")
        self.btn_tabela.setMinimumSize(QSize(150, 50))
        self.btn_tabela.setFont(font)
        self.btn_tabela.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.btn_tabela)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txt_caminho.setPlaceholderText(QCoreApplication.translate("Form", u"caminho", None))
        self.label.setText("")
        self.btn_enviar_caminho.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.btn_tabela.setText(QCoreApplication.translate("Form", u"TABELA", None))
        self.label_4.setText("")
    # retranslateUi

