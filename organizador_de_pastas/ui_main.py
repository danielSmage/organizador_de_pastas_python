# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_organizador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imagens_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMaximumSize(QSize(500, 400))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.label_fundo1 = QLabel(self.centralwidget)
        self.label_fundo1.setObjectName(u"label_fundo1")
        self.label_fundo1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_fundo1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_fundo1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_arquivos = QLineEdit(self.frame)
        self.lineEdit_arquivos.setObjectName(u"lineEdit_arquivos")
        self.lineEdit_arquivos.setMinimumSize(QSize(0, 25))
        self.lineEdit_arquivos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_arquivos)

        self.pushButton_abrir = QPushButton(self.frame)
        self.pushButton_abrir.setObjectName(u"pushButton_abrir")
        self.pushButton_abrir.setEnabled(True)
        self.pushButton_abrir.setMinimumSize(QSize(120, 25))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.pushButton_abrir.setFont(font)
        self.pushButton_abrir.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_abrir.setStyleSheet(u"QPushButton{\n"
"	border-top-right-radius: 15px;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(129, 129, 129);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_abrir)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pushButton_organizar = QPushButton(self.frame)
        self.pushButton_organizar.setObjectName(u"pushButton_organizar")
        self.pushButton_organizar.setMinimumSize(QSize(200, 30))
        self.pushButton_organizar.setFont(font)
        self.pushButton_organizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_organizar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(129, 129, 129);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_organizar)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_fundo1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/pastas/icone100.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.lineEdit_arquivos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione o diret\u00f3rio", None))
        self.pushButton_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_2.setText("")
        self.pushButton_organizar.setText(QCoreApplication.translate("MainWindow", u"Organizar", None))
        self.label_3.setText("")
    # retranslateUi

