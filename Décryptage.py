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
entree=input("Entrez le mot crypté=")
print("Le mot crypté était :")
new_mdp=decryptage(key,entree)
print("")
print(new_mdp)
sleep(3)
