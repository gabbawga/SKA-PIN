import os


def listDevices():
    volumes = os.listdir("/Volumes/")  # Lista os dispositivos montados em /Volumes/
    pendrives = [f"/Volumes/{vol}" for vol in volumes if vol not in ["Macintosh HD"]]
    
    return pendrives

# Testando a função
pendrives = listDevices()

if pendrives:
    print("Pendrive detectado:", pendrives)
else:
    print("Nenhum pendrive encontrado.")
