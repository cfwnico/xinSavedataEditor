# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'savemainoxLieK.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 460)
        MainWindow.setMinimumSize(QSize(550, 460))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(416, 416))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openfile_button = QPushButton(self.centralwidget)
        self.openfile_button.setObjectName(u"openfile_button")

        self.verticalLayout.addWidget(self.openfile_button)

        self.destroy_button = QPushButton(self.centralwidget)
        self.destroy_button.setObjectName(u"destroy_button")
        self.destroy_button.setEnabled(False)

        self.verticalLayout.addWidget(self.destroy_button)

        self.replace_button = QPushButton(self.centralwidget)
        self.replace_button.setObjectName(u"replace_button")
        self.replace_button.setEnabled(False)

        self.verticalLayout.addWidget(self.replace_button)

        self.savefloor_button = QPushButton(self.centralwidget)
        self.savefloor_button.setObjectName(u"savefloor_button")
        self.savefloor_button.setEnabled(False)

        self.verticalLayout.addWidget(self.savefloor_button)

        self.editother_button = QPushButton(self.centralwidget)
        self.editother_button.setObjectName(u"editother_button")
        self.editother_button.setEnabled(False)

        self.verticalLayout.addWidget(self.editother_button)

        self.savefile_button = QPushButton(self.centralwidget)
        self.savefile_button.setObjectName(u"savefile_button")
        self.savefile_button.setEnabled(False)

        self.verticalLayout.addWidget(self.savefile_button)

        self.save_combobox = QComboBox(self.centralwidget)
        self.save_combobox.addItem("")
        self.save_combobox.addItem("")
        self.save_combobox.addItem("")
        self.save_combobox.addItem("")
        self.save_combobox.setObjectName(u"save_combobox")
        self.save_combobox.setEnabled(False)

        self.verticalLayout.addWidget(self.save_combobox)

        self.floor_widget = QListWidget(self.centralwidget)
        self.floor_widget.setObjectName(u"floor_widget")

        self.verticalLayout.addWidget(self.floor_widget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u65b0\u65b0\u9b54\u5854\u5b58\u6863\u7f16\u8f91\u5668 V1.1", None))
        self.openfile_button.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5b58\u6863", None))
        self.destroy_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5899\u4f53", None))
        self.replace_button.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u56fe\u5757", None))
        self.savefloor_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5f53\u524d\u697c\u5c42", None))
        self.editother_button.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5176\u4ed6\u9879", None))
        self.savefile_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5b58\u6863", None))
        self.save_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5b58\u68631", None))
        self.save_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5b58\u68632", None))
        self.save_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5b58\u68633", None))
        self.save_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5b58\u68634", None))

    # retranslateUi

