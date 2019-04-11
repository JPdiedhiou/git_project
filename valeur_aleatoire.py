import random
nbre_alea = random.randint(0, 9)
rep_user = None
while rep_user != nbre_alea:
      rep_user = int(input("Entrer une valeur entre 0 et 9 :"))
      if rep_user < nbre_alea:
         print("Le nombre aléatoire est plus petit")
      elif rep_user > nbre_alea:
         print("Le nombre aléatoire est plus petit")
      else:
         print("Bravo !! Tu as gagné ")

