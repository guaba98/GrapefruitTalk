# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/DialogWarning.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgWarning(object):
    def setupUi(self, DlgWarning):
        DlgWarning.setObjectName("DlgWarning")
        DlgWarning.setWindowModality(QtCore.Qt.NonModal)
        DlgWarning.resize(400, 350)
        DlgWarning.setMinimumSize(QtCore.QSize(400, 350))
        DlgWarning.setStyleSheet("background-color:white;")
        DlgWarning.setModal(True)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(DlgWarning)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(DlgWarning)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_close = QtWidgets.QPushButton(self.widget)
        self.btn_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/img_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setAutoDefault(False)
        self.btn_close.setFlat(True)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout_4.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(DlgWarning)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_img = QtWidgets.QLabel(self.widget_3)
        self.lbl_img.setMaximumSize(QtCore.QSize(35, 35))
        self.lbl_img.setText("")
        self.lbl_img.setPixmap(QtGui.QPixmap("../Images/img_warning.png"))
        self.lbl_img.setObjectName("lbl_img")
        self.verticalLayout_2.addWidget(self.lbl_img)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.layout_content = QtWidgets.QVBoxLayout()
        self.layout_content.setContentsMargins(-1, 5, -1, -1)
        self.layout_content.setObjectName("layout_content")
        self.lbl_text = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_text.setFont(font)
        self.lbl_text.setText("")
        self.lbl_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_text.setObjectName("lbl_text")
        self.layout_content.addWidget(self.lbl_text)
        self.horizontalLayout_2.addLayout(self.layout_content)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.layout_button = QtWidgets.QVBoxLayout()
        self.layout_button.setContentsMargins(40, 15, 40, 15)
        self.layout_button.setSpacing(10)
        self.layout_button.setObjectName("layout_button")
        self.layout_double = QtWidgets.QWidget(DlgWarning)
        self.layout_double.setObjectName("layout_double")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layout_double)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_yes = QtWidgets.QPushButton(self.layout_double)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_yes.sizePolicy().hasHeightForWidth())
        self.btn_yes.setSizePolicy(sizePolicy)
        self.btn_yes.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_yes.setFont(font)
        self.btn_yes.setStyleSheet("border:1px solid lightgray;\n"
"border-radius:5px;\n"
"padding:5px;")
        self.btn_yes.setObjectName("btn_yes")
        self.horizontalLayout_3.addWidget(self.btn_yes)
        self.btn_no = QtWidgets.QPushButton(self.layout_double)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_no.sizePolicy().hasHeightForWidth())
        self.btn_no.setSizePolicy(sizePolicy)
        self.btn_no.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_no.setFont(font)
        self.btn_no.setStyleSheet("border:1px solid lightgray;\n"
"border-radius:5px;\n"
"padding:5px;")
        self.btn_no.setObjectName("btn_no")
        self.horizontalLayout_3.addWidget(self.btn_no)
        self.layout_button.addWidget(self.layout_double)
        self.btn_single = QtWidgets.QPushButton(DlgWarning)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_single.sizePolicy().hasHeightForWidth())
        self.btn_single.setSizePolicy(sizePolicy)
        self.btn_single.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_single.setFont(font)
        self.btn_single.setStyleSheet("border:1px solid lightgray;\n"
"border-radius:5px;\n"
"padding:5px;")
        self.btn_single.setObjectName("btn_single")
        self.layout_button.addWidget(self.btn_single)
        self.verticalLayout_4.addLayout(self.layout_button)
        self.verticalLayout_4.setStretch(1, 1)

        self.retranslateUi(DlgWarning)
        QtCore.QMetaObject.connectSlotsByName(DlgWarning)

    def retranslateUi(self, DlgWarning):
        _translate = QtCore.QCoreApplication.translate
        DlgWarning.setWindowTitle(_translate("DlgWarning", "Warning"))
        self.btn_yes.setText(_translate("DlgWarning", "예"))
        self.btn_no.setText(_translate("DlgWarning", "아니오"))
        self.btn_single.setText(_translate("DlgWarning", "확인"))