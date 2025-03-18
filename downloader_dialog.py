# -*- coding: utf-8 -*-
import os
import urllib.request
import zipfile
from qgis.PyQt.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                               QLineEdit, QPushButton, QFileDialog, QMessageBox,
                               QProgressBar)
from qgis.PyQt.QtCore import Qt, QThread, pyqtSignal
import tempfile

class DownloadThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, url, dest_file):
        super(DownloadThread, self).__init__()
        self.url = url
        self.dest_file = dest_file
    
    def run(self):
        try:
            self.progress.emit(10)
            
            # Baixar o arquivo
            urllib.request.urlretrieve(self.url, self.dest_file)
            
            self.progress.emit(100)
            self.finished.emit(True, self.dest_file)
            
        except Exception as e:
            self.finished.emit(False, str(e))


class DownloaderDialog(QDialog):
    def __init__(self, parent=None):
        super(DownloaderDialog, self).__init__(parent)
        self.thread = None
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle("IBGE Downloader")
        self.resize(500, 150)
        
        # Layout principal
        layout = QVBoxLayout()
        
        # URL
        url_layout = QHBoxLayout()
        url_layout.addWidget(QLabel("URL:"))
        self.url_edit = QLineEdit()
        url_layout.addWidget(self.url_edit)
        layout.addLayout(url_layout)
        
        # Pasta de destino
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(QLabel("Pasta de destino:"))
        self.folder_edit = QLineEdit()
        self.folder_edit.setText(os.path.join(tempfile.gettempdir(), "ibge_data"))
        folder_layout.addWidget(self.folder_edit)
        browse_button = QPushButton("Procurar...")
        browse_button.clicked.connect(self.browse_folder)
        folder_layout.addWidget(browse_button)
        layout.addLayout(folder_layout)
        
        # Barra de progresso
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Botões
        button_layout = QHBoxLayout()
        
        self.download_button = QPushButton("Baixar")
        self.download_button.clicked.connect(self.download)
        button_layout.addWidget(self.download_button)
        
        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self, "Selecionar pasta de destino", self.folder_edit.text()
        )
        if folder:
            self.folder_edit.setText(folder)
    
    def download(self):
        url = self.url_edit.text().strip()
        if not url:
            QMessageBox.warning(self, "Aviso", "Por favor, informe uma URL.")
            return
        
        dest_folder = self.folder_edit.text()
        if not os.path.exists(dest_folder):
            try:
                os.makedirs(dest_folder)
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Não foi possível criar a pasta: {str(e)}")
                return
        
        # Extrair o nome do arquivo da URL
        filename = url.split('/')[-1]
        if not filename:
            filename = "download.zip"
        
        dest_file = os.path.join(dest_folder, filename)
        
        # Mostrar barra de progresso
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Iniciar download em uma thread separada
        self.thread = DownloadThread(url, dest_file)
        self.thread.progress.connect(self.update_progress)
        self.thread.finished.connect(self.download_finished)
        self.thread.start()
    
    def update_progress(self, value):
        self.progress_bar.setValue(value)
    
    def download_finished(self, success, result):
        self.progress_bar.setVisible(False)
        
        if success:
            QMessageBox.information(
                self, "Sucesso", f"Arquivo baixado com sucesso em:\n{result}"
            )
            
            # Perguntar se deseja extrair o arquivo, se for um ZIP
            if result.lower().endswith('.zip'):
                reply = QMessageBox.question(
                    self, "Extrair arquivo", 
                    "Deseja extrair o arquivo ZIP?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
                )
                
                if reply == QMessageBox.Yes:
                    try:
                        extract_folder = os.path.splitext(result)[0]
                        if not os.path.exists(extract_folder):
                            os.makedirs(extract_folder)
                            
                        with zipfile.ZipFile(result, 'r') as zip_ref:
                            zip_ref.extractall(extract_folder)
                            
                        QMessageBox.information(
                            self, "Sucesso", 
                            f"Arquivo extraído com sucesso em:\n{extract_folder}"
                        )
                    except Exception as e:
                        QMessageBox.warning(
                            self, "Erro", 
                            f"Não foi possível extrair o arquivo: {str(e)}"
                        )
        else:
            QMessageBox.warning(
                self, "Erro", f"Erro ao baixar o arquivo:\n{result}"
            )