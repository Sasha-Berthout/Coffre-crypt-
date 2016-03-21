# Cryptage-de-Coffre
Programme : Projet ISN 2015

[Programme]

Il y a 3 programmes importants dans ce coffre:

- Coffre
- Configuration
- Décryptage

ATTENTION : Il faut éviter de lancer les .bat car cela destabilise le bon fonctionnement du coffre et peut amener à des contradictions entre les différents fichiers.


Le programme n'est pas compatible avec les ordinateurs ayant un système d'explotation autre que WINDOWS et nécessite python 3.5


[Utilisation]

- Coffre est le programme principal, celui qui permet d'ouvrir le coffre avec le mot de passe correct ou de le fermer.

- Configuration est le programme qui permet de modifier le mot de passe du coffre ou de changer la clé, biensur lui-même protégé par un mot de passe (Passe).

- Décryptage est le programme pour décrypter un mot à l'aide d'une clé (pas besoin de rentrer la clé)

- Settings donne toutes les informations requises sur le coffre:
1. La clé
2. Le mot de passe crypté
3. Le statut du coffre
4. 1=activé et 0=désactivé, X1 indique qu'il y a un doublon a la place (position=numéro qui suit le point) et W1 
indique qu'il y a un W a la place (position=numéro qui suit le point)


[Explication]

 CMD:

": x" exprime une fonction "x", c'est l'équivalent de "def" en python.

"goto + x" éxécute la fonction x.

"Exist" est un test pour savoir si le fichier existe ou pas.

" ren "x" "y" " permet de rename x en y.

"attrib" permet de cacher le coffre si il y a des "+" devant les attributs et enlève les attributs pour cacher si il y a un "-".

"echo" est un équivalent de "print".

"md + x" permet de créer un dossier avec le nom "x".

"start" permet d'éxécuter un fichier.

"echo "x" > y.txt" permet d'écrire x dans y.txt, cette commande est utilisée pour créer un .txt.

 Python:

- Pour les librairies c'est normal qu'
il y est à chaque fois (dans les différents fichiers) les mêmes défintions mais c'est la seule solution à l'erreur
(function is not definied) que nous avons trouvé.
