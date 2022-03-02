# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'savemainwusfse.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 470)
        MainWindow.setMinimumSize(QSize(550, 470))
        MainWindow.setMaximumSize(QSize(550, 470))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 20, 82, 146))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.import_button = QPushButton(self.layoutWidget)
        self.import_button.setObjectName(u"import_button")

        self.verticalLayout.addWidget(self.import_button)

        self.destroy_button = QPushButton(self.layoutWidget)
        self.destroy_button.setObjectName(u"destroy_button")

        self.verticalLayout.addWidget(self.destroy_button)

        self.replace_button = QPushButton(self.layoutWidget)
        self.replace_button.setObjectName(u"replace_button")

        self.verticalLayout.addWidget(self.replace_button)

        self.export_button = QPushButton(self.layoutWidget)
        self.export_button.setObjectName(u"export_button")

        self.verticalLayout.addWidget(self.export_button)

        self.about_button = QPushButton(self.layoutWidget)
        self.about_button.setObjectName(u"about_button")

        self.verticalLayout.addWidget(self.about_button)

        self.label_bg = QLabel(self.centralwidget)
        self.label_bg.setObjectName(u"label_bg")
        self.label_bg.setGeometry(QRect(20, 20, 416, 416))
        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_bg.setBuddy(self.label_bg)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u65b0\u65b0\u9b54\u5854\u5b58\u6863\u7f16\u8f91\u5668", None))
        self.import_button.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.destroy_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5899\u4f53", None))
        self.replace_button.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362\u56fe\u5757", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label_bg.setText("")
    # retranslateUi

