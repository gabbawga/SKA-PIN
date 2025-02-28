from tkinter import *
import os
from .ConfigColetor import salvar_config
from .PendriveUtil import listar_dispositivos_usb_mac

def criar_interface():

#Funcoes de interface

    #Salvar os dados inputados pelo usuário
    def salvar_config_interface():
        ip_servidor = configServ.get()
        ip_coletor = configColetor.get()

        if not ip_servidor or not ip_coletor:
            lblStatus.config(text="Por favor, preencha ambos os campos!", fg="red")
            return
        #funcao que pega os dados
        else:
            salvar_config(ip_servidor, ip_coletor)
    
    #Alterar o label responsavel pelo Pendrive
    def alterar_labelPendrive():
        pendrive = listar_dispositivos_usb_mac()

        if pendrive:
             lblPendrive.config(text=f"Dispositivo encontrado: {pendrive}")
        else:
            lblPendrive.config(text=f"Dispositivo nao encontrado: {pendrive}")

    root = Tk()
    root.title("SKA-Pin")
    root.geometry('500x400')

    #Verificacao Pendrive
    lblPendrive = Label(root, text="Nenhum dispositivo encontrado")
    lblPendrive.grid(row=0, column=0)

    btnEncontrarPendrive = Button(root, text="Encontrar Pendrive", fg="red", command=alterar_labelPendrive)
    btnEncontrarPendrive.grid(row=0, column=1)

    #Servidor Config
    lblServidor = Label(root, text="IP do Servidor")
    lblServidor.grid(row=1, column=0, pady=10)

    configServ = Entry(root, width=15)
    configServ.grid(row=1, column=1)
    

    #Coletor Config
    lblColetor = Label(root, text="IP do Coletor")
    lblColetor.grid(row=2, column=0)

    configColetor = Entry(root, width=15)
    configColetor.grid(row=2, column=1)

    btnSalvar = Button(root, text="Salvar no pendrive", fg="red", command=salvar_config_interface)
    btnSalvar.grid(row=11, column=1)

    lblStatus = Label(root, text="", fg="black")
    lblStatus.grid(row=9, column=1)

    root.mainloop()
