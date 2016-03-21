# -*- coding: utf-8 -*-

from Librairies.Cryptage import *
from time import *
from os import popen
import os.path
from sys import *
from subprocess import *

# Le programme permet de créer un txt Settings après la création du coffre

txt=open("Settings.txt","r")
settings=txt.read()
key=read_settings(settings)[0]
mdp=read_settings(settings)[1]
statut="OUVERT"
cas=read_settings(settings)[3]
write_settings(key,mdp,statut,cas)
