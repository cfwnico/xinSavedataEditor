# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingycqWMV.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(435, 600)
        Dialog.setMinimumSize(QSize(435, 600))
        Dialog.setMaximumSize(QSize(435, 600))
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(180, 20, 241, 221))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.fly_check = QCheckBox(self.groupBox_2)
        self.fly_check.setObjectName(u"fly_check")

        self.gridLayout_2.addWidget(self.fly_check, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.ddd_check = QCheckBox(self.groupBox_2)
        self.ddd_check.setObjectName(u"ddd_check")

        self.gridLayout_2.addWidget(self.ddd_check, 1, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.ice_check = QCheckBox(self.groupBox_2)
        self.ice_check.setObjectName(u"ice_check")

        self.gridLayout_2.addWidget(self.ice_check, 2, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.magicdef_check = QCheckBox(self.groupBox_2)
        self.magicdef_check.setObjectName(u"magicdef_check")

        self.gridLayout_2.addWidget(self.magicdef_check, 3, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)

        self.chor_check = QCheckBox(self.groupBox_2)
        self.chor_check.setObjectName(u"chor_check")

        self.gridLayout_2.addWidget(self.chor_check, 4, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 6, 0, 1, 1)

        self.key_check = QCheckBox(self.groupBox_2)
        self.key_check.setObjectName(u"key_check")

        self.gridLayout_2.addWidget(self.key_check, 5, 2, 1, 1)

        self.yellow_edit = QSpinBox(self.groupBox_2)
        self.yellow_edit.setObjectName(u"yellow_edit")
        self.yellow_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.yellow_edit, 0, 1, 1, 1)

        self.blue_edit = QSpinBox(self.groupBox_2)
        self.blue_edit.setObjectName(u"blue_edit")
        self.blue_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.blue_edit, 1, 1, 1, 1)

        self.red_edit = QSpinBox(self.groupBox_2)
        self.red_edit.setObjectName(u"red_edit")
        self.red_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.red_edit, 2, 1, 1, 1)

        self.nod_edit = QSpinBox(self.groupBox_2)
        self.nod_edit.setObjectName(u"nod_edit")
        self.nod_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.nod_edit, 3, 1, 1, 1)

        self.nok_edit = QSpinBox(self.groupBox_2)
        self.nok_edit.setObjectName(u"nok_edit")
        self.nok_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.nok_edit, 4, 1, 1, 1)

        self.bigchor_edit = QSpinBox(self.groupBox_2)
        self.bigchor_edit.setObjectName(u"bigchor_edit")
        self.bigchor_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.bigchor_edit, 5, 1, 1, 1)

        self.relive_edit = QSpinBox(self.groupBox_2)
        self.relive_edit.setObjectName(u"relive_edit")
        self.relive_edit.setMaximum(9999)

        self.gridLayout_2.addWidget(self.relive_edit, 6, 1, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 151, 221))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.lv_edit = QSpinBox(self.groupBox)
        self.lv_edit.setObjectName(u"lv_edit")
        self.lv_edit.setMinimum(1)
        self.lv_edit.setMaximum(9999)

        self.gridLayout.addWidget(self.lv_edit, 0, 1, 1, 1)

        self.hp_edit = QSpinBox(self.groupBox)
        self.hp_edit.setObjectName(u"hp_edit")
        self.hp_edit.setMinimum(1)
        self.hp_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.hp_edit, 1, 1, 1, 1)

        self.atk_edit = QSpinBox(self.groupBox)
        self.atk_edit.setObjectName(u"atk_edit")
        self.atk_edit.setMinimum(1)
        self.atk_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.atk_edit, 2, 1, 1, 1)

        self.def_edit = QSpinBox(self.groupBox)
        self.def_edit.setObjectName(u"def_edit")
        self.def_edit.setMinimum(1)
        self.def_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.def_edit, 3, 1, 1, 1)

        self.miss_edit = QSpinBox(self.groupBox)
        self.miss_edit.setObjectName(u"miss_edit")
        self.miss_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.miss_edit, 4, 1, 1, 1)

        self.exp_edit = QSpinBox(self.groupBox)
        self.exp_edit.setObjectName(u"exp_edit")
        self.exp_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.exp_edit, 5, 1, 1, 1)

        self.gold_edit = QSpinBox(self.groupBox)
        self.gold_edit.setObjectName(u"gold_edit")
        self.gold_edit.setMaximum(9999999)

        self.gridLayout.addWidget(self.gold_edit, 6, 1, 1, 1)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 250, 151, 181))
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.nowfloor_edit = QSpinBox(self.groupBox_4)
        self.nowfloor_edit.setObjectName(u"nowfloor_edit")
        self.nowfloor_edit.setMinimum(-25)
        self.nowfloor_edit.setMaximum(20)

        self.gridLayout_3.addWidget(self.nowfloor_edit, 2, 1, 1, 1)

        self.currenfloor_label = QLabel(self.groupBox_4)
        self.currenfloor_label.setObjectName(u"currenfloor_label")

        self.gridLayout_3.addWidget(self.currenfloor_label, 3, 1, 1, 1)

        self.x_edit = QSpinBox(self.groupBox_4)
        self.x_edit.setObjectName(u"x_edit")
        self.x_edit.setMinimum(1)
        self.x_edit.setMaximum(11)

        self.gridLayout_3.addWidget(self.x_edit, 0, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)

        self.y_edit = QSpinBox(self.groupBox_4)
        self.y_edit.setObjectName(u"y_edit")
        self.y_edit.setMinimum(1)
        self.y_edit.setMaximum(11)

        self.gridLayout_3.addWidget(self.y_edit, 1, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.savename_edit = QLineEdit(self.groupBox_4)
        self.savename_edit.setObjectName(u"savename_edit")

        self.gridLayout_3.addWidget(self.savename_edit, 5, 0, 1, 2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(180, 250, 241, 181))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.atktimes_edit = QSpinBox(self.groupBox_3)
        self.atktimes_edit.setObjectName(u"atktimes_edit")
        self.atktimes_edit.setMinimum(1)
        self.atktimes_edit.setMaximum(9999)

        self.gridLayout_4.addWidget(self.atktimes_edit, 0, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)

        self.atknear_edit = QSpinBox(self.groupBox_3)
        self.atknear_edit.setObjectName(u"atknear_edit")
        self.atknear_edit.setMaximum(9999)

        self.gridLayout_4.addWidget(self.atknear_edit, 1, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)

        self.defnear_edit = QSpinBox(self.groupBox_3)
        self.defnear_edit.setObjectName(u"defnear_edit")
        self.defnear_edit.setMaximum(9999)

        self.gridLayout_4.addWidget(self.defnear_edit, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 3, 0, 1, 1)

        self.stat_combobox = QComboBox(self.groupBox_3)
        self.stat_combobox.addItem("")
        self.stat_combobox.addItem("")
        self.stat_combobox.addItem("")
        self.stat_combobox.setObjectName(u"stat_combobox")

        self.gridLayout_4.addWidget(self.stat_combobox, 3, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 4, 0, 1, 1)

        self.atkanm_combobox = QComboBox(self.groupBox_3)
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.addItem("")
        self.atkanm_combobox.setObjectName(u"atkanm_combobox")

        self.gridLayout_4.addWidget(self.atkanm_combobox, 4, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 8)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 440, 211, 140))
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.shop3f_edit = QSpinBox(self.groupBox_5)
        self.shop3f_edit.setObjectName(u"shop3f_edit")
        self.shop3f_edit.setMinimum(1)
        self.shop3f_edit.setMaximum(9999)

        self.gridLayout_5.addWidget(self.shop3f_edit, 0, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 2, 0, 1, 2)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)

        self.shopb5f_edit = QSpinBox(self.groupBox_5)
        self.shopb5f_edit.setObjectName(u"shopb5f_edit")
        self.shopb5f_edit.setMinimum(1)
        self.shopb5f_edit.setMaximum(9999)

        self.gridLayout_5.addWidget(self.shopb5f_edit, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_28 = QLabel(self.groupBox_5)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_3.addWidget(self.label_28)

        self.minf_edit = QSpinBox(self.groupBox_5)
        self.minf_edit.setObjectName(u"minf_edit")
        self.minf_edit.setMinimum(-25)
        self.minf_edit.setMaximum(0)

        self.horizontalLayout_3.addWidget(self.minf_edit)

        self.label_27 = QLabel(self.groupBox_5)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_3.addWidget(self.label_27)

        self.label_29 = QLabel(self.groupBox_5)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_3.addWidget(self.label_29)

        self.maxf_edit = QSpinBox(self.groupBox_5)
        self.maxf_edit.setObjectName(u"maxf_edit")
        self.maxf_edit.setMaximum(20)

        self.horizontalLayout_3.addWidget(self.maxf_edit)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 560, 158, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.save_button = QPushButton(self.layoutWidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_2.addWidget(self.save_button)

        self.cancel_button = QPushButton(self.layoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_2.addWidget(self.cancel_button)

        self.label_30 = QLabel(Dialog)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(250, 450, 161, 101))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u4fee\u6539\u5176\u4ed6\u9879...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u9053\u5177\u76f8\u5173", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u9ec4\u94a5\u5319\uff1a", None))
        self.fly_check.setText(QCoreApplication.translate("Dialog", u"\u697c\u5c42\u4f20\u9001", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u84dd\u94a5\u5319\uff1a", None))
        self.ddd_check.setText(QCoreApplication.translate("Dialog", u"\u602a\u7269\u624b\u518c", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u7ea2\u94a5\u5319\uff1a", None))
#if QT_CONFIG(tooltip)
        self.ice_check.setToolTip(QCoreApplication.translate("Dialog", u"\u6d88\u9664\u706b\u7f51\u9677\u9631\u7684\u9053\u5177", None))
#endif // QT_CONFIG(tooltip)
        self.ice_check.setText(QCoreApplication.translate("Dialog", u"\u51b0\u4e4b\u62a4\u7b26", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u4efb\u610f\u95e8\uff1a", None))
#if QT_CONFIG(tooltip)
        self.magicdef_check.setToolTip(QCoreApplication.translate("Dialog", u"\u964d\u4f4e\u6cd5\u5e08\u9632\u5fa1\u529b\u7684\u9053\u5177", None))
#endif // QT_CONFIG(tooltip)
        self.magicdef_check.setText(QCoreApplication.translate("Dialog", u"\u9b54\u6cd5\u62a4\u7b26", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u795e\u5251\u4e4b\u8bc1\uff1a", None))
#if QT_CONFIG(tooltip)
        self.chor_check.setToolTip(QCoreApplication.translate("Dialog", u"\u62e5\u6709\u540e\u548c\u5c0f\u5077\u5bf9\u8bdd\u53ef\u4ee5\u5f00\u542f\u5730\u4e0b\u5c42", None))
#endif // QT_CONFIG(tooltip)
        self.chor_check.setText(QCoreApplication.translate("Dialog", u"\u5c0f\u5077\u9504\u5934", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u5b9d\u77f3\u9504\u5934\uff1a", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("Dialog", u"\u751f\u547d\u5f520\u540e\u589e\u52a02000\u8840\u7684\u9053\u5177", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u590d\u6d3b\u5341\u5b57\uff1a", None))
#if QT_CONFIG(tooltip)
        self.key_check.setToolTip(QCoreApplication.translate("Dialog", u"\u62e5\u6709\u540e\u53ef\u4ee5\u8fdb\u516517F\u5bc6\u9053", None))
#endif // QT_CONFIG(tooltip)
        self.key_check.setText(QCoreApplication.translate("Dialog", u"\u4ed9\u5b50\u94a5\u5319", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u80fd\u529b\u503c\u76f8\u5173", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7b49\u7ea7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u751f\u547d\u503c\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u653b\u51fb\u529b\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u9632\u5fa1\u529b\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u654f\u6377\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7ecf\u9a8c\u503c\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u91d1\u5e01\uff1a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u5b58\u6863\u76f8\u5173", None))
        self.currenfloor_label.setText("")
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u5b58\u6863\u540d\u79f0\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u697c\u5c42\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u697c\u5c42\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u52c7\u8005\u5750\u6807\uff1aX\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u52c7\u8005\u5750\u6807\uff1aY\uff1a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u6218\u6597\u76f8\u5173", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u6bcf\u56de\u5408\u653b\u51fb\u6b21\u6570\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u653b\u51fb\u4e34\u754c\u503c\uff1a", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"\u9632\u5fa1\u4e34\u754c\u503c\uff1a", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u72b6\u6001\uff1a", None))
        self.stat_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"\u6b63\u5e38", None))
        self.stat_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"\u4e2d\u6bd2", None))
        self.stat_combobox.setItemText(2, QCoreApplication.translate("Dialog", u"\u8870\u5f31", None))

        self.label_31.setText(QCoreApplication.translate("Dialog", u"\u653b\u51fb\u52a8\u753b\uff1a", None))
        self.atkanm_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"\u7a7a\u624b", None))
        self.atkanm_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"\u94c1\u5251", None))
        self.atkanm_combobox.setItemText(2, QCoreApplication.translate("Dialog", u"\u94f6\u5251", None))
        self.atkanm_combobox.setItemText(3, QCoreApplication.translate("Dialog", u"\u9a91\u58eb\u5251", None))
        self.atkanm_combobox.setItemText(4, QCoreApplication.translate("Dialog", u"\u5723\u5251", None))
        self.atkanm_combobox.setItemText(5, QCoreApplication.translate("Dialog", u"\u795e\u5723\u5251", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"\u6742\u9879", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"\u697c\u5c42\u4f20\u9001\u5668\u5141\u8bb8\u4f20\u9001\u7684\u697c\u5c42\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"B5F\u5546\u5e97\u52a0\u70b9\u91d1\u5e01\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"3F\u5546\u5e97\u52a0\u70b9\u91d1\u5e01\uff1a", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"\u6700\u4f4e", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"~", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"\u6700\u9ad8", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.label_30.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"right\">By Python 3.10.2</p><p align=\"right\">GUI PySide6</p><p align=\"right\">Author:cfw</p></body></html>", None))
    # retranslateUi

