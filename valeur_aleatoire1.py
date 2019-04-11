import sys
#Génèrence d'un nombre aléatoire
import random
nbre_alea = random.randint(0, 9)
#Initialisation de la réponse de l'utilisateur
rep_user = None
print(nbre_alea)
#Limitation du message rendu en cas de victoir au 1er coup

#Définition du nombre de tentative
for i in range(3):
#Établissement comparaison avec la valeur entrée par l'utilisateur
      if rep_user != nbre_alea:
         rep_user = int(input("Entrer une valeur entre 0 et 9 :"))
      if rep_user < nbre_alea:
         print("Le nombre aléatoire est plus grand")
      elif rep_user > nbre_alea:
         print("Le nombre aléatoire est plus petit")
      else:
         print("Bravo !! Tu as gagné ")
         sys.exit()
         print("Désolé, le nombre de tentative est épuisé")
