# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serverwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_ServerWindow(object):
    def setupUi(self, ServerWindow):
        if not ServerWindow.objectName():
            ServerWindow.setObjectName(u"ServerWindow")
        ServerWindow.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServerWindow.sizePolicy().hasHeightForWidth())
        ServerWindow.setSizePolicy(sizePolicy)
        ServerWindow.setMinimumSize(QSize(900, 600))
        ServerWindow.setMaximumSize(QSize(900, 600))
        self.aMenuSaveConfig = QAction(ServerWindow)
        self.aMenuSaveConfig.setObjectName(u"aMenuSaveConfig")
        self.aMenuOpenConfig = QAction(ServerWindow)
        self.aMenuOpenConfig.setObjectName(u"aMenuOpenConfig")
        self.aMenuQuit = QAction(ServerWindow)
        self.aMenuQuit.setObjectName(u"aMenuQuit")
        self.actionAbout = QAction(ServerWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(ServerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grpRadioList = QGroupBox(self.centralwidget)
        self.grpRadioList.setObjectName(u"grpRadioList")
        self.grpRadioList.setGeometry(QRect(10, 10, 471, 531))
        self.fAddRadio = QPushButton(self.grpRadioList)
        self.fAddRadio.setObjectName(u"fAddRadio")
        self.fAddRadio.setGeometry(QRect(10, 480, 111, 41))
        self.fEditRadio = QPushButton(self.grpRadioList)
        self.fEditRadio.setObjectName(u"fEditRadio")
        self.fEditRadio.setGeometry(QRect(130, 480, 111, 41))
        self.fDeleteRadio = QPushButton(self.grpRadioList)
        self.fDeleteRadio.setObjectName(u"fDeleteRadio")
        self.fDeleteRadio.setGeometry(QRect(250, 480, 111, 41))
        self.fRadioList = QTreeWidget(self.grpRadioList)
        self.fRadioList.setObjectName(u"fRadioList")
        self.fRadioList.setGeometry(QRect(10, 31, 451, 431))
        self.grpRadioSettings = QGroupBox(self.centralwidget)
        self.grpRadioSettings.setObjectName(u"grpRadioSettings")
        self.grpRadioSettings.setGeometry(QRect(489, 10, 401, 531))
        self.gridLayoutWidget = QWidget(self.grpRadioSettings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 29, 381, 431))
        self.grdRadioSettings = QGridLayout(self.gridLayoutWidget)
        self.grdRadioSettings.setObjectName(u"grdRadioSettings")
        self.grdRadioSettings.setHorizontalSpacing(10)
        self.grdRadioSettings.setVerticalSpacing(5)
        self.grdRadioSettings.setContentsMargins(10, 5, 10, 5)
        self.lblRadioRxAud = QLabel(self.gridLayoutWidget)
        self.lblRadioRxAud.setObjectName(u"lblRadioRxAud")
        self.lblRadioRxAud.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioRxAud, 5, 0, 1, 1)

        self.lblRadioSigId = QLabel(self.gridLayoutWidget)
        self.lblRadioSigId.setObjectName(u"lblRadioSigId")
        self.lblRadioSigId.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioSigId, 7, 0, 1, 1)

        self.lblRadioDesc = QLabel(self.gridLayoutWidget)
        self.lblRadioDesc.setObjectName(u"lblRadioDesc")
        self.lblRadioDesc.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioDesc, 1, 0, 1, 1)

        self.lblRadioTxAud = QLabel(self.gridLayoutWidget)
        self.lblRadioTxAud.setObjectName(u"lblRadioTxAud")
        self.lblRadioTxAud.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioTxAud, 4, 0, 1, 1)

        self.fEditRadioSigMode = QComboBox(self.gridLayoutWidget)
        self.fEditRadioSigMode.setObjectName(u"fEditRadioSigMode")
        self.fEditRadioSigMode.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioSigMode, 6, 1, 1, 1)

        self.fEditRadioName = QLineEdit(self.gridLayoutWidget)
        self.fEditRadioName.setObjectName(u"fEditRadioName")
        self.fEditRadioName.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioName, 0, 1, 1, 1)

        self.fEditRadioCtrlPort = QComboBox(self.gridLayoutWidget)
        self.fEditRadioCtrlPort.setObjectName(u"fEditRadioCtrlPort")
        self.fEditRadioCtrlPort.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioCtrlPort, 3, 1, 1, 1)

        self.fEditRadioDesc = QLineEdit(self.gridLayoutWidget)
        self.fEditRadioDesc.setObjectName(u"fEditRadioDesc")
        self.fEditRadioDesc.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioDesc, 1, 1, 1, 1)

        self.fEditRadioRxAud = QComboBox(self.gridLayoutWidget)
        self.fEditRadioRxAud.setObjectName(u"fEditRadioRxAud")
        self.fEditRadioRxAud.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioRxAud, 5, 1, 1, 1)

        self.fEditRadioSigId = QLineEdit(self.gridLayoutWidget)
        self.fEditRadioSigId.setObjectName(u"fEditRadioSigId")
        self.fEditRadioSigId.setEnabled(False)
        self.fEditRadioSigId.setMaxLength(8)

        self.grdRadioSettings.addWidget(self.fEditRadioSigId, 7, 1, 1, 1)

        self.lblRadioName = QLabel(self.gridLayoutWidget)
        self.lblRadioName.setObjectName(u"lblRadioName")
        self.lblRadioName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioName, 0, 0, 1, 1)

        self.lblRadioCtrlPort = QLabel(self.gridLayoutWidget)
        self.lblRadioCtrlPort.setObjectName(u"lblRadioCtrlPort")
        self.lblRadioCtrlPort.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioCtrlPort, 3, 0, 1, 1)

        self.lblRadioSigMode = QLabel(self.gridLayoutWidget)
        self.lblRadioSigMode.setObjectName(u"lblRadioSigMode")
        self.lblRadioSigMode.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioSigMode, 6, 0, 1, 1)

        self.lblRadioCtrlMode = QLabel(self.gridLayoutWidget)
        self.lblRadioCtrlMode.setObjectName(u"lblRadioCtrlMode")
        self.lblRadioCtrlMode.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grdRadioSettings.addWidget(self.lblRadioCtrlMode, 2, 0, 1, 1)

        self.fEditRadioTxAud = QComboBox(self.gridLayoutWidget)
        self.fEditRadioTxAud.setObjectName(u"fEditRadioTxAud")
        self.fEditRadioTxAud.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioTxAud, 4, 1, 1, 1)

        self.fEditRadioCtrlMode = QComboBox(self.gridLayoutWidget)
        self.fEditRadioCtrlMode.setObjectName(u"fEditRadioCtrlMode")
        self.fEditRadioCtrlMode.setEnabled(False)

        self.grdRadioSettings.addWidget(self.fEditRadioCtrlMode, 2, 1, 1, 1)

        self.fConnectRadio = QPushButton(self.grpRadioSettings)
        self.fConnectRadio.setObjectName(u"fConnectRadio")
        self.fConnectRadio.setEnabled(False)
        self.fConnectRadio.setGeometry(QRect(10, 480, 111, 41))
        self.fDisconnectRadio = QPushButton(self.grpRadioSettings)
        self.fDisconnectRadio.setObjectName(u"fDisconnectRadio")
        self.fDisconnectRadio.setEnabled(False)
        self.fDisconnectRadio.setGeometry(QRect(130, 480, 111, 41))
        self.lblSelectedRadioStatus = QLabel(self.grpRadioSettings)
        self.lblSelectedRadioStatus.setObjectName(u"lblSelectedRadioStatus")
        self.lblSelectedRadioStatus.setGeometry(QRect(250, 480, 141, 41))
        ServerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ServerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        ServerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ServerWindow)
        self.statusbar.setObjectName(u"statusbar")
        ServerWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.fRadioList, self.fAddRadio)
        QWidget.setTabOrder(self.fAddRadio, self.fEditRadio)
        QWidget.setTabOrder(self.fEditRadio, self.fDeleteRadio)
        QWidget.setTabOrder(self.fDeleteRadio, self.fEditRadioName)
        QWidget.setTabOrder(self.fEditRadioName, self.fEditRadioDesc)
        QWidget.setTabOrder(self.fEditRadioDesc, self.fEditRadioCtrlMode)
        QWidget.setTabOrder(self.fEditRadioCtrlMode, self.fEditRadioCtrlPort)
        QWidget.setTabOrder(self.fEditRadioCtrlPort, self.fEditRadioTxAud)
        QWidget.setTabOrder(self.fEditRadioTxAud, self.fEditRadioRxAud)
        QWidget.setTabOrder(self.fEditRadioRxAud, self.fEditRadioSigMode)
        QWidget.setTabOrder(self.fEditRadioSigMode, self.fEditRadioSigId)
        QWidget.setTabOrder(self.fEditRadioSigId, self.fConnectRadio)
        QWidget.setTabOrder(self.fConnectRadio, self.fDisconnectRadio)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.aMenuSaveConfig)
        self.menu_File.addAction(self.aMenuOpenConfig)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.aMenuQuit)
        self.menu_Help.addAction(self.actionAbout)

        self.retranslateUi(ServerWindow)

        QMetaObject.connectSlotsByName(ServerWindow)
    # setupUi

    def retranslateUi(self, ServerWindow):
        ServerWindow.setWindowTitle(QCoreApplication.translate("ServerWindow", u"Radio Console Server", None))
        self.aMenuSaveConfig.setText(QCoreApplication.translate("ServerWindow", u"&Save Config", None))
        self.aMenuOpenConfig.setText(QCoreApplication.translate("ServerWindow", u"&Open Config", None))
        self.aMenuQuit.setText(QCoreApplication.translate("ServerWindow", u"&Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("ServerWindow", u"About", None))
        self.grpRadioList.setTitle(QCoreApplication.translate("ServerWindow", u"Radio List", None))
        self.fAddRadio.setText(QCoreApplication.translate("ServerWindow", u"Add", None))
        self.fEditRadio.setText(QCoreApplication.translate("ServerWindow", u"Edit", None))
        self.fDeleteRadio.setText(QCoreApplication.translate("ServerWindow", u"Delete", None))
        ___qtreewidgetitem = self.fRadioList.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("ServerWindow", u"Status", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("ServerWindow", u"Description", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ServerWindow", u"Name", None));
        self.grpRadioSettings.setTitle(QCoreApplication.translate("ServerWindow", u"Radio Settings", None))
        self.lblRadioRxAud.setText(QCoreApplication.translate("ServerWindow", u"Receive Audio", None))
        self.lblRadioSigId.setText(QCoreApplication.translate("ServerWindow", u"Signalling ID", None))
        self.lblRadioDesc.setText(QCoreApplication.translate("ServerWindow", u"Description", None))
        self.lblRadioTxAud.setText(QCoreApplication.translate("ServerWindow", u"Transmit Audio", None))
        self.lblRadioName.setText(QCoreApplication.translate("ServerWindow", u"Name", None))
        self.lblRadioCtrlPort.setText(QCoreApplication.translate("ServerWindow", u"Control Port", None))
        self.lblRadioSigMode.setText(QCoreApplication.translate("ServerWindow", u"Signalling", None))
        self.lblRadioCtrlMode.setText(QCoreApplication.translate("ServerWindow", u"Control Mode", None))
        self.fConnectRadio.setText(QCoreApplication.translate("ServerWindow", u"Connect", None))
        self.fDisconnectRadio.setText(QCoreApplication.translate("ServerWindow", u"Disconnect", None))
        self.lblSelectedRadioStatus.setText(QCoreApplication.translate("ServerWindow", u"No Radio Selected", None))
        self.menu_File.setTitle(QCoreApplication.translate("ServerWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("ServerWindow", u"&Help", None))
    # retranslateUi

