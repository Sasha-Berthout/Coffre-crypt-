# -*- coding: utf-8 -*-

from Librairies.Cryptage import *
from time import *
from os import popen
import os.path
from sys import *
from subprocess import *

txt=open("Settings.txt","r")
settings=txt.read()
key=read_settings(settings)[0]
mdp=read_settings(settings)[1]
statut=read_settings(settings)[2]
cas=read_settings(settings)[3]
L=grille(key)
mdp=input("Entrez le mot de passe=")
print("")
if mdp=="Passe":
    new_config(mdp,key,statut,cas)
else:
    print("Mot de passe: Incorrect!")
    config=False
    popen("Relance_config.bat")
    exit(0)
    
