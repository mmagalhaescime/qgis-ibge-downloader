# -*- coding: utf-8 -*-
"""
Arquivo de inicialização do plugin IBGE Downloader.
"""
def classFactory(iface):
    from .ibge_downloader import IBGEDownloader
    return IBGEDownloader(iface)