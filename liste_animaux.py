#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
#
#  Exos Introduction à python
"""
ENONCE : Voir file Exercice1-1.pdf
"""

# ~ ### PARTIE 1
# ~ # PARTIE 1.1
the_liste = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]

for i in the_liste :
	print (i)
	
# PARTIE 1.2
the_liste.reverse()
print (the_liste)
 
 # PARTIE 1.3
the_liste.sort()
print (the_liste)
 
 # PARTIE 1.4
the_liste.append("troll")
domestic_liste = ["lapin", "chat", "chien", "chiot"]
for i in domestic_liste:
	the_liste.remove(i)
print (the_liste)



### PARTIE 2
# PARTIE 2.1
import random

tableau_jeu = []
for i in range(0,10) :
	tableau_jeu.append(random.randint(1,10))
	
valeur = int(input ("Donnez-moi un nombre entre 1 et 10 : "))

compteur = 0
for i in tableau_jeu :
	if i == valeur :
		print ("Gagné !")
		compteur = 1
		break
	else :
		continue

if compteur == 0 :
	print("Perdu !")

# PARTIE 2.2
import random

tableau_jeu = []
for i in range(0,10) :
	tableau_jeu.append(random.randint(1,10))
tableau_jeu.sort()
print(tableau_jeu)    ###
	
valeur = int(input ("Donnez-moi un nombre entre 1 et 10 : "))

compteur = 0
for i in tableau_jeu :
	if i == valeur :
		print ("Gagné !")
		compteur = 1
		break
	elif i > valeur :
		print("Perdu !")
		compteur = 1
		break
	else :
		continue
	
if compteur == 0 :
	print("Perdu !")
	

