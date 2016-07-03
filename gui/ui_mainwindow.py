# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.datamodeTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.datamodeTabWidget.setObjectName("datamodeTabWidget")
        self.dailytab = QtWidgets.QWidget()
        self.dailytab.setObjectName("dailytab")
        self.dailyTabLayout = QtWidgets.QVBoxLayout(self.dailytab)
        self.dailyTabLayout.setContentsMargins(9, 9, 9, 9)
        self.dailyTabLayout.setObjectName("dailyTabLayout")
        self.headerLabel_daily = QtWidgets.QLabel(self.dailytab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.headerLabel_daily.setFont(font)
        self.headerLabel_daily.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel_daily.setObjectName("headerLabel_daily")
        self.dailyTabLayout.addWidget(self.headerLabel_daily)
        self.dailyTabLayout_2 = QtWidgets.QFormLayout()
        self.dailyTabLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.dailyTabLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.dailyTabLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dailyTabLayout_2.setHorizontalSpacing(0)
        self.dailyTabLayout_2.setObjectName("dailyTabLayout_2")
        self.placeLabel_daily = QtWidgets.QLabel(self.dailytab)
        self.placeLabel_daily.setObjectName("placeLabel_daily")
        self.dailyTabLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.placeLabel_daily)
        self.stationComboBox_daily = QtWidgets.QComboBox(self.dailytab)
        self.stationComboBox_daily.setEditable(True)
        self.stationComboBox_daily.setMaxVisibleItems(20)
        self.stationComboBox_daily.setObjectName("stationComboBox_daily")
        self.dailyTabLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stationComboBox_daily)
        self.availableFromLabel_daily = QtWidgets.QLabel(self.dailytab)
        self.availableFromLabel_daily.setObjectName("availableFromLabel_daily")
        self.dailyTabLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.availableFromLabel_daily)
        self.availableDataFromContent_daily = QtWidgets.QLabel(self.dailytab)
        self.availableDataFromContent_daily.setText("")
        self.availableDataFromContent_daily.setObjectName("availableDataFromContent_daily")
        self.dailyTabLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.availableDataFromContent_daily)
        self.startDatetimeLabel_daily = QtWidgets.QLabel(self.dailytab)
        self.startDatetimeLabel_daily.setObjectName("startDatetimeLabel_daily")
        self.dailyTabLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.startDatetimeLabel_daily)
        self.startDatetimeEdit_daily = QtWidgets.QDateEdit(self.dailytab)
        self.startDatetimeEdit_daily.setStyleSheet("")
        self.startDatetimeEdit_daily.setObjectName("startDatetimeEdit_daily")
        self.dailyTabLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startDatetimeEdit_daily)
        self.endDatetimeLabel_daily = QtWidgets.QLabel(self.dailytab)
        self.endDatetimeLabel_daily.setObjectName("endDatetimeLabel_daily")
        self.dailyTabLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.endDatetimeLabel_daily)
        self.endDatetimeEdit_daily = QtWidgets.QDateEdit(self.dailytab)
        self.endDatetimeEdit_daily.setObjectName("endDatetimeEdit_daily")
        self.dailyTabLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endDatetimeEdit_daily)
        self.dailyTabLayout.addLayout(self.dailyTabLayout_2)
        self.downloadButton_daily = QtWidgets.QPushButton(self.dailytab)
        self.downloadButton_daily.setObjectName("downloadButton_daily")
        self.dailyTabLayout.addWidget(self.downloadButton_daily)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dailyTabLayout.addItem(spacerItem)
        self.datamodeTabWidget.addTab(self.dailytab, "")
        self.realtimetab = QtWidgets.QWidget()
        self.realtimetab.setMaximumSize(QtCore.QSize(393, 238))
        self.realtimetab.setObjectName("realtimetab")
        self.realtimeTabLayout = QtWidgets.QVBoxLayout(self.realtimetab)
        self.realtimeTabLayout.setContentsMargins(9, 9, 9, 9)
        self.realtimeTabLayout.setObjectName("realtimeTabLayout")
        self.headerLabel_realtime = QtWidgets.QLabel(self.realtimetab)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.headerLabel_realtime.setFont(font)
        self.headerLabel_realtime.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel_realtime.setObjectName("headerLabel_realtime")
        self.realtimeTabLayout.addWidget(self.headerLabel_realtime)
        self.realtimeTabLayout_2 = QtWidgets.QFormLayout()
        self.realtimeTabLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.realtimeTabLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.realtimeTabLayout_2.setObjectName("realtimeTabLayout_2")
        self.placeLabel_realtime = QtWidgets.QLabel(self.realtimetab)
        self.placeLabel_realtime.setObjectName("placeLabel_realtime")
        self.realtimeTabLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.placeLabel_realtime)
        self.stationComboBox_realtime = QtWidgets.QComboBox(self.realtimetab)
        self.stationComboBox_realtime.setEditable(True)
        self.stationComboBox_realtime.setMaxVisibleItems(20)
        self.stationComboBox_realtime.setObjectName("stationComboBox_realtime")
        self.realtimeTabLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.stationComboBox_realtime)
        self.availableFromLabel_realtime = QtWidgets.QLabel(self.realtimetab)
        self.availableFromLabel_realtime.setObjectName("availableFromLabel_realtime")
        self.realtimeTabLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.availableFromLabel_realtime)
        self.availableFromContent_realtime = QtWidgets.QLabel(self.realtimetab)
        self.availableFromContent_realtime.setObjectName("availableFromContent_realtime")
        self.realtimeTabLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.availableFromContent_realtime)
        self.startDatetimeLabel_realtime = QtWidgets.QLabel(self.realtimetab)
        self.startDatetimeLabel_realtime.setObjectName("startDatetimeLabel_realtime")
        self.realtimeTabLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.startDatetimeLabel_realtime)
        self.endDatetimeLabel_realtime = QtWidgets.QLabel(self.realtimetab)
        self.endDatetimeLabel_realtime.setObjectName("endDatetimeLabel_realtime")
        self.realtimeTabLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.endDatetimeLabel_realtime)
        self.startDatetimeEdit_realtime = QtWidgets.QDateTimeEdit(self.realtimetab)
        self.startDatetimeEdit_realtime.setStyleSheet("")
        self.startDatetimeEdit_realtime.setObjectName("startDatetimeEdit_realtime")
        self.realtimeTabLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.startDatetimeEdit_realtime)
        self.endDatetimeEdit_realtime = QtWidgets.QDateTimeEdit(self.realtimetab)
        self.endDatetimeEdit_realtime.setObjectName("endDatetimeEdit_realtime")
        self.realtimeTabLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endDatetimeEdit_realtime)
        self.realtimeTabLayout.addLayout(self.realtimeTabLayout_2)
        self.downloadButton_realtime = QtWidgets.QPushButton(self.realtimetab)
        self.downloadButton_realtime.setObjectName("downloadButton_realtime")
        self.realtimeTabLayout.addWidget(self.downloadButton_realtime)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.realtimeTabLayout.addItem(spacerItem1)
        self.datamodeTabWidget.addTab(self.realtimetab, "")
        self.verticalLayout_2.addWidget(self.datamodeTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSet_api_key = QtWidgets.QAction(MainWindow)
        self.actionSet_api_key.setObjectName("actionSet_api_key")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSet_language = QtWidgets.QAction(MainWindow)
        self.actionSet_language.setObjectName("actionSet_language")
        self.actionView_instructions = QtWidgets.QAction(MainWindow)
        self.actionView_instructions.setObjectName("actionView_instructions")
        self.actionCheck_updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_updates.setObjectName("actionCheck_updates")
        self.menuOptions.addAction(self.actionSet_api_key)
        self.menuOptions.addAction(self.actionSet_language)
        self.menuOptions.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionView_instructions)
        self.menuHelp.addAction(self.actionCheck_updates)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.datamodeTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Säähavaintodatan lataaja"))
        self.headerLabel_daily.setText(_translate("MainWindow", "Ilmatieteenlaitoksen vuorokausiarvojen lataus"))
        self.placeLabel_daily.setText(_translate("MainWindow", "Paikka:"))
        self.stationComboBox_daily.setToolTip(_translate("MainWindow", "Valitse sääasema, jonka tiedot tahdot ladata"))
        self.availableFromLabel_daily.setText(_translate("MainWindow", "Saatavilla vuodesta:"))
        self.availableDataFromContent_daily.setToolTip(_translate("MainWindow", "Vuosi josta lähtien dataa on saatavilla. Huomaa, että dataa ei välttämättä ole saatavilla vuoden alusta asti! "))
        self.startDatetimeLabel_daily.setText(_translate("MainWindow", "Aloitus pvm:"))
        self.startDatetimeEdit_daily.setToolTip(_translate("MainWindow", "Aloituspäivämäärä, jolta tahdot ladata datan. Ei saa olla sama kuin lopetus päivämäärä."))
        self.endDatetimeLabel_daily.setText(_translate("MainWindow", "Lopetus pvm:"))
        self.endDatetimeEdit_daily.setToolTip(_translate("MainWindow", "Lopetuspäivämäärä, jolta tahdot ladata datan. Ei saa olla sama kuin aloitus päivämäärä."))
        self.downloadButton_daily.setToolTip(_translate("MainWindow", "Lataa data, ja tallenna se tiedostoon"))
        self.downloadButton_daily.setText(_translate("MainWindow", "Lataa"))
        self.datamodeTabWidget.setTabText(self.datamodeTabWidget.indexOf(self.dailytab), _translate("MainWindow", "Vuorokausiarvot"))
        self.datamodeTabWidget.setTabToolTip(self.datamodeTabWidget.indexOf(self.dailytab), _translate("MainWindow", "Ilmatieteenlaitoksen vuorokausiarvojen lataus"))
        self.headerLabel_realtime.setText(_translate("MainWindow", "Ilmatieteenlaitoksen reaaliaika havaintojen lataus"))
        self.placeLabel_realtime.setText(_translate("MainWindow", "Paikka:"))
        self.stationComboBox_realtime.setToolTip(_translate("MainWindow", "Valitse sääasema, jonka tiedot tahdot ladata"))
        self.availableFromLabel_realtime.setText(_translate("MainWindow", "Saatavilla vuodesta:"))
        self.availableFromContent_realtime.setToolTip(_translate("MainWindow", "Vuosi josta lähtien dataa on saatavilla. Huomaa, että dataa ei välttämättä ole saatavilla vuoden alusta asti! "))
        self.availableFromContent_realtime.setText(_translate("MainWindow", "1.1.2010"))
        self.startDatetimeLabel_realtime.setText(_translate("MainWindow", "Aloitus pvm ja aika:"))
        self.endDatetimeLabel_realtime.setText(_translate("MainWindow", "Lopetus pvm ja aika:"))
        self.startDatetimeEdit_realtime.setToolTip(_translate("MainWindow", "Aloituspäivämäärä, jolta tahdot ladata datan. Ei saa olla sama kuin lopetus päivämäärä."))
        self.endDatetimeEdit_realtime.setToolTip(_translate("MainWindow", "Lopetuspäivämäärä, jolta tahdot ladata datan. Ei saa olla sama kuin aloitus päivämäärä."))
        self.downloadButton_realtime.setToolTip(_translate("MainWindow", "Lataa data, ja tallenna se tiedostoon"))
        self.downloadButton_realtime.setText(_translate("MainWindow", "Lataa"))
        self.datamodeTabWidget.setTabText(self.datamodeTabWidget.indexOf(self.realtimetab), _translate("MainWindow", "Reaaliaika havainnot"))
        self.datamodeTabWidget.setTabToolTip(self.datamodeTabWidget.indexOf(self.realtimetab), _translate("MainWindow", "Ilmatieteenlaitoksen reaaliaikaisten havaintojen lataus"))
        self.menuOptions.setTitle(_translate("MainWindow", "Tiedosto"))
        self.menuHelp.setTitle(_translate("MainWindow", "Apua"))
        self.actionSet_api_key.setText(_translate("MainWindow", "Aseta tunnisteavain"))
        self.actionSet_api_key.setToolTip(_translate("MainWindow", "Aseta palvelun käyttöön tarvittava tunnisteavain"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "Tietoa"))
        self.actionAbout.setToolTip(_translate("MainWindow", "Tietoa tästä sovelluksesta"))
        self.actionExit.setText(_translate("MainWindow", "Poistu"))
        self.actionSet_language.setText(_translate("MainWindow", "Aseta kieli"))
        self.actionView_instructions.setText(_translate("MainWindow", "Ohjeet"))
        self.actionCheck_updates.setText(_translate("MainWindow", "Tarkista päivitykset"))

