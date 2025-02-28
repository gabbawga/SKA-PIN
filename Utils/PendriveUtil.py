import os


def listar_dispositivos_usb_mac():
    volumes = os.listdir("/Volumes/")  # Lista os dispositivos montados em /Volumes/
    pendrives = [f"/Volumes/{vol}" for vol in volumes if vol not in ["Macintosh HD"]]
    
    

    return pendrives

# Testando a função
pendrives = listar_dispositivos_usb_mac()

if pendrives:
    print("Pendrive detectado:", pendrives)
else:
    print("Nenhum pendrive encontrado.")
