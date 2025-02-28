from Utils.ConfigColetor import getConfig
from Utils.PendriveUtil import listDevices

def saveConfigColetor(configServ, configColetor, lblStatus):
        ip_servidor = configServ.get()
        ip_coletor = configColetor.get()

        if not ip_servidor or not ip_coletor:
            lblStatus.config(text="Por favor, preencha ambos os campos!", fg="red")
            return
        #funcao que pega os dados
        else:
            getConfig(ip_servidor, ip_coletor)
    
    #Alterar o label responsavel pelo Pendrive
def updateLabelPendrive(lblPendrive):
        pendrive = listDevices()

        if pendrive:
             lblPendrive.config(text=f"Dispositivo encontrado: {pendrive}")
        else:
            lblPendrive.config(text=f"Dispositivo nao encontrado: {pendrive}")