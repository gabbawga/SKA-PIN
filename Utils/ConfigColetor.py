import json
import os

def getConfig(ip_servidor, ip_coletor):
    data = {
        "ip_servidor": ip_servidor,
        "ip_coletor": ip_coletor
    }

    print("dados chegou aqui", data["ip_servidor"])


