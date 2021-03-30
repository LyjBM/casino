#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-
#
#  Exos Introduction à python
"""
ENONCE : Voir file Notre sujet Casino.docx
"""

import random, time, math

print ("==================== Bienvenue dans notre casino ====================\n\n")

k = 1
while k != 0:
	try:
		argent = int(input ("Avec combien d'euros arrivez-vous ? (ex: 150, 3000) "))
		break
	except:
		print ("?? Je n'ai pas compris...")

i = 1
while i != 0:
	numero = int(input ("\nSur quelle case allez-vous miser ? (0 à 49)"))
	while numero < 0 or numero > 49 :
		print ("\nCette case n'existe pas sur notre roulette !")
		numero = int(input ("Sur quelle case allez-vous miser ? (0 à 49)"))
	
	mise = int(input (f"Votre cagnotte est de {argent} euros. Combien allez-vous mettre en euros ? "))
	while mise > argent :
		print (f"Vous n'avez pas assez d'argent ! Vous pouvez misez au maximum {argent} euros.")
		mise = int(input ("Combien allez-vous mettre en euros ? "))
	
	print ("\n\n--------------- Le croupier lance la roue")
	time.sleep(1)
	print ("---------- La boule tourne")
	time.sleep(1)
	print ("----- La boule c'est arrêtée sur la case ", end=" ")
	
	case = random.randrange(50)
	if numero == case:
		gain =  mise * 3
		argent = argent + gain
		print (f"{case}\n\n Magnifique !! Vous triplez votre mise et remportez {gain} euros.")
	elif numero % 2 == 0 and case % 2 == 0 :
		gain =  mise + math.ceil(mise/2)
		argent = argent + gain
		print (f"{case}\n\n Génial !! Votre case et la chance sont toutes les deux de couleur noir ! Vous remportez {gain} euros.")
	elif numero % 2 != 0 and case % 2 != 0 :
		gain =  mise + math.ceil(mise/2)
		argent = argent + gain
		print (f"{case}\n\n Génial !! Votre case et la chance sont toutes les deux de couleur rouge ! Vous remportez {gain} euros.")
	else :
		argent = argent - mise
		print (f"{case}\n\n Vous avez perdu {mise} euros.")
		if argent == 0 :
			i = 1
			print ("Vous ne pouvez plus jouer.\n==================== A bientôt ====================\n\n\n")
		else:
			pass
		
	relance = input ("\n\nVoulez-vous rejouer ? [o|n] ")
	j = 1
	while j != 0:
		if relance == "o" or relance == "O" :
			i = 1
			j = 0
		elif relance == "n" or relance == "N" :
			i = 0
			print ("==================== A bientôt ====================\n\n\n")
			j = 0
		else:
			relance = input ("Voulez-vous rejouer ? [o|n] ")
			print ("Je suis désolé, je n'ai pas compris!")





