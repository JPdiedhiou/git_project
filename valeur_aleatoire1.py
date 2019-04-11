x=print("Hello, World")
#Génèrence d'un nombre aléatoire
import random
nbre_alea = random.randint(0, 9)
#Initialisation de la réponse de l'utilisateur
rep_user = None
#Définition du nombre de tentative
for i in range(3):
#Établissement comparaison avec la valeur entrée par l'utilisateur
      if rep_user != nbre_alea:
         rep_user = int(input("Entrer une valeur entre 0 et 9 :"))
      if rep_user < nbre_alea:
         print("Le nombre aléatoire est plus petit")
      elif rep_user > nbre_alea:
         print("Le nombre aléatoire est plus petit")
      else:
         print("Bravo !! Tu as gagné ")

#!print("Désolé, le nombre de tentative est épuisé")
