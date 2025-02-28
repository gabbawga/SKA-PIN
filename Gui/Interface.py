from tkinter import *
from .UtilsGui import updateLabelPendrive, saveConfigColetor

def criar_interface():
   
    root = Tk()
    root.title("SKA-Pin")
    root.geometry('500x400')

    # Verificacao Pendrive
    lblPendrive = Label(root, text="Nenhum dispositivo encontrado")
    lblPendrive.grid(row=0, column=0)

    btnEncontrarPendrive = Button(root, text="Encontrar Pendrive", fg="red", command=lambda: updateLabelPendrive(lblPendrive))
    btnEncontrarPendrive.grid(row=0, column=1)

    # Servidor Config
    lblServidor = Label(root, text="IP do Servidor")
    lblServidor.grid(row=1, column=0, pady=10)

    configServ = Entry(root, width=15)
    configServ.grid(row=1, column=1)
    
    # Coletor Config
    lblColetor = Label(root, text="IP do Coletor")
    lblColetor.grid(row=2, column=0)

    configColetor = Entry(root, width=15)
    configColetor.grid(row=2, column=1)

    lblStatus = Label(root, text="", fg="black")
    lblStatus.grid(row=9, column=1)

    btnSalvar = Button(root, text="Salvar no pendrive", fg="red", command=lambda: saveConfigColetor(configServ, configColetor, lblStatus))
    btnSalvar.grid(row=11, column=1)

    root.mainloop()