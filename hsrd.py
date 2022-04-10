import random
import os
from colorama import Fore, Style
import webbrowser

mf = "Mots fantômes"

sujets = [
		mf,
		"Yaourt/topline",
		"Algorithmes génétiques",
		"Gratuité de l'aléatoire",
		"La Randomization (RANDOMIZER) dans les DAWs",
		"Musique stochastique",
		"Esquisse"
		]

couleurs = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
couleur_courante = random.choice(couleurs)

random.seed(None) # Le seed est initialisé sur le temps de l'horloge
random.shuffle(sujets)
random.shuffle(couleurs)

def sujet():
	try:
		print('\n')
		sujet = sujets.pop(0)
		printCenteredText(setColor() + Style.BRIGHT + sujet)
		if sujet == mf: motsFantomes()
		print('\n')
	except IndexError:
		print(Style.RESET_ALL + "Plus de sujets, c'est fini !")

def motsFantomes():
	global sujets
	if "Algorithmes génétiques" in sujets:
		print("Ce serait quand même mieux de parler des algorithmes génétiques avant... Autre sujet !")
		sujet()
		sujets += [mf]
	else:
		print("Ouverture de la page web...")
		webbrowser.open('base_mots_fantomes.html')
		print("Page ouverte !")

def setColor():
	global couleur_courante
	couleur = couleur_courante
	while(couleur == couleur_courante):
		couleur = random.choice(couleurs)
	couleur_courante = couleur
	return couleur_courante

def printCenteredText(s):
	rows, columns = os.popen('stty size', 'r').read().split()
	print(s.center(int(columns)))