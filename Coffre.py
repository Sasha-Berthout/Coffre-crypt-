# -*- coding: utf-8 -*-

from Librairies.Cryptage import *
from time import *
from os import popen
import os.path
from sys import *
from subprocess import *

if os.path.isfile("Settings.txt")==False:
    Popen("New_settings.bat")
    exit(0)        
txt=open("Settings.txt","r")
settings=txt.read()
key=read_settings(settings)[0]
mdp=read_settings(settings)[1]
statut=read_settings(settings)[2]
cas=read_settings(settings)[3]
L=grille(key)
if statut=="OUVERT":
    write_settings(key,mdp,"FERME",cas)
    Popen("Coffre.bat")
    exit(0)
entree=input("Entrez le mot de passe=")
entree=minmaj(entree)
entree,cas=correction_mdp(entree)
cas=read_settings(settings)[3]
entree=comp_key(entree)
newcode=cryptage(entree,key)
print("")
if newcode==mdp:
    sleep(1)
    print("",end="")
    sleep(1)
    print("",end="")
    sleep(1)
    print("Correct!")
    print("")
    write_settings(key,mdp,"OUVERT",cas)
    Popen("Ouverture.bat")
else:
    sleep(1)
    print("",end="")
    sleep(1)
    print("",end="")
    sleep(1)
    print("Incorrect!")
    popen("Relance.bat")
