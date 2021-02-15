# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

import os, time
import psutil
from datetime import datetime, timezone

class InfoArquivos():
    def __init__(self, nome, tamanho, data_adicionado, data_alterado):
        self.nome = nome
        self.tamanho = tamanho // 1024
        self.data_adicionado = datetime.fromtimestamp(data_adicionado, tz=timezone.utc).strftime('%d/%m/%Y %H:%M')
        self.data_alterado = datetime.fromtimestamp(data_alterado, tz=timezone.utc).strftime('%d/%m/%Y %H:%M')

# Create your views here.
def arquivos(request):
    caminho = '/Users/jeffersonsouza/Downloads/'
    lista_arquivos = os.listdir(caminho)

    lista = []

    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)
        if os.path.isfile(caminho_arquivo):
            detalhes = os.stat(caminho_arquivo)
            info = InfoArquivos(arquivo, detalhes.st_size, detalhes.st_atime, detalhes.st_mtime)
            lista.append(info)

    return render(request, 'lista_arquivos.html', { "lista": lista })

def processos(request):
    lista_processos = []

    for processo in psutil.process_iter():
        lista_processos.append(processo.as_dict(['pid', 'name', 'status', 'cpu_times', 'memory_info']))

    return render(request, 'lista_processos.html', { "processos": lista_processos })

def processo(request, pid):
    lista_processos = []

    for processo in psutil.process_iter():
        lista_processos.append(processo.as_dict(['pid', 'name', 'status', 'cpu_times', 'memory_info']))

    return render(request, 'detalhe_processo.html', { "processo": lista_processos })
