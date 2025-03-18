# -*- coding: utf-8 -*-
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
import os.path

from .downloader_dialog import DownloaderDialog

class IBGEDownloader:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []
        self.menu = 'IBGE Downloader'
        self.toolbar = self.iface.addToolBar('IBGE Downloader')
        self.toolbar.setObjectName('IBGEDownloader')

    def add_action(self, icon_path, text, callback, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        self.toolbar.addAction(action)
        self.iface.addPluginToMenu(self.menu, action)
        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        if not os.path.exists(icon_path):
            icon_path = ":/images/themes/default/mActionAddLayer.svg"
            
        self.add_action(
            icon_path,
            text="IBGE Downloader",
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu('IBGE Downloader', action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def run(self):
        dialog = DownloaderDialog(self.iface.mainWindow())
        dialog.exec_()