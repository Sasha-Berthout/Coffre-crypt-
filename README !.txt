[Programme]

Il y a 3 programmes importants dans ce coffre:

- Coffre
- Configuration
- D�cryptage

ATTENTION : Il faut �viter de lancer les .bat car cela destabilise le bon fonctionnement du coffre et peut amener � des contradictions entre les diff�rents fichiers.

Le programme n'est pas compatible avec les ordinateurs ayant un syst�me d'explotation autre que WINDOWS et n�cessite python 3.5

[Utilisation]

- Coffre est le programme principal, celui qui permet d'ouvrir le coffre avec le mot de passe correct ou de le fermer.

- Configuration est le programme qui permet de modifier le mot de passe du coffre ou de changer la cl�, biens�r lui-m�me prot�g� par un mot de passe (Passe).

- D�cryptage est le programme pour d�crypter un mot � l'aide d'une cl� (pas besoin de rentrer la cl�)

- Settings donne toutes les informations requises sur le coffre:

1. La cl�
2. Le mot de passe crypt�
3. Le statut du coffre
4. 1=activ� et 0=d�sactiv�, X1 indique qu'il y a un doublon a la place (position=num�ro qui suit le point) et W1 
indique qu'il y a un W a la place (position=num�ro qui suit le point)


[Explication]

 CMD:

": x" exprime une fonction "x", c'est l'�quivalent de "def" en python.

"goto + x" �x�cute la fonction x.

"Exist" est un test pour savoir si le fichier existe ou pas.

" ren "x" "y" " permet de rename x en y.

"attrib" permet de cacher le coffre si il y a des "+" devant les attributs et enl�ve les attributs pour cacher si il y a un "-".

"echo" est un �quivalent de "print".

"md + x" permet de cr�er un dossier avec le nom "x".

"start" permet d'�x�cuter un fichier.

"echo "x" > y.txt" permet d'�crire x dans y.txt, cette commande est utilis�e pour cr�er un .txt.

 Python:

- Pour les librairies c'est normal qu'il y est � chaque fois (dans les diff�rents fichiers) les m�mes d�fintions mais c'est la seule solution � l'erreur
(function is not definied) que nous avons trouv�.