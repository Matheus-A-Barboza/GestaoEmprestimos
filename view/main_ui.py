# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import view.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 668)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 120))
        self.widget.setStyleSheet(u"image: url(:/icon/icon.png);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_inicio = QWidget()
        self.tab_inicio.setObjectName(u"tab_inicio")
        self.verticalLayout_3 = QVBoxLayout(self.tab_inicio)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_inicio)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.label)

        self.btn_receber = QPushButton(self.tab_inicio)
        self.btn_receber.setObjectName(u"btn_receber")

        self.verticalLayout_3.addWidget(self.btn_receber)

        self.btn_emprestar = QPushButton(self.tab_inicio)
        self.btn_emprestar.setObjectName(u"btn_emprestar")

        self.verticalLayout_3.addWidget(self.btn_emprestar)

        self.label_2 = QLabel(self.tab_inicio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tb_emprestimos_ativos = QTableWidget(self.tab_inicio)
        if (self.tb_emprestimos_ativos.columnCount() < 4):
            self.tb_emprestimos_ativos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_emprestimos_ativos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_emprestimos_ativos.setObjectName(u"tb_emprestimos_ativos")
        self.tb_emprestimos_ativos.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tb_emprestimos_ativos)

        self.tabWidget.addTab(self.tab_inicio, "")
        self.tab_relatorio = QWidget()
        self.tab_relatorio.setObjectName(u"tab_relatorio")
        self.verticalLayout_4 = QVBoxLayout(self.tab_relatorio)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_data_inicial = QLabel(self.tab_relatorio)
        self.lbl_data_inicial.setObjectName(u"lbl_data_inicial")

        self.horizontalLayout.addWidget(self.lbl_data_inicial)

        self.txt_data_inicial = QLineEdit(self.tab_relatorio)
        self.txt_data_inicial.setObjectName(u"txt_data_inicial")

        self.horizontalLayout.addWidget(self.txt_data_inicial)

        self.lbl_data_final = QLabel(self.tab_relatorio)
        self.lbl_data_final.setObjectName(u"lbl_data_final")

        self.horizontalLayout.addWidget(self.lbl_data_final)

        self.txt_data_final = QLineEdit(self.tab_relatorio)
        self.txt_data_final.setObjectName(u"txt_data_final")

        self.horizontalLayout.addWidget(self.txt_data_final)

        self.btn_consultar_relatorio = QPushButton(self.tab_relatorio)
        self.btn_consultar_relatorio.setObjectName(u"btn_consultar_relatorio")

        self.horizontalLayout.addWidget(self.btn_consultar_relatorio)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tb_relatorio = QTableWidget(self.tab_relatorio)
        if (self.tb_relatorio.columnCount() < 3):
            self.tb_relatorio.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_relatorio.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tb_relatorio.setObjectName(u"tb_relatorio")

        self.verticalLayout_4.addWidget(self.tb_relatorio)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btn_exportar = QPushButton(self.tab_relatorio)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.horizontalLayout_5.addWidget(self.btn_exportar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_relatorio, "")
        self.tab_gestao = QWidget()
        self.tab_gestao.setObjectName(u"tab_gestao")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_gestao)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.coluna_esquerda = QWidget(self.tab_gestao)
        self.coluna_esquerda.setObjectName(u"coluna_esquerda")
        self.verticalLayout_6 = QVBoxLayout(self.coluna_esquerda)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.coluna_esquerda)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.lbl_nome_funcionario = QLabel(self.coluna_esquerda)
        self.lbl_nome_funcionario.setObjectName(u"lbl_nome_funcionario")

        self.verticalLayout_6.addWidget(self.lbl_nome_funcionario)

        self.txt_nome = QLineEdit(self.coluna_esquerda)
        self.txt_nome.setObjectName(u"txt_nome")

        self.verticalLayout_6.addWidget(self.txt_nome)

        self.lbl_cpf_funcionario = QLabel(self.coluna_esquerda)
        self.lbl_cpf_funcionario.setObjectName(u"lbl_cpf_funcionario")

        self.verticalLayout_6.addWidget(self.lbl_cpf_funcionario)

        self.txt_cpf = QLineEdit(self.coluna_esquerda)
        self.txt_cpf.setObjectName(u"txt_cpf")

        self.verticalLayout_6.addWidget(self.txt_cpf)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_editar_funcionario = QPushButton(self.coluna_esquerda)
        self.btn_editar_funcionario.setObjectName(u"btn_editar_funcionario")

        self.horizontalLayout_3.addWidget(self.btn_editar_funcionario)

        self.btn_adicionar_funcionario = QPushButton(self.coluna_esquerda)
        self.btn_adicionar_funcionario.setObjectName(u"btn_adicionar_funcionario")

        self.horizontalLayout_3.addWidget(self.btn_adicionar_funcionario)

        self.btn_remover_funcionario = QPushButton(self.coluna_esquerda)
        self.btn_remover_funcionario.setObjectName(u"btn_remover_funcionario")

        self.horizontalLayout_3.addWidget(self.btn_remover_funcionario)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tb_funcionarios = QTableWidget(self.coluna_esquerda)
        if (self.tb_funcionarios.columnCount() < 2):
            self.tb_funcionarios.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tb_funcionarios.setObjectName(u"tb_funcionarios")

        self.verticalLayout_6.addWidget(self.tb_funcionarios)


        self.horizontalLayout_2.addWidget(self.coluna_esquerda)

        self.coluna_direita = QWidget(self.tab_gestao)
        self.coluna_direita.setObjectName(u"coluna_direita")
        self.verticalLayout_5 = QVBoxLayout(self.coluna_direita)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.coluna_direita)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.lbl_nome_uniforme = QLabel(self.coluna_direita)
        self.lbl_nome_uniforme.setObjectName(u"lbl_nome_uniforme")

        self.verticalLayout_5.addWidget(self.lbl_nome_uniforme)

        self.txt_nome_2 = QLineEdit(self.coluna_direita)
        self.txt_nome_2.setObjectName(u"txt_nome_2")

        self.verticalLayout_5.addWidget(self.txt_nome_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_editar_uniforme = QPushButton(self.coluna_direita)
        self.btn_editar_uniforme.setObjectName(u"btn_editar_uniforme")

        self.horizontalLayout_4.addWidget(self.btn_editar_uniforme)

        self.btn_adicionar_uniforme = QPushButton(self.coluna_direita)
        self.btn_adicionar_uniforme.setObjectName(u"btn_adicionar_uniforme")

        self.horizontalLayout_4.addWidget(self.btn_adicionar_uniforme)

        self.btn_remover_uniforme = QPushButton(self.coluna_direita)
        self.btn_remover_uniforme.setObjectName(u"btn_remover_uniforme")

        self.horizontalLayout_4.addWidget(self.btn_remover_uniforme)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tb_uniforme = QTableWidget(self.coluna_direita)
        if (self.tb_uniforme.columnCount() < 1):
            self.tb_uniforme.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_uniforme.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        self.tb_uniforme.setObjectName(u"tb_uniforme")

        self.verticalLayout_5.addWidget(self.tb_uniforme)


        self.horizontalLayout_2.addWidget(self.coluna_direita)

        self.tabWidget.addTab(self.tab_gestao, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestao de Emprestimo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Emprestar ou Receber Uniforme</span></p></body></html>", None))
        self.btn_receber.setText(QCoreApplication.translate("MainWindow", u"Receber", None))
        self.btn_emprestar.setText(QCoreApplication.translate("MainWindow", u"Emprestar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Emprestimos Ativos</span></p></body></html>", None))
        ___qtablewidgetitem = self.tb_emprestimos_ativos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Funcionario", None));
        ___qtablewidgetitem1 = self.tb_emprestimos_ativos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF Funcionario", None));
        ___qtablewidgetitem2 = self.tb_emprestimos_ativos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Emprestimo", None));
        ___qtablewidgetitem3 = self.tb_emprestimos_ativos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Uniforme", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inicio), QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.lbl_data_inicial.setText(QCoreApplication.translate("MainWindow", u"Data Inicial", None))
        self.lbl_data_final.setText(QCoreApplication.translate("MainWindow", u"Data Final", None))
        self.btn_consultar_relatorio.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem4 = self.tb_relatorio.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nome Funcionario", None));
        ___qtablewidgetitem5 = self.tb_relatorio.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data Emprestimo", None));
        ___qtablewidgetitem6 = self.tb_relatorio.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data Devolu\u00e7\u00e3o", None));
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_relatorio), QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Funcionarios</span></p></body></html>", None))
        self.lbl_nome_funcionario.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_cpf_funcionario.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.btn_editar_funcionario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_adicionar_funcionario.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remover_funcionario.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem7 = self.tb_funcionarios.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem8 = self.tb_funcionarios.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Uniformes</span></p></body></html>", None))
        self.lbl_nome_uniforme.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.btn_editar_uniforme.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_adicionar_uniforme.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_remover_uniforme.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem9 = self.tb_uniforme.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_gestao), QCoreApplication.translate("MainWindow", u"Gest\u00e3o", None))
    # retranslateUi

