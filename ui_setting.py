# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingSyXorx.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(440, 600)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 230, 401, 321))
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 20, 91, 16))
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 40, 91, 16))
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 60, 101, 16))
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 80, 91, 16))
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 100, 71, 16))
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 120, 53, 16))
        self.x_edit = QLineEdit(self.groupBox_3)
        self.x_edit.setObjectName(u"x_edit")
        self.x_edit.setGeometry(QRect(100, 20, 113, 21))
        self.y_edit = QLineEdit(self.groupBox_3)
        self.y_edit.setObjectName(u"y_edit")
        self.y_edit.setGeometry(QRect(100, 40, 113, 21))
        self.toname_edit = QLineEdit(self.groupBox_3)
        self.toname_edit.setObjectName(u"toname_edit")
        self.toname_edit.setGeometry(QRect(110, 60, 113, 21))
        self.cureenfloor_edit = QLineEdit(self.groupBox_3)
        self.cureenfloor_edit.setObjectName(u"cureenfloor_edit")
        self.cureenfloor_edit.setGeometry(QRect(110, 80, 113, 21))
        self.nowfloor_edit = QLineEdit(self.groupBox_3)
        self.nowfloor_edit.setObjectName(u"nowfloor_edit")
        self.nowfloor_edit.setGeometry(QRect(100, 100, 113, 21))
        self.savename_edit = QLineEdit(self.groupBox_3)
        self.savename_edit.setObjectName(u"savename_edit")
        self.savename_edit.setGeometry(QRect(100, 120, 113, 21))
        self.ok_button = QPushButton(Dialog)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(270, 560, 75, 24))
        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(350, 560, 75, 24))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(180, 20, 241, 201))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.yellow_edit = QLineEdit(self.groupBox_2)
        self.yellow_edit.setObjectName(u"yellow_edit")

        self.gridLayout_2.addWidget(self.yellow_edit, 0, 1, 1, 1)

        self.fly_check = QCheckBox(self.groupBox_2)
        self.fly_check.setObjectName(u"fly_check")

        self.gridLayout_2.addWidget(self.fly_check, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.blue_edit = QLineEdit(self.groupBox_2)
        self.blue_edit.setObjectName(u"blue_edit")

        self.gridLayout_2.addWidget(self.blue_edit, 1, 1, 1, 1)

        self.ddd_check = QCheckBox(self.groupBox_2)
        self.ddd_check.setObjectName(u"ddd_check")

        self.gridLayout_2.addWidget(self.ddd_check, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.red_edit = QLineEdit(self.groupBox_2)
        self.red_edit.setObjectName(u"red_edit")

        self.gridLayout_2.addWidget(self.red_edit, 2, 1, 1, 1)

        self.checkBox_6 = QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_2.addWidget(self.checkBox_6, 2, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.nod_edit = QLineEdit(self.groupBox_2)
        self.nod_edit.setObjectName(u"nod_edit")

        self.gridLayout_2.addWidget(self.nod_edit, 3, 1, 1, 1)

        self.ice_check = QCheckBox(self.groupBox_2)
        self.ice_check.setObjectName(u"ice_check")

        self.gridLayout_2.addWidget(self.ice_check, 3, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)

        self.nok_edit = QLineEdit(self.groupBox_2)
        self.nok_edit.setObjectName(u"nok_edit")

        self.gridLayout_2.addWidget(self.nok_edit, 4, 1, 1, 1)

        self.magicdef_check = QCheckBox(self.groupBox_2)
        self.magicdef_check.setObjectName(u"magicdef_check")

        self.gridLayout_2.addWidget(self.magicdef_check, 4, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)

        self.bigchor_edit = QLineEdit(self.groupBox_2)
        self.bigchor_edit.setObjectName(u"bigchor_edit")

        self.gridLayout_2.addWidget(self.bigchor_edit, 5, 1, 1, 1)

        self.chor_check = QCheckBox(self.groupBox_2)
        self.chor_check.setObjectName(u"chor_check")

        self.gridLayout_2.addWidget(self.chor_check, 5, 2, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 151, 201))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hp_edit = QLineEdit(self.groupBox)
        self.hp_edit.setObjectName(u"hp_edit")

        self.gridLayout.addWidget(self.hp_edit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.def_edit = QLineEdit(self.groupBox)
        self.def_edit.setObjectName(u"def_edit")

        self.gridLayout.addWidget(self.def_edit, 3, 1, 2, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lv_edit = QLineEdit(self.groupBox)
        self.lv_edit.setObjectName(u"lv_edit")

        self.gridLayout.addWidget(self.lv_edit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 2, 1)

        self.miss_edit = QLineEdit(self.groupBox)
        self.miss_edit.setObjectName(u"miss_edit")

        self.gridLayout.addWidget(self.miss_edit, 5, 1, 1, 1)

        self.atk_edit = QLineEdit(self.groupBox)
        self.atk_edit.setObjectName(u"atk_edit")

        self.gridLayout.addWidget(self.atk_edit, 2, 1, 1, 1)

        self.exp_edit = QLineEdit(self.groupBox)
        self.exp_edit.setObjectName(u"exp_edit")

        self.gridLayout.addWidget(self.exp_edit, 6, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.gold_edit = QLineEdit(self.groupBox)
        self.gold_edit.setObjectName(u"gold_edit")

        self.gridLayout.addWidget(self.gold_edit, 7, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5176\u4ed6\u9879...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u5176\u4ed6", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u52c7\u8005\u5750\u6807\uff1aX", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u52c7\u8005\u5750\u6807\uff1aY", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"tonameofstage", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"currentfloor", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"nowfloor", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u5b58\u6863\u540d\u79f0\uff1a", None))
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u9053\u5177", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u9ec4\u94a5\u5319\uff1a", None))
        self.fly_check.setText(QCoreApplication.translate("Dialog", u"\u697c\u5c42\u4f20\u9001\u5668", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u84dd\u94a5\u5319\uff1a", None))
        self.ddd_check.setText(QCoreApplication.translate("Dialog", u"\u602a\u7269\u624b\u518c", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u7ea2\u94a5\u5319\uff1a", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"\u590d\u6d3b\u5341\u5b57\u67b6", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u4efb\u610f\u95e8\uff1a", None))
        self.ice_check.setText(QCoreApplication.translate("Dialog", u"\u51b0\u4e4b\u62a4\u7b26", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u795e\u5251\u4e4b\u8bc1\uff1a", None))
        self.magicdef_check.setText(QCoreApplication.translate("Dialog", u"\u9b54\u6cd5\u62a4\u7b26", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u5b9d\u77f3\u9504\u5934\uff1a", None))
        self.chor_check.setText(QCoreApplication.translate("Dialog", u"\u5c0f\u5077\u9504\u5934", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u80fd\u529b\u503c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u751f\u547d\u503c\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u9632\u5fa1\u529b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u654f\u6377\uff1a", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7b49\u7ea7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u653b\u51fb\u529b\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7ecf\u9a8c\u503c\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u91d1\u5e01\uff1a", None))
    # retranslateUi

