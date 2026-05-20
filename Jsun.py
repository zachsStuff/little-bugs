
import json


with open("config.json","r") as cfg:
#this may not work at points for somereason, but hopefully its working right now

    data=json.load(cfg)

def load(name: str,data):
    
    return data[name]
def loadFloat(name:str,data):
    
    return float(data[name])
def loadInt(name:str,data):
    
    return int(data[name])


def Wrapload(wraperName:str,name: str,data):
    
    return data[wraperName][name]
def WraploadFloat(wraperName:str,name:str,data):
    
    return float(data[wraperName][name])
def WraploadInt(wraperName:str,name:str,data):
    
    return int(name[wraperName][name])
