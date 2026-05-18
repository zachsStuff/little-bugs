
import json

#idk if i should put this in a function but who cares
with open("config.json","r") as cfg:
#this may not work at points for somereason, but hopefully its working right now

    data=json.load(cfg)

def load(name: str):
    global data
    return data[name]
def loadFloat(name:str):
    global data
    return float(data[name])
def loadInt(name:str):
    global data
    return int(data[name])


def Wrapload(wraperName:str,name: str):
#>realisticly i dont see myself ever wrapping<#
#>           a thing beyond once             <#
#>  so this should work for now, dont touch!!<#
    global data
    return data[wraperName][name]
def WraploadFloat(wraperName:str,name:str):
    global data
    return float(data[wraperName][name])
def WraploadInt(wraperName:str,name:str):
    global data
    return int(name[wraperName][name])
