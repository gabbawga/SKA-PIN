from ..Utils.ConfigColetor import salvar_config
from ..Utils.PendriveUtil import listar_dispositivos_usb_mac

def salvar_config_interface(configServ, configColetor, lblStatus):
        ip_servidor = configServ.get()
        ip_coletor = configColetor.get()

        if not ip_servidor or not ip_coletor:
            lblStatus.config(text="Por favor, preencha ambos os campos!", fg="red")
            return
        #funcao que pega os dados
        else:
            salvar_config(ip_servidor, ip_coletor)
    
    #Alterar o label responsavel pelo Pendrive
def alterar_labelPendrive(lblPendrive):
        pendrive = listar_dispositivos_usb_mac()

        if pendrive:
             lblPendrive.config(text=f"Dispositivo encontrado: {pendrive}")
        else:
            lblPendrive.config(text=f"Dispositivo nao encontrado: {pendrive}")