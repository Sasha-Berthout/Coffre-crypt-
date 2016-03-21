@echo off
@title Coffre
if EXIST Coffre goto ferme
if NOT EXIST Coffre goto coffre
if NOT EXIST Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D} goto coffre
:ferme
ren Coffre "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Dossier Coffre verouille
goto fin
:niet
echo Mot de passe incorect
goto fin
:coffre
md Coffre
echo Le dossier Coffre est cree
start Relance_settings.py
goto fin
:fin
pause