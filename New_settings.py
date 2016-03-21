# -*- coding: utf-8 -*-

from Librairies.Cryptage import *
from time import *
from os import popen
import os.path
from sys import *
from subprocess import *

# Le programme permet de créer le fichier txt Settings

txt=open("Settings.txt","a")
key="BYDGZJSFUPLARKXCOIVEQNMHT"
mdp="DFJZ"
statut="OUVERT"
cas="0.0.0.0"
write_settings(key,mdp,statut,cas)
print("Le mot de passe par défaut est Mdp")
Popen("Ouverture.bat")
sleep(3)
