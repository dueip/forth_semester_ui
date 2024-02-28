# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 719)
        MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.whole_calculator = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.whole_calculator.setGeometry(QtCore.QRect(0, 0, 441, 701))
        self.whole_calculator.setStyleSheet("QPushButton{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: darkGray;\n"
"     font: bold 36px;\n"
"}\n"
"QPushButton:pressed{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: lightGray;\n"
"     font: bold 36px;\n"
"}\n"
"QPushButton:!enabled{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: gray;\n"
"     font: bold 36px;\n"
"}\n"
"QGroupBox{\n"
"     border-style: outset;\n"
"     border-width: 0px;\n"
"     background-color: darkGray;\n"
"}\n"
"QSlider{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: darkGray;\n"
"     font: bold 36px;\n"
"}\n"
"QLabel{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: darkGray;\n"
"     font: bold 36px;\n"
"}\n"
"\n"
"QSlider:!enabled{\n"
"     border-style: outset;\n"
"     border-width: 3px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     background-color: gray;\n"
"     font: bold 36px;\n"
"}\n"
"\n"
"")
        self.whole_calculator.setObjectName("whole_calculator")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.whole_calculator)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.previous_input = QtWidgets.QLabel(parent=self.whole_calculator)
        self.previous_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.previous_input.setObjectName("previous_input")
        self.verticalLayout_2.addWidget(self.previous_input)
        self.result = QtWidgets.QLabel(parent=self.whole_calculator)
        self.result.setMaximumSize(QtCore.QSize(16777215, 75))
        self.result.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.result.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.result.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.result.setObjectName("result")
        self.verticalLayout_2.addWidget(self.result)
        self.number_system = QtWidgets.QLabel(parent=self.whole_calculator)
        self.number_system.setObjectName("number_system")
        self.verticalLayout_2.addWidget(self.number_system)
        self.horizontalSlider = QtWidgets.QSlider(parent=self.whole_calculator)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(16)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setInvertedAppearance(True)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.buttons = QtWidgets.QGroupBox(parent=self.whole_calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setStyleSheet("")
        self.buttons.setObjectName("buttons")
        self.buttonLayout = QtWidgets.QGridLayout(self.buttons)
        self.buttonLayout.setContentsMargins(-1, 0, -1, 0)
        self.buttonLayout.setObjectName("buttonLayout")
        self.number9 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number9.sizePolicy().hasHeightForWidth())
        self.number9.setSizePolicy(sizePolicy)
        self.number9.setMinimumSize(QtCore.QSize(100, 75))
        self.number9.setStyleSheet("")
        self.number9.setIconSize(QtCore.QSize(50, 30))
        self.number9.setObjectName("number9")
        self.buttonLayout.addWidget(self.number9, 2, 1, 1, 1)
        self.number4 = QtWidgets.QPushButton(parent=self.buttons)
        self.number4.setMinimumSize(QtCore.QSize(0, 75))
        self.number4.setObjectName("number4")
        self.buttonLayout.addWidget(self.number4, 3, 4, 1, 1)
        self.number8 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number8.sizePolicy().hasHeightForWidth())
        self.number8.setSizePolicy(sizePolicy)
        self.number8.setMinimumSize(QtCore.QSize(0, 75))
        self.number8.setObjectName("number8")
        self.buttonLayout.addWidget(self.number8, 2, 3, 1, 1)
        self.button_mul = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_mul.sizePolicy().hasHeightForWidth())
        self.button_mul.setSizePolicy(sizePolicy)
        self.button_mul.setMinimumSize(QtCore.QSize(0, 75))
        self.button_mul.setObjectName("button_mul")
        self.buttonLayout.addWidget(self.button_mul, 4, 0, 1, 1)
        self.number5 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number5.sizePolicy().hasHeightForWidth())
        self.number5.setSizePolicy(sizePolicy)
        self.number5.setMinimumSize(QtCore.QSize(0, 75))
        self.number5.setObjectName("number5")
        self.buttonLayout.addWidget(self.number5, 3, 3, 1, 1)
        self.number6 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number6.sizePolicy().hasHeightForWidth())
        self.number6.setSizePolicy(sizePolicy)
        self.number6.setMinimumSize(QtCore.QSize(0, 75))
        self.number6.setObjectName("number6")
        self.buttonLayout.addWidget(self.number6, 3, 1, 1, 1)
        self.number7 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number7.sizePolicy().hasHeightForWidth())
        self.number7.setSizePolicy(sizePolicy)
        self.number7.setMinimumSize(QtCore.QSize(100, 75))
        self.number7.setObjectName("number7")
        self.buttonLayout.addWidget(self.number7, 2, 4, 1, 1)
        self.button_plus = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        self.button_plus.setMinimumSize(QtCore.QSize(0, 75))
        self.button_plus.setObjectName("button_plus")
        self.buttonLayout.addWidget(self.button_plus, 2, 0, 1, 1)
        self.button_div = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_div.sizePolicy().hasHeightForWidth())
        self.button_div.setSizePolicy(sizePolicy)
        self.button_div.setMinimumSize(QtCore.QSize(0, 75))
        self.button_div.setObjectName("button_div")
        self.buttonLayout.addWidget(self.button_div, 5, 0, 1, 1)
        self.number3 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number3.sizePolicy().hasHeightForWidth())
        self.number3.setSizePolicy(sizePolicy)
        self.number3.setMinimumSize(QtCore.QSize(0, 75))
        self.number3.setObjectName("number3")
        self.buttonLayout.addWidget(self.number3, 4, 1, 1, 1)
        self.button_c = QtWidgets.QPushButton(parent=self.buttons)
        self.button_c.setObjectName("button_c")
        self.buttonLayout.addWidget(self.button_c, 0, 3, 1, 1)
        self.button_equal = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        self.button_equal.setMinimumSize(QtCore.QSize(0, 75))
        self.button_equal.setObjectName("button_equal")
        self.buttonLayout.addWidget(self.button_equal, 5, 1, 1, 1)
        self.number0 = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number0.sizePolicy().hasHeightForWidth())
        self.number0.setSizePolicy(sizePolicy)
        self.number0.setMinimumSize(QtCore.QSize(0, 75))
        self.number0.setObjectName("number0")
        self.buttonLayout.addWidget(self.number0, 5, 4, 1, 1)
        self.number1 = QtWidgets.QPushButton(parent=self.buttons)
        self.number1.setMinimumSize(QtCore.QSize(0, 75))
        self.number1.setObjectName("number1")
        self.buttonLayout.addWidget(self.number1, 4, 4, 1, 1)
        self.number2 = QtWidgets.QPushButton(parent=self.buttons)
        self.number2.setMinimumSize(QtCore.QSize(0, 75))
        self.number2.setObjectName("number2")
        self.buttonLayout.addWidget(self.number2, 4, 3, 1, 1)
        self.button_back = QtWidgets.QPushButton(parent=self.buttons)
        self.button_back.setMaximumSize(QtCore.QSize(16777215, 49))
        self.button_back.setObjectName("button_back")
        self.buttonLayout.addWidget(self.button_back, 0, 0, 1, 1)
        self.button_sp = QtWidgets.QPushButton(parent=self.buttons)
        self.button_sp.setObjectName("button_sp")
        self.buttonLayout.addWidget(self.button_sp, 0, 1, 1, 1)
        self.button_dot = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_dot.sizePolicy().hasHeightForWidth())
        self.button_dot.setSizePolicy(sizePolicy)
        self.button_dot.setMinimumSize(QtCore.QSize(0, 75))
        self.button_dot.setObjectName("button_dot")
        self.buttonLayout.addWidget(self.button_dot, 5, 3, 1, 1)
        self.button_ce = QtWidgets.QPushButton(parent=self.buttons)
        self.button_ce.setObjectName("button_ce")
        self.buttonLayout.addWidget(self.button_ce, 0, 4, 1, 1)
        self.button_minus = QtWidgets.QPushButton(parent=self.buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        self.button_minus.setMinimumSize(QtCore.QSize(0, 75))
        self.button_minus.setObjectName("button_minus")
        self.buttonLayout.addWidget(self.button_minus, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.buttons)
        self.horizontalGroupBox = QtWidgets.QGroupBox(parent=self.whole_calculator)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_2.setContentsMargins(11, 0, 5, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.numberF = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberF.sizePolicy().hasHeightForWidth())
        self.numberF.setSizePolicy(sizePolicy)
        self.numberF.setMinimumSize(QtCore.QSize(0, 50))
        self.numberF.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberF.setObjectName("numberF")
        self.horizontalLayout_2.addWidget(self.numberF)
        self.numberE = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberE.sizePolicy().hasHeightForWidth())
        self.numberE.setSizePolicy(sizePolicy)
        self.numberE.setMinimumSize(QtCore.QSize(0, 50))
        self.numberE.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberE.setObjectName("numberE")
        self.horizontalLayout_2.addWidget(self.numberE)
        self.numberD = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberD.sizePolicy().hasHeightForWidth())
        self.numberD.setSizePolicy(sizePolicy)
        self.numberD.setMinimumSize(QtCore.QSize(0, 50))
        self.numberD.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberD.setObjectName("numberD")
        self.horizontalLayout_2.addWidget(self.numberD)
        self.numberC = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberC.sizePolicy().hasHeightForWidth())
        self.numberC.setSizePolicy(sizePolicy)
        self.numberC.setMinimumSize(QtCore.QSize(0, 50))
        self.numberC.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberC.setObjectName("numberC")
        self.horizontalLayout_2.addWidget(self.numberC)
        self.numberB = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberB.sizePolicy().hasHeightForWidth())
        self.numberB.setSizePolicy(sizePolicy)
        self.numberB.setMinimumSize(QtCore.QSize(0, 50))
        self.numberB.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberB.setObjectName("numberB")
        self.horizontalLayout_2.addWidget(self.numberB)
        self.numberA = QtWidgets.QPushButton(parent=self.horizontalGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberA.sizePolicy().hasHeightForWidth())
        self.numberA.setSizePolicy(sizePolicy)
        self.numberA.setMinimumSize(QtCore.QSize(0, 50))
        self.numberA.setMaximumSize(QtCore.QSize(16777215, 50))
        self.numberA.setObjectName("numberA")
        self.horizontalLayout_2.addWidget(self.numberA)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 26))
        self.menubar.setObjectName("menubar")
        self.menuCalculator = QtWidgets.QMenu(parent=self.menubar)
        self.menuCalculator.setObjectName("menuCalculator")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuCalculator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.previous_input.setText(_translate("MainWindow", "0"))
        self.result.setText(_translate("MainWindow", "0"))
        self.number_system.setText(_translate("MainWindow", "Number System: 10"))
        self.number9.setText(_translate("MainWindow", "9"))
        self.number4.setText(_translate("MainWindow", "4"))
        self.number8.setText(_translate("MainWindow", "8"))
        self.button_mul.setText(_translate("MainWindow", "*"))
        self.number5.setText(_translate("MainWindow", "5"))
        self.number6.setText(_translate("MainWindow", "6"))
        self.number7.setText(_translate("MainWindow", "7"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_div.setText(_translate("MainWindow", "/"))
        self.number3.setText(_translate("MainWindow", "3"))
        self.button_c.setText(_translate("MainWindow", "Clear"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.number0.setText(_translate("MainWindow", "0"))
        self.number1.setText(_translate("MainWindow", "1"))
        self.number2.setText(_translate("MainWindow", "2"))
        self.button_back.setText(_translate("MainWindow", "⌫"))
        self.button_sp.setText(_translate("MainWindow", "Time"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_ce.setText(_translate("MainWindow", "CE"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.numberF.setText(_translate("MainWindow", "F"))
        self.numberE.setText(_translate("MainWindow", "E"))
        self.numberD.setText(_translate("MainWindow", "D"))
        self.numberC.setText(_translate("MainWindow", "C"))
        self.numberB.setText(_translate("MainWindow", "B"))
        self.numberA.setText(_translate("MainWindow", "A"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))